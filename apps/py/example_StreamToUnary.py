config = {
    "type": "StreamToUnary"
}


def add(head, request_iterator):
    nums = [int(head.message.get("num"))]
    for i in request_iterator:
        nums.append(int(i.message.get("num")))
    return {
        "message": {
            "res": f"{'+'.join(map(str, nums))}={sum(nums)}"
        }
    }
