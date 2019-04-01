from abc import ABC

from .models import ImageFunction


class DiscordFunctions(ImageFunction, ABC):

    async def ss_discord_message(self, **kwargs):
        route = self.route("/discord/ss/message/")
        data = await self.request(route, json=kwargs)
        return data
