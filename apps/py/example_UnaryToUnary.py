from core.lib.decorator import channel


@channel.uu
def upper(request):
    return {
        "message": {
            "upper": request.message.get("raw").upper()
        }
    }


@channel.uu
def lower(request):
    return {
        "message": {
            "lower": request.message.get("raw").lower()
        }
    }
