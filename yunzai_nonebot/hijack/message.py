from nonebot import message


def patch(func):
    async def wrapper(*args, **kwargs):
        matcher = args[0]
        event = args[2]
        if matcher.plugin_name.replace("-", "_") not in event.plugins:
            return
        return await func(*args, **kwargs)

    return wrapper


def hijack_matcher():
    message._check_matcher = patch(message._check_matcher)
