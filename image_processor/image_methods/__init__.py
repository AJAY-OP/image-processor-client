from abc import abstractmethod

from .memes import MemesMethods


class ImageMethods(object):

    @property
    @abstractmethod
    def http(self):
        raise NotImplementedError

    def __init__(self):
        self.memes = MemesMethods(self.http)
