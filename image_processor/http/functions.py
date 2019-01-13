from abc import ABC, abstractmethod

from .response import HttpResponseData
from .route import Route


class ImageFunctions(ABC):

    @abstractmethod
    def route(self, path, method: str = "POST", **params):
        raise NotImplementedError

    @abstractmethod
    async def request(self, route: Route, **kwargs) -> HttpResponseData:
        raise NotImplementedError

    async def rip_meme(self, text: str, avatar_url: str):
        payload = {
            "text": text,
            "avatar_url": avatar_url
        }
        route = self.route("/rip_meme/")
        data = await self.request(route, json=payload)
        return data
