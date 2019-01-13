from ._http import gateway
from . import image_methods


class Client(image_methods.ImageMethods):

    def __init__(self, connection_uri: str = None, loop=None):
        self._http = gateway.HttpImageClient(uri=connection_uri, loop=loop)
        super().__init__()

    @property
    def http(self):
        return self._http

    async def close(self):
        return await self.http.session.close()
