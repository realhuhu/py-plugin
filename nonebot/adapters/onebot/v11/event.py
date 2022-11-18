# DONE
from copy import deepcopy
from typing import TYPE_CHECKING, Any, Dict, Literal, Optional

from nonebot.typing import overrides
from nonebot.utils import escape_tag
from pydantic import BaseModel, root_validator

from nonebot.adapters import Event as BaseEvent

from .message import Message

if TYPE_CHECKING:
    from .bot import Bot


class Event(BaseEvent):
    time: int
    self_id: int
    post_type: str

    @overrides(BaseEvent)
    def get_type(self) -> str:
        return self.post_type

    @overrides(BaseEvent)
    def get_event_name(self) -> str:
        return self.post_type

    @overrides(BaseEvent)
    def get_event_description(self) -> str:
        return escape_tag(str(self.dict()))

    @overrides(BaseEvent)
    def get_message(self) -> Message:
        raise ValueError("Event has no message!")

    @overrides(BaseEvent)
    def get_user_id(self) -> str:
        raise ValueError("Event has no context!")

    @overrides(BaseEvent)
    def get_session_id(self) -> str:
        raise ValueError("Event has no context!")

    @overrides(BaseEvent)
    def is_tome(self) -> bool:
        return False


class Sender(BaseModel):
    user_id: Optional[int] = None
    nickname: Optional[str] = None
    sex: Optional[str] = None
    age: Optional[int] = None
    card: Optional[str] = None
    area: Optional[str] = None
    level: Optional[str] = None
    role: Optional[str] = None
    title: Optional[str] = None

    class Config:
        extra = "allow"


class Reply(BaseModel):
    time: int
    message_type: str
    message_id: str
    real_id: int
    sender: Sender
    message: Message

    class Config:
        extra = "allow"


class Anonymous(BaseModel):
    id: int
    name: str
    flag: str

    class Config:
        extra = "allow"


class File(BaseModel):
    id: str
    name: str
    size: int
    busid: int

    class Config:
        extra = "allow"


class Status(BaseModel):
    online: bool
    good: bool

    class Config:
        extra = "allow"


class MessageEvent(Event):
    post_type: Literal["message"]
    sub_type: str
    user_id: int
    message_type: str
    message_id: str
    message: Message
    original_message: Message
    raw_message: str
    font: int
    sender: Sender
    to_me: bool = False
    reply: Optional[Reply] = None

    @classmethod
    @root_validator(pre=True, allow_reuse=True)
    def check_message(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        if "message" in values:
            values["original_message"] = deepcopy(values["message"])
        return values

    @overrides(Event)
    def get_event_name(self) -> str:
        sub_type = getattr(self, "sub_type", None)
        return f"{self.post_type}.{self.message_type}" + (
            f".{sub_type}" if sub_type else ""
        )

    @overrides(Event)
    def get_message(self) -> Message:
        return self.message

    @overrides(Event)
    def get_user_id(self) -> str:
        return str(self.user_id)

    @overrides(Event)
    def get_session_id(self) -> str:
        return str(self.user_id)

    @overrides(Event)
    def is_tome(self) -> bool:
        return self.to_me


class PrivateMessageEvent(MessageEvent):
    message_type: Literal["private"]

    @overrides(Event)
    def get_event_description(self) -> str:
        msg = "".join(
            map(
                lambda x: escape_tag(str(x))
                if x.is_text()
                else f"<le>{escape_tag(str(x))}</le>",
                self.message,
            ))
        return (
                f'(私聊:{self.user_id})"'
                + msg
                + '"'
        )


class GroupMessageEvent(MessageEvent):
    message_type: Literal["group"]
    group_id: int
    anonymous: Optional[Anonymous] = None

    @overrides(Event)
    def get_event_description(self) -> str:
        msg = "".join(
            map(
                lambda x: escape_tag(str(x))
                if x.is_text()
                else f"<le>{escape_tag(str(x))}</le>",
                self.message,
            )
        )
        return (
                f'(群聊:{self.group_id} 用户:{self.user_id})"'
                + msg
                + '"'
        )

    @overrides(MessageEvent)
    def get_session_id(self) -> str:
        return f"group_{self.group_id}_{self.user_id}"


# Notice Events
class NoticeEvent(Event):
    post_type: Literal["notice"]
    notice_type: str

    @overrides(Event)
    def get_event_name(self) -> str:
        sub_type = getattr(self, "sub_type", None)
        return f"{self.post_type}.{self.notice_type}" + (
            f".{sub_type}" if sub_type else ""
        )


class GroupAdminNoticeEvent(NoticeEvent):
    notice_type: Literal["group_admin"]
    sub_type: str
    user_id: int
    group_id: int

    @overrides(NoticeEvent)
    def is_tome(self) -> bool:
        return self.user_id == self.self_id

    @overrides(NoticeEvent)
    def get_user_id(self) -> str:
        return str(self.user_id)

    @overrides(NoticeEvent)
    def get_session_id(self) -> str:
        return f"group_{self.group_id}_{self.user_id}"


class GroupDecreaseNoticeEvent(NoticeEvent):
    notice_type: Literal["group_decrease"]
    sub_type: str
    user_id: int
    group_id: int
    operator_id: int

    @overrides(NoticeEvent)
    def is_tome(self) -> bool:
        return self.user_id == self.self_id

    @overrides(NoticeEvent)
    def get_user_id(self) -> str:
        return str(self.user_id)

    @overrides(NoticeEvent)
    def get_session_id(self) -> str:
        return f"group_{self.group_id}_{self.user_id}"


class GroupIncreaseNoticeEvent(NoticeEvent):
    notice_type: Literal["group_increase"]
    sub_type: str
    user_id: int
    group_id: int
    operator_id: int

    @overrides(NoticeEvent)
    def is_tome(self) -> bool:
        return self.user_id == self.self_id

    @overrides(NoticeEvent)
    def get_user_id(self) -> str:
        return str(self.user_id)

    @overrides(NoticeEvent)
    def get_session_id(self) -> str:
        return f"group_{self.group_id}_{self.user_id}"


class GroupBanNoticeEvent(NoticeEvent):
    notice_type: Literal["group_ban"]
    sub_type: str
    user_id: int
    group_id: int
    operator_id: int
    duration: int

    @overrides(NoticeEvent)
    def is_tome(self) -> bool:
        return self.user_id == self.self_id

    @overrides(NoticeEvent)
    def get_user_id(self) -> str:
        return str(self.user_id)

    @overrides(NoticeEvent)
    def get_session_id(self) -> str:
        return f"group_{self.group_id}_{self.user_id}"


class FriendAddNoticeEvent(NoticeEvent):
    notice_type: Literal["friend_add"]
    user_id: int

    @overrides(NoticeEvent)
    def get_user_id(self) -> str:
        return str(self.user_id)

    @overrides(NoticeEvent)
    def get_session_id(self) -> str:
        return str(self.user_id)


class GroupRecallNoticeEvent(NoticeEvent):
    notice_type: Literal["group_recall"]
    user_id: int
    group_id: int
    operator_id: int
    message_id: str

    @overrides(Event)
    def is_tome(self) -> bool:
        return self.user_id == self.self_id

    @overrides(NoticeEvent)
    def get_user_id(self) -> str:
        return str(self.user_id)

    @overrides(NoticeEvent)
    def get_session_id(self) -> str:
        return f"group_{self.group_id}_{self.user_id}"

    @overrides(Event)
    def get_event_description(self) -> str:
        return f"{self.operator_id}撤回了{self.user_id}的消息"


class FriendRecallNoticeEvent(NoticeEvent):
    notice_type: Literal["friend_recall"]
    user_id: int
    message_id: str

    @overrides(NoticeEvent)
    def get_user_id(self) -> str:
        return str(self.user_id)

    @overrides(NoticeEvent)
    def get_session_id(self) -> str:
        return str(self.user_id)

    @overrides(Event)
    def get_event_description(self) -> str:
        return f"{self.user_id}撤回了消息"


class NotifyEvent(NoticeEvent):
    notice_type: Literal["notify"]
    sub_type: str
    user_id: int
    group_id: int

    @overrides(NoticeEvent)
    def get_user_id(self) -> str:
        return str(self.user_id)

    @overrides(NoticeEvent)
    def get_session_id(self) -> str:
        return f"group_{self.group_id}_{self.user_id}"


class PokeNotifyEvent(NotifyEvent):
    sub_type: Literal["poke"]
    target_id: int
    group_id: Optional[int] = None

    @overrides(Event)
    def is_tome(self) -> bool:
        return self.target_id == self.self_id

    @overrides(NotifyEvent)
    def get_session_id(self) -> str:
        if not self.group_id:
            return str(self.user_id)
        return super().get_session_id()


class LuckyKingNotifyEvent(NotifyEvent):
    sub_type: Literal["lucky_king"]
    target_id: int

    @overrides(Event)
    def is_tome(self) -> bool:
        return self.target_id == self.self_id

    @overrides(NotifyEvent)
    def get_user_id(self) -> str:
        return str(self.target_id)

    @overrides(NotifyEvent)
    def get_session_id(self) -> str:
        return f"group_{self.group_id}_{self.target_id}"


class RequestEvent(Event):
    post_type: Literal["request"]
    request_type: str

    @overrides(Event)
    def get_event_name(self) -> str:
        sub_type = getattr(self, "sub_type", None)
        return f"{self.post_type}.{self.request_type}" + (
            f".{sub_type}" if sub_type else ""
        )


class FriendRequestEvent(RequestEvent):
    request_type: Literal["friend"]
    user_id: int
    comment: str
    flag: str

    @overrides(RequestEvent)
    def get_user_id(self) -> str:
        return str(self.user_id)

    @overrides(RequestEvent)
    def get_session_id(self) -> str:
        return str(self.user_id)

    async def approve(self, bot: "Bot", remark: str = ""):
        return await bot.set_friend_add_request(
            flag=self.flag, approve=True, remark=remark
        )

    async def reject(self, bot: "Bot"):
        return await bot.set_friend_add_request(flag=self.flag, approve=False)


class GroupRequestEvent(RequestEvent):
    request_type: Literal["group"]
    sub_type: str
    group_id: int
    user_id: int
    comment: str
    flag: str

    @overrides(RequestEvent)
    def get_user_id(self) -> str:
        return str(self.user_id)

    @overrides(RequestEvent)
    def get_session_id(self) -> str:
        return f"group_{self.group_id}_{self.user_id}"

    async def approve(self, bot: "Bot"):
        return await bot.set_group_add_request(
            flag=self.flag, sub_type=self.sub_type, approve=True
        )

    async def reject(self, bot: "Bot", reason: str = ""):
        return await bot.set_group_add_request(
            flag=self.flag, sub_type=self.sub_type, approve=False, reason=reason
        )
