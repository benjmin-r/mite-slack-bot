import unittest
from plugins import track_time

class TestCommandExtraction(unittest.TestCase):

    BOT_NAME = 'mitebot'

    def setUp(self):
        self.wrong_command = '%s proj' % self.BOT_NAME
        self.simple = '%s projects' % self.BOT_NAME
        self.with_arg = '%s projects substrmatch' % self.BOT_NAME
        self.halp = '%s help' % self.BOT_NAME
        self.track_with_args = '%s track prjkey 2h' % self.BOT_NAME
        self.track_wrong_args = '%s track prjkey' % self.BOT_NAME

    def test_wrong_command(self):
        self.assertEqual(
            track_time.extract_command_and_args(self.wrong_command),
            ('help', []))

    def test_help(self):
        self.assertEqual(
            track_time.extract_command_and_args(self.halp),
            ('help', []))

    def test_project_list_wo_args(self):
        self.assertEqual(
            track_time.extract_command_and_args(self.simple),
            ('projects', []))

    def test_project_list_with_args(self):
        self.assertEqual(
            track_time.extract_command_and_args(self.with_arg),
            ('projects', ['substrmatch']))

    def test_track_mandatory_args(self):
        self.assertEqual(
            track_time.extract_command_and_args(self.track_with_args),
            ('track', ['prjkey', '2h']))

    def test_track_wrong_args(self):
        self.assertEqual(
            track_time.extract_command_and_args(self.track_wrong_args),
            ('Command track required 2 mandatory arguments, got 1', []))



if __name__ == '__main__':
    unittest.main()
