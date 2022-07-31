def upper(request):
    return {
        "message": {
            "upper": request.message.get("raw").upper()
        }
    }


def lower(request):
    return {
        "message": {
            "lower": request.message.get("raw").lower()
        }
    }
