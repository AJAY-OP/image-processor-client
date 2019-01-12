import aiohttp

from .route import Route
from .functions import ImageFunctions
from .exceptions import InvalidFormat


class HttpImageClient(ImageFunctions):

    def __init__(self, uri: str = None, loop=None):
        self.session = aiohttp.ClientSession(loop=loop)
        Route.BASE_URL = Route.BASE_URL or uri
        self._route = Route

    def route(self, path, method: str = "POST", **params):
        return self._route(path, method, **params)

    async def request(self, route: Route, **kwargs):
        method = route.method
        url = route.url
        async with self.session.request(method, url, **kwargs) as response:
            if response.status == 400:
                raise InvalidFormat
            return response
