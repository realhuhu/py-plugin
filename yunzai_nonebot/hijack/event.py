import re

from nonebot.adapters.onebot import v11, v12
from nonebot.internal.adapter import Event


class OneEvent(Event):
    def get_event_name(self) -> str:
        return self.v11.get_event_name()

    def get_event_description(self) -> str:
        return self.v11.get_event_description()

    def get_user_id(self) -> str:
        return self.v11.get_user_id()

    def get_session_id(self) -> str:
        return self.v11.get_session_id()

    def get_message(self) -> "Message":
        return self.v11.get_message()

    def is_tome(self) -> bool:
        return self.v11.is_tome()

    def get_type(self) -> str:
        return self.v11.get_type()


def strip(func):
    def wrapper(*args, **kwargs):
        description = func(*args, **kwargs)
        return re.sub("Message \d+ ", "", description)

    return wrapper


def hijack_event():
    v11.GroupMessageEvent.get_event_description = strip(v11.GroupMessageEvent.get_event_description)
    v11.PrivateMessageEvent.get_event_description = strip(v11.PrivateMessageEvent.get_event_description)
    v12.PrivateMessageEvent.get_event_description = strip(v12.PrivateMessageEvent.get_event_description)
    v12.PrivateMessageEvent.get_event_description = strip(v12.PrivateMessageEvent.get_event_description)
