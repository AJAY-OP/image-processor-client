from .._http import HttpImageClient


class DiscordMethods(object):

    def __init__(self, http: HttpImageClient):
        self.http = http

    async def ss_message(self, name: str, message_content: str, avatar_url: str, name_color: tuple = None, time_stamp: str = None):

        if name_color:
            name_color = list(name_color)

        kwargs = {
            "name": name,
            "message_content": message_content,
            "avatar_url": avatar_url,
            "name_color": name_color,
            "time_stamp": time_stamp
        }

        data = await self.http.ss_discord_message(**kwargs)
        return data.read_data
