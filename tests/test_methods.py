import unittest
from typing import Union

from image_processor_client import Client

import asyncio


class DiscordMethodsTest(unittest.TestCase):

    SAMPLE_SS_MSG_DATA = {
        "name": "The Cosmos",
        "message_content": "Python unittests test message content.",
        "avatar_url": "https://i.imgur.com/qgATqeF.png",
    }

    @staticmethod
    def __run_async(function):
        return asyncio.get_event_loop().run_until_complete(function)

    def test_get_msg_ss(self):
        return self.__run_async(self._get_msg_ss())

    async def _get_msg_ss(self):
        client = Client()
        ss_bytes = await client.discord.ss_message(**self.SAMPLE_SS_MSG_DATA)
        self.assertIsInstance(ss_bytes, Union[bytes])
