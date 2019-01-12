from .http import HttpImageClient


class Client(object):

    def __init__(self, connection_uri: str = None, loop=None):
        self.http = HttpImageClient(uri=connection_uri, loop=loop)
