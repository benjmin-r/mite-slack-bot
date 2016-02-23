import os
import re
import logging
import requests

MITE_API_KEY = os.getenv("MITE_API_KEY", None)
MITE_TEAM_NAME = os.getenv("MITE_TEAM_NAME", None)

BOT_NAME = 'mitebot'
COMMANDS = {
    'projects': {
        'help': 'print a list of all projects',
        'opt_args': ['optionally filtering for `arg1`']
    },
    'track': {
        'help': 'track time towards a project',
        'args': ['project', 'amount']
    },
    'help': {'help': 'see this message'}
}


crontable = []
outputs = []
attachments = []
typing_sleep = 0


### 
### TODO generate help text from COMMANDS dict
### 
help_text = """I will respond to the following messages:
`%(name)s projects <substring>` 
`%(name)s help` to see this again.
""" % { 'name': BOT_NAME }


def extract_command_and_args(msg_text):
    words = msg_text.split() # first elem is always bot name
    if len(words) < 2 or words[1] not in COMMANDS:
        return ('help', [])

    ret_cmd = None
    ret_args = None

    ret_cmd = words[1]
    ret_args = words[2:]

    if 'args' in COMMANDS[ret_cmd]:
        mandatory_arg_count = len(COMMANDS[ret_cmd]['args']) 
        if mandatory_arg_count != len(ret_args):
            arg_error = 'Command %s required %i mandatory arguments, got %i' % (
                ret_cmd, mandatory_arg_count, len(ret_args))
            return (arg_error, [])

    return (ret_cmd, ret_args)


def process_message(data):
    logging.debug("process_message:data: {}".format(data))

    (cmd, args) = extract_command_and_args(data['text'])

    if cmd == 'projects':
        prj_str = numbered_projects(args)
        outputs.append([
            data['channel'],
            u'Projects (not just yours):\n' + prj_str
        ])

    elif cmd == 'help':
        outputs.append([data['channel'], "{}".format(help_text)])

    else:
        outputs.append([data['channel'],
            "Sorry, not sure what you mean :cry:\n'{}'".format(cmd)])


def mite_api_GET(path):
    return requests.get('https://%s.mite.yo.lk%s' % (MITE_TEAM_NAME, path),
        headers={
            'X-MiteApiKey': MITE_API_KEY,
            'User-Agent': 'mite-slack github.com/nureineide/mite-slack-bot.git'
        })


def numbered_projects(opt_filter=None):
    ### TODO handle auth & internal server errors
    response = mite_api_GET('/projects.json')
    projects = sorted([p['project'] for p in response.json()])

    if opt_filter is not None and len(opt_filter) == 1:
        projects = filter(lambda p: opt_filter[0]in p['name'], projects)

    return '\n'.join([
        '%i - %s' % (i, projects[i]['name']) for i in range(0, len(projects))
        ])

