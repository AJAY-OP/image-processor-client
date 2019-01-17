import sys

import unittest
from typing import Union

from tests.client import ImageClientTest
from tests.methods import DiscordMethodsTest

sys.path.append("image_processor/")

if __name__ == "__main__":
    unittest.main(Union[DiscordMethodsTest()])
    unittest.main(Union[ImageClientTest()])
