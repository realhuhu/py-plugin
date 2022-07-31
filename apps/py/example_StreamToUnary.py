from core.lib.decorator import channel


@channel.su
def add(request_iterator):
    nums = []

    for i in request_iterator:
        nums.append(int(i.message.get("num")))

    return {
        "message": {
            "res": f"{'+'.join(map(str, nums))}={sum(nums)}"
        }
    }
