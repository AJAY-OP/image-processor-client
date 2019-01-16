import unittest

from image_processor import Client
from . import utils


client = Client()


class DiscordMethodsTest(unittest.TestCase):

    SAMPLE_SS_MSG_DATA = {
        "name": "The Cosmos",
        "message_content": "Python unittests test message content.",
        "avatar_url": "https://i.imgur.com/qgATqeF.png",
    }

    def test_get_msg_ss(self):
        return utils.run_async(self._get_msg_ss())

    async def _get_msg_ss(self):
        ss_bytes = await client.discord.ss_message(**self.SAMPLE_SS_MSG_DATA)
        with open("tests/images/msg_ss.png", "wb") as ss_file:
            ss_file.write(ss_bytes)
        files = utils.get_files("tests/images/")
        self.assertIn("msg_ss.png", files)
