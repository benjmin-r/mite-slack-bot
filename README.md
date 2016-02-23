mite-slack-bot
=============

## Overview

A simple slack bot for interacting with the [mite](https://mite.yo.lk) time
tracker.

It's meant to run on [Beep Boop](https://beepboophq.com/) but should actually
run anywhere that can run Python or Docker.

The Slack API documentation can be found [here](https://api.slack.com/).


## Assumptions

* You have already signed up with [Beep Boop](https://beepboophq.com) and have a
  local fork of this project.
* You have sufficient rights in your Slack team to configure a bot and
  generate/access a Slack API token. Go to [Slack's app
  directory](https://slack.com/apps/build) to register your own bot. For playing
  around with a private bot first, choose to [make a custom integration or
  rather a bot](https://slack.com/apps/build/custom-integration) first


## Usage

### Run locally
Install dependencies and run the bot locally.

	pip install -r requirements.txt
	export SLACK_TOKEN=<YOUR SLACK TOKEN>
	export MITE_TEAM_NAME=<YOUR MITE TEAM/ACCOUNT NAME>
	export MITE_API_KEY=<YOUR MITE API KEY>
	python rtmbot.py

Things are looking good if the console prints something like:

	Connected <your bot name> to <your slack team> team at https://<your slack team>.slack.com.

If you want change the logging level, prepend `export LOG_LEVEL=<your level>; `
to the `python rtmbot.py` command.


### Run locally in Docker

	docker build -t starter-python-bot .
	docker run --rm -it -e SLACK_TOKEN=<YOUR SLACK API TOKEN> MITE_API_KEY=<MITEAPIKEY> MITE_TEAM_NAME=<demo> starter-python-bot

## Customizing the Bot

If you are looking to change what the bot responds to and how they respond, take
a look at the `plugins/starter.py` file.  You'll see a function that gets called
on all "message" type events, which has various regular expression matches that
determine when the bot responds and how it responds.  Each "Plugin" is
registered with the RtmBot on startup by scanning the "plugins/" directory and
communicates back to the RtmBot through variables like output[] and
attachments[].

For more information on the Plugins pattern see the sections "Add Plugins" and
"Create Plugins" at:
https://github.com/slackhq/python-rtmbot/blob/master/README.md

## Acknowledgements

This code was forked from
[starter-python-kit](https://github.com/BeepBoopHQ/starter-python-bot) and
utilizes [python-rtmbot](https://github.com/slackhq/python-rtmbot) which again
is based on the awesome
[python-slackclient](https://github.com/slackhq/python-slackclient) project by
[@rawdigits](https://github.com/rawdigits).


## License

See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT).

