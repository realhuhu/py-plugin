import random
from core.lib.decorator import channel


@channel.ss
def guess(request_iterator):
    num = random.randint(0, 100)

    for i in request_iterator:
        guessNum = int(i.message.get("num"))
        print(guessNum)
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
