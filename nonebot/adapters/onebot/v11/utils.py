# DONE
from nonebot.utils import logger_wrapper

log = logger_wrapper("OneBot V11")


def escape(s: str, *, escape_comma: bool = True) -> str:
    s = s.replace("&", "&amp;").replace("[", "&#91;").replace("]", "&#93;")
    if escape_comma:
        s = s.replace(",", "&#44;")
    return s


def unescape(s: str) -> str:
    return s.replace("&#44;", ",").replace("&#91;", "[").replace("&#93;", "]").replace("&amp;", "&")
