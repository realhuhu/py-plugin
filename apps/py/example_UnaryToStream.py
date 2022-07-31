import time
from core.lib.decorator import channel


@channel.us
def who(request):
    yield {
        "message": {
            "res": "我"
        }
    }
    time.sleep(1)
    yield {
        "message": {
            "res": "是"
        }
    }
    time.sleep(1)
    yield {
        "message": {
            "res": "你叠"
        }
    }
