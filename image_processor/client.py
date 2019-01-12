from .http import HttpImageClient
from .image_methods import ImageMethods


class Client(ImageMethods):

    def __init__(self, connection_uri: str = None, loop=None):
        self._http = HttpImageClient(uri=connection_uri, loop=loop)

    @property
    def http(self):
        return self._http

    async def close(self):
        return await self.http.session.close()
