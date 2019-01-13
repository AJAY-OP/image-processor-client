from abc import ABC

from .memes import MemeFunctions


FUNCTIONS = [
    MemeFunctions,
]


class ImageFunctions(*FUNCTIONS, ABC):

    pass
