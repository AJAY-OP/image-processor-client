from .._http import HttpImageClient


class DiscordMethods(object):
    """Base class for available discord imaging methods."""

    def __init__(self, http: HttpImageClient):
        self.http = http

    async def ss_message(
            self,
            name: str,
            message_content: str,
            avatar_url: str,
            name_color: tuple = None,
            time_stamp: str = None
    ):
        """Requests server to process screenshot of a discord message using provided parameters and returns image\
        bytes.

        Note
        ----
        For now it only supports text message content.

        Parameters
        ----------
        name : str
            Name of discord User or Member who sent the message.
        message_content : str
            Full clean message content
        avatar_url : str
            Direct avatar URL of discord User or Member who sent the message.
        name_color : tuple, optional
            A tuple representing RGB color of discord User or Message who sent the message. It's default value\
            is set to ``(255, 255, 255)``.
        time_stamp : str, optional
            String representing date and time stamp of epoch when message was sent. Uses ``Today at 11:38 AM``\
            if not provided.

        Returns
        -------
        bytes
            Binary image bytes which appears as screenshot of a discord message.

        """
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
