import os
import asyncio
import unittest

from image_processor import Client


class ImageClientTest(unittest.TestCase):

    RIP_MEME_TEXT = "Test Test Test"
    RIP_MEME_AVATAR_URL = "https://cdn.discordapp.com/avatars/331793750273687553/a_c59ddca1e44a4acb72654999459c58e0.gif"

    def test_client(self):
        client = Client()
        self.assertIsInstance(client, Client)

    def test_client_with_loop(self):
        loop = asyncio.get_event_loop()
        client = Client(loop=loop)
        self.assertIsInstance(client, Client)

    def test_get_rip_meme(self):
        loop = asyncio.get_event_loop()
        client = Client(loop=loop)
        meme_generator = client.rip_meme(self.RIP_MEME_TEXT, self.RIP_MEME_AVATAR_URL)
        meme_bytes = loop.run_until_complete(meme_generator)
        meme_file = open("tests/images/rip_meme.png", "rb")
        meme_file.write(meme_bytes)
        meme_file.close()
        files = os.listdir("tests/images/")
        self.assertIn("rip_meme.png", files)
