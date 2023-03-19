class InitChannelError(Exception):
    ...


class SerializeEventError(Exception):
    def __init__(self, event):
        self.event = event

    def __str__(self):
        return f"event:{self.event}"

    __repr__ = __str__


class DeserializeRequestError(Exception):
    def __init__(self, bot, api):
        self.bot = bot
        self.api = api

    def __str__(self):
        return f"无法处理的api:{self.bot}-{self.api}"

    __repr__ = __str__
