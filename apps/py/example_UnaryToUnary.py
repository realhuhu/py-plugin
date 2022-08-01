from core.lib.decorator import channel
from core.lib.type import Request


@channel.uu
def upper(request: Request):
    return {
        "message": {
            "upper": request.message.get("raw1").upper()
        }
    }


@channel.uu
def lower(request: Request):
    return {
        "message": {
            "lower": request.message.get("raw").lower()
        }
    }
