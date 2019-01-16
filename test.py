import unittest
from typing import Union

from tests.client import ImageClientTest
from tests.methods import DiscordMethodsTest


if __name__ == "__main__":
    unittest.main(Union[DiscordMethodsTest()])
    unittest.main(Union[ImageClientTest()])
