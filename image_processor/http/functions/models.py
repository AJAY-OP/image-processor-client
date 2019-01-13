from abc import ABC, abstractmethod

from image_processor.http.response import HttpResponseData
from image_processor.http.route import Route


class ImageFunction(ABC):

    @abstractmethod
    def route(self, path, method: str = "POST", **params):
        raise NotImplementedError

    @abstractmethod
    async def request(self, route: Route, **kwargs) -> HttpResponseData:
        raise NotImplementedError
