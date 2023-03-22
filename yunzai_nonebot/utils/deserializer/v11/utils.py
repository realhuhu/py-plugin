import os
import base64
from typing import Union
from urllib.request import url2pathname
from urllib.parse import urlparse, unquote

from nonebot.adapters.onebot.v11 import Bot


def message_id_to_str(message_id: Union[int, str]) -> str:
    if isinstance(message_id, str) and not message_id.isdigit():
        return message_id

    if isinstance(message_id, str) and message_id.isdigit():
        message_id = int(message_id)

    return base64.b64encode(bytes.fromhex("{:08x}".format(message_id))).decode("utf-8")


def format_file(bot: Bot, file):
    if hasattr(bot.adapter.config, "server") and isinstance(file, str) and file.startswith("file"):
        with open(os.path.normpath(url2pathname(unquote(urlparse(file).path))), "rb") as f:
            return f.read()
    return file
