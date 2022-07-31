import random

config = {
    "type": "StreamToStream"
}


def guess(head, request_iterator):
    num = random.randint(0, 100)
    guessNum = int(head.message.get("num"))

    if guessNum == num:
        yield {
            "message": {
                "res": "猜对了！",
                "correct": "true"
            }
        }
        return

    else:
        yield {
            "message": {
                "res": f"猜{'大' if guessNum > num else '小'}了",
            }
        }

    for i in request_iterator:
        guessNum = int(i.message.get("num"))
        if guessNum == num:
            yield {
                "message": {
                    "res": "猜对了！",
                    "correct": "true"
                }
            }
            return

        else:
            yield {
                "message": {
                    "res": f"猜{'大' if guessNum > num else '小'}了",
                }
            }
