from abc import ABC

from .memes import MemeFunctions
from .discord import DiscordScreenShotFunctions


FUNCTIONS = [
    MemeFunctions,
    DiscordScreenShotFunctions
]


class ImageFunctions(*FUNCTIONS, ABC):

    pass
