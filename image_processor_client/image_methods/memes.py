from .._http import HttpImageClient


class MemesMethods(object):

    def __init__(self, http: HttpImageClient):
        self.http = http

    async def rip(self, text: str, avatar_url: str) -> bytes:
        data = await self.http.rip_meme(text, avatar_url)
        return data.read_data
