# DONE
from .params import EventType
from .adapters import Bot, Event
from .internal.permission import Permission as Permission


class Message:
    __slots__ = ()

    def __repr__(self) -> str:
        return "Message()"

    async def __call__(self, type: str = EventType()) -> bool:
        return type == "message"


class Notice:
    __slots__ = ()

    def __repr__(self) -> str:
        return "Notice()"

    async def __call__(self, type: str = EventType()) -> bool:
        return type == "notice"


class Request:
    __slots__ = ()

    def __repr__(self) -> str:
        return "Request()"

    async def __call__(self, type: str = EventType()) -> bool:
        return type == "request"


class SuperUser:
    __slots__ = ()

    def __repr__(self) -> str:
        return "Superuser()"

    async def __call__(self, bot: Bot, event: Event) -> bool:
        try:
            user_id = event.get_user_id()
            return user_id in [str(i) for i in bot.config["superusers"]]
        except Exception:
            return False


MESSAGE: Permission = Permission(Message())
NOTICE: Permission = Permission(Notice())
REQUEST: Permission = Permission(Request())
SUPERUSER: Permission = Permission(SuperUser())
