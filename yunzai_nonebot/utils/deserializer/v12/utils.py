import os
from urllib.request import url2pathname
from urllib.parse import urlparse, unquote
from nonebot.adapters.onebot.v12 import Bot


def format_file(bot: Bot, file):
    if hasattr(bot.adapter.config, "server") and isinstance(file, str) and file.startswith("file"):
        with open(os.path.normpath(url2pathname(unquote(urlparse(file).path))), "rb") as f:
            return f.read()
    return file
