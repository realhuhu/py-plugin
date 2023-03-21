from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Anonymous(_message.Message):
    __slots__ = ["flag", "id", "name"]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    flag: str
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., flag: _Optional[str] = ...) -> None: ...

class AnonymousSegment(_message.Message):
    __slots__ = ["ignore"]
    IGNORE_FIELD_NUMBER: _ClassVar[int]
    ignore: bool
    def __init__(self, ignore: bool = ...) -> None: ...

class AtSegment(_message.Message):
    __slots__ = ["qq"]
    QQ_FIELD_NUMBER: _ClassVar[int]
    qq: str
    def __init__(self, qq: _Optional[str] = ...) -> None: ...

class ContactSegment(_message.Message):
    __slots__ = ["id", "type"]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: str
    def __init__(self, type: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class CustomMusicSegment(_message.Message):
    __slots__ = ["audio", "content", "image", "title", "type", "url"]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    audio: str
    content: str
    image: str
    title: str
    type: str
    url: str
    def __init__(self, type: _Optional[str] = ..., url: _Optional[str] = ..., audio: _Optional[str] = ..., title: _Optional[str] = ..., content: _Optional[str] = ..., image: _Optional[str] = ...) -> None: ...

class DeleteMessageRequest(_message.Message):
    __slots__ = ["message_id"]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    def __init__(self, message_id: _Optional[str] = ...) -> None: ...

class DeleteMessageResult(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DiceSegment(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Event(_message.Message):
    __slots__ = ["friend_add_notice", "friend_recall_notice", "friend_request", "group_admin_notice", "group_ban_notice", "group_decrease_notice", "group_increase_notice", "group_message", "group_recall_notice", "group_request", "plugins", "poke_notify", "private_message", "self_id"]
    FRIEND_ADD_NOTICE_FIELD_NUMBER: _ClassVar[int]
    FRIEND_RECALL_NOTICE_FIELD_NUMBER: _ClassVar[int]
    FRIEND_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GROUP_ADMIN_NOTICE_FIELD_NUMBER: _ClassVar[int]
    GROUP_BAN_NOTICE_FIELD_NUMBER: _ClassVar[int]
    GROUP_DECREASE_NOTICE_FIELD_NUMBER: _ClassVar[int]
    GROUP_INCREASE_NOTICE_FIELD_NUMBER: _ClassVar[int]
    GROUP_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    GROUP_RECALL_NOTICE_FIELD_NUMBER: _ClassVar[int]
    GROUP_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PLUGINS_FIELD_NUMBER: _ClassVar[int]
    POKE_NOTIFY_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    friend_add_notice: FriendAddNoticeEvent
    friend_recall_notice: FriendRecallNoticeEvent
    friend_request: FriendRequestEvent
    group_admin_notice: GroupAdminNoticeEvent
    group_ban_notice: GroupBanNoticeEvent
    group_decrease_notice: GroupDecreaseNoticeEvent
    group_increase_notice: GroupIncreaseNoticeEvent
    group_message: GroupMessageEvent
    group_recall_notice: GroupRecallNoticeEvent
    group_request: GroupRequestEvent
    plugins: _containers.RepeatedScalarFieldContainer[str]
    poke_notify: PokeNotifyEvent
    private_message: PrivateMessageEvent
    self_id: str
    def __init__(self, plugins: _Optional[_Iterable[str]] = ..., self_id: _Optional[str] = ..., friend_request: _Optional[_Union[FriendRequestEvent, _Mapping]] = ..., group_request: _Optional[_Union[GroupRequestEvent, _Mapping]] = ..., private_message: _Optional[_Union[PrivateMessageEvent, _Mapping]] = ..., group_message: _Optional[_Union[GroupMessageEvent, _Mapping]] = ..., friend_add_notice: _Optional[_Union[FriendAddNoticeEvent, _Mapping]] = ..., friend_recall_notice: _Optional[_Union[FriendRecallNoticeEvent, _Mapping]] = ..., group_increase_notice: _Optional[_Union[GroupIncreaseNoticeEvent, _Mapping]] = ..., group_decrease_notice: _Optional[_Union[GroupDecreaseNoticeEvent, _Mapping]] = ..., group_recall_notice: _Optional[_Union[GroupRecallNoticeEvent, _Mapping]] = ..., group_ban_notice: _Optional[_Union[GroupBanNoticeEvent, _Mapping]] = ..., group_admin_notice: _Optional[_Union[GroupAdminNoticeEvent, _Mapping]] = ..., poke_notify: _Optional[_Union[PokeNotifyEvent, _Mapping]] = ...) -> None: ...

class FaceSegment(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ForwardSegment(_message.Message):
    __slots__ = ["content", "name", "uin"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UIN_FIELD_NUMBER: _ClassVar[int]
    content: _containers.RepeatedCompositeFieldContainer[SendibleMessageSegment]
    name: str
    uin: str
    def __init__(self, name: _Optional[str] = ..., uin: _Optional[str] = ..., content: _Optional[_Iterable[_Union[SendibleMessageSegment, _Mapping]]] = ...) -> None: ...

class Friend(_message.Message):
    __slots__ = ["nickname", "remark", "sex", "user_id"]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    REMARK_FIELD_NUMBER: _ClassVar[int]
    SEX_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    nickname: str
    remark: str
    sex: str
    user_id: int
    def __init__(self, user_id: _Optional[int] = ..., nickname: _Optional[str] = ..., sex: _Optional[str] = ..., remark: _Optional[str] = ...) -> None: ...

class FriendAddNoticeEvent(_message.Message):
    __slots__ = ["self_id", "time", "user_id"]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    self_id: int
    time: int
    user_id: int
    def __init__(self, time: _Optional[int] = ..., self_id: _Optional[int] = ..., user_id: _Optional[int] = ...) -> None: ...

class FriendRecallNoticeEvent(_message.Message):
    __slots__ = ["message_id", "self_id", "time", "user_id"]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    self_id: int
    time: int
    user_id: int
    def __init__(self, time: _Optional[int] = ..., self_id: _Optional[int] = ..., user_id: _Optional[int] = ..., message_id: _Optional[str] = ...) -> None: ...

class FriendRequestEvent(_message.Message):
    __slots__ = ["comment", "flag", "self_id", "time", "user_id"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    comment: str
    flag: str
    self_id: int
    time: int
    user_id: int
    def __init__(self, time: _Optional[int] = ..., self_id: _Optional[int] = ..., user_id: _Optional[int] = ..., comment: _Optional[str] = ..., flag: _Optional[str] = ...) -> None: ...

class GetForwardMessageRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetForwardMessageResult(_message.Message):
    __slots__ = ["messages"]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[ForwardSegment]
    def __init__(self, messages: _Optional[_Iterable[_Union[ForwardSegment, _Mapping]]] = ...) -> None: ...

class GetFriendListRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetFriendListResult(_message.Message):
    __slots__ = ["friend_list"]
    FRIEND_LIST_FIELD_NUMBER: _ClassVar[int]
    friend_list: _containers.RepeatedCompositeFieldContainer[Friend]
    def __init__(self, friend_list: _Optional[_Iterable[_Union[Friend, _Mapping]]] = ...) -> None: ...

class GetGroupInfoRequest(_message.Message):
    __slots__ = ["group_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    def __init__(self, group_id: _Optional[int] = ...) -> None: ...

class GetGroupInfoResult(_message.Message):
    __slots__ = ["group"]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: Group
    def __init__(self, group: _Optional[_Union[Group, _Mapping]] = ...) -> None: ...

class GetGroupListRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetGroupListResult(_message.Message):
    __slots__ = ["group_list"]
    GROUP_LIST_FIELD_NUMBER: _ClassVar[int]
    group_list: _containers.RepeatedCompositeFieldContainer[Group]
    def __init__(self, group_list: _Optional[_Iterable[_Union[Group, _Mapping]]] = ...) -> None: ...

class GetGroupMemberInfoRequest(_message.Message):
    __slots__ = ["group_id", "user_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    user_id: int
    def __init__(self, group_id: _Optional[int] = ..., user_id: _Optional[int] = ...) -> None: ...

class GetGroupMemberInfoResult(_message.Message):
    __slots__ = ["member"]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    member: Member
    def __init__(self, member: _Optional[_Union[Member, _Mapping]] = ...) -> None: ...

class GetGroupMemberListRequest(_message.Message):
    __slots__ = ["group_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    def __init__(self, group_id: _Optional[int] = ...) -> None: ...

class GetGroupMemberListResult(_message.Message):
    __slots__ = ["member_list"]
    MEMBER_LIST_FIELD_NUMBER: _ClassVar[int]
    member_list: _containers.RepeatedCompositeFieldContainer[Member]
    def __init__(self, member_list: _Optional[_Iterable[_Union[Member, _Mapping]]] = ...) -> None: ...

class GetMessageRequest(_message.Message):
    __slots__ = ["message_id"]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    def __init__(self, message_id: _Optional[str] = ...) -> None: ...

class GetMessageResult(_message.Message):
    __slots__ = ["message", "message_id", "real_id", "sender", "time"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    REAL_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    message: _containers.RepeatedCompositeFieldContainer[ReceivableMessageSegment]
    message_id: str
    real_id: int
    sender: Sender
    time: int
    def __init__(self, message_id: _Optional[str] = ..., real_id: _Optional[int] = ..., sender: _Optional[_Union[Sender, _Mapping]] = ..., time: _Optional[int] = ..., message: _Optional[_Iterable[_Union[ReceivableMessageSegment, _Mapping]]] = ...) -> None: ...

class GetSelfInfoRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetSelfInfoResult(_message.Message):
    __slots__ = ["nickname", "user_id"]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    nickname: str
    user_id: int
    def __init__(self, user_id: _Optional[int] = ..., nickname: _Optional[str] = ...) -> None: ...

class GetUserInfoRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class GetUserInfoResult(_message.Message):
    __slots__ = ["user"]
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class Group(_message.Message):
    __slots__ = ["group_create_time", "group_id", "group_level", "group_name", "max_member_count", "member_count"]
    GROUP_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_LEVEL_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    MAX_MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    group_create_time: int
    group_id: int
    group_level: int
    group_name: str
    max_member_count: int
    member_count: int
    def __init__(self, group_id: _Optional[int] = ..., group_name: _Optional[str] = ..., group_create_time: _Optional[int] = ..., group_level: _Optional[int] = ..., member_count: _Optional[int] = ..., max_member_count: _Optional[int] = ...) -> None: ...

class GroupAdminNoticeEvent(_message.Message):
    __slots__ = ["group_id", "self_id", "sub_type", "time", "user_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    self_id: int
    sub_type: str
    time: int
    user_id: int
    def __init__(self, time: _Optional[int] = ..., self_id: _Optional[int] = ..., sub_type: _Optional[str] = ..., user_id: _Optional[int] = ..., group_id: _Optional[int] = ...) -> None: ...

class GroupBanNoticeEvent(_message.Message):
    __slots__ = ["duration", "group_id", "operator_id", "self_id", "sub_type", "time", "user_id"]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_ID_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    duration: int
    group_id: int
    operator_id: int
    self_id: int
    sub_type: str
    time: int
    user_id: int
    def __init__(self, time: _Optional[int] = ..., self_id: _Optional[int] = ..., sub_type: _Optional[str] = ..., user_id: _Optional[int] = ..., group_id: _Optional[int] = ..., operator_id: _Optional[int] = ..., duration: _Optional[int] = ...) -> None: ...

class GroupDecreaseNoticeEvent(_message.Message):
    __slots__ = ["group_id", "operator_id", "self_id", "sub_type", "time", "user_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_ID_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    operator_id: int
    self_id: int
    sub_type: str
    time: int
    user_id: int
    def __init__(self, time: _Optional[int] = ..., self_id: _Optional[int] = ..., sub_type: _Optional[str] = ..., user_id: _Optional[int] = ..., group_id: _Optional[int] = ..., operator_id: _Optional[int] = ...) -> None: ...

class GroupIncreaseNoticeEvent(_message.Message):
    __slots__ = ["group_id", "operator_id", "self_id", "sub_type", "time", "user_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_ID_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    operator_id: int
    self_id: int
    sub_type: str
    time: int
    user_id: int
    def __init__(self, time: _Optional[int] = ..., self_id: _Optional[int] = ..., sub_type: _Optional[str] = ..., user_id: _Optional[int] = ..., group_id: _Optional[int] = ..., operator_id: _Optional[int] = ...) -> None: ...

class GroupMessageEvent(_message.Message):
    __slots__ = ["anonymous", "group_id", "message", "message_id", "raw_message", "reply", "self_id", "sender", "sub_type", "time", "to_me", "user_id"]
    ANONYMOUS_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    RAW_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    TO_ME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    anonymous: Anonymous
    group_id: int
    message: _containers.RepeatedCompositeFieldContainer[ReceivableMessageSegment]
    message_id: str
    raw_message: str
    reply: Reply
    self_id: int
    sender: Sender
    sub_type: str
    time: int
    to_me: bool
    user_id: int
    def __init__(self, time: _Optional[int] = ..., self_id: _Optional[int] = ..., sub_type: _Optional[str] = ..., message_id: _Optional[str] = ..., group_id: _Optional[int] = ..., user_id: _Optional[int] = ..., anonymous: _Optional[_Union[Anonymous, _Mapping]] = ..., message: _Optional[_Iterable[_Union[ReceivableMessageSegment, _Mapping]]] = ..., raw_message: _Optional[str] = ..., sender: _Optional[_Union[Sender, _Mapping]] = ..., to_me: bool = ..., reply: _Optional[_Union[Reply, _Mapping]] = ...) -> None: ...

class GroupMessageResponse(_message.Message):
    __slots__ = ["group_id", "message"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    message: _containers.RepeatedCompositeFieldContainer[SendibleMessageSegment]
    def __init__(self, group_id: _Optional[int] = ..., message: _Optional[_Iterable[_Union[SendibleMessageSegment, _Mapping]]] = ...) -> None: ...

class GroupRecallNoticeEvent(_message.Message):
    __slots__ = ["group_id", "message_id", "operator_id", "self_id", "time", "user_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_ID_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    message_id: str
    operator_id: int
    self_id: int
    time: int
    user_id: int
    def __init__(self, time: _Optional[int] = ..., self_id: _Optional[int] = ..., user_id: _Optional[int] = ..., group_id: _Optional[int] = ..., operator_id: _Optional[int] = ..., message_id: _Optional[str] = ...) -> None: ...

class GroupRequestEvent(_message.Message):
    __slots__ = ["comment", "flag", "group_id", "self_id", "sub_type", "time", "user_id"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    comment: str
    flag: str
    group_id: int
    self_id: int
    sub_type: str
    time: int
    user_id: int
    def __init__(self, time: _Optional[int] = ..., self_id: _Optional[int] = ..., sub_type: _Optional[str] = ..., group_id: _Optional[int] = ..., user_id: _Optional[int] = ..., comment: _Optional[str] = ..., flag: _Optional[str] = ...) -> None: ...

class Head(_message.Message):
    __slots__ = ["self_id"]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    self_id: str
    def __init__(self, self_id: _Optional[str] = ...) -> None: ...

class ImageSegment(_message.Message):
    __slots__ = ["content", "file", "timeout", "type", "url"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    file: str
    timeout: str
    type: str
    url: str
    def __init__(self, file: _Optional[str] = ..., type: _Optional[str] = ..., url: _Optional[str] = ..., content: _Optional[bytes] = ..., timeout: _Optional[str] = ...) -> None: ...

class JsonSegment(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: str
    def __init__(self, data: _Optional[str] = ...) -> None: ...

class LocationSegment(_message.Message):
    __slots__ = ["content", "lat", "lon", "title"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    LAT_FIELD_NUMBER: _ClassVar[int]
    LON_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    content: str
    lat: str
    lon: str
    title: str
    def __init__(self, lat: _Optional[str] = ..., lon: _Optional[str] = ..., title: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class Member(_message.Message):
    __slots__ = ["age", "area", "card", "group_id", "join_time", "last_sent_time", "level", "nickname", "role", "sex", "shutup_timestamp", "title", "title_expire_time", "user_id"]
    AGE_FIELD_NUMBER: _ClassVar[int]
    AREA_FIELD_NUMBER: _ClassVar[int]
    CARD_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    JOIN_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_SENT_TIME_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    SEX_FIELD_NUMBER: _ClassVar[int]
    SHUTUP_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TITLE_EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    age: int
    area: str
    card: str
    group_id: int
    join_time: int
    last_sent_time: int
    level: int
    nickname: str
    role: str
    sex: str
    shutup_timestamp: int
    title: str
    title_expire_time: int
    user_id: int
    def __init__(self, group_id: _Optional[int] = ..., user_id: _Optional[int] = ..., nickname: _Optional[str] = ..., card: _Optional[str] = ..., sex: _Optional[str] = ..., age: _Optional[int] = ..., area: _Optional[str] = ..., join_time: _Optional[int] = ..., last_sent_time: _Optional[int] = ..., level: _Optional[int] = ..., role: _Optional[str] = ..., title: _Optional[str] = ..., title_expire_time: _Optional[int] = ..., shutup_timestamp: _Optional[int] = ...) -> None: ...

class MusicSegment(_message.Message):
    __slots__ = ["id", "type"]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: str
    def __init__(self, type: _Optional[str] = ..., id: _Optional[int] = ...) -> None: ...

class OptionCode(_message.Message):
    __slots__ = ["code"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: int
    def __init__(self, code: _Optional[int] = ...) -> None: ...

class PokeNotifyEvent(_message.Message):
    __slots__ = ["group_id", "self_id", "target_id", "time", "user_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    self_id: int
    target_id: int
    time: int
    user_id: int
    def __init__(self, time: _Optional[int] = ..., self_id: _Optional[int] = ..., user_id: _Optional[int] = ..., target_id: _Optional[int] = ..., group_id: _Optional[int] = ...) -> None: ...

class PokeSegment(_message.Message):
    __slots__ = ["id", "name", "type"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    type: str
    def __init__(self, type: _Optional[str] = ..., id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class PrivateMessageEvent(_message.Message):
    __slots__ = ["message", "message_id", "raw_message", "reply", "self_id", "sender", "sub_type", "time", "to_me", "user_id"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    RAW_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    TO_ME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    message: _containers.RepeatedCompositeFieldContainer[ReceivableMessageSegment]
    message_id: str
    raw_message: str
    reply: Reply
    self_id: int
    sender: Sender
    sub_type: str
    time: int
    to_me: bool
    user_id: int
    def __init__(self, time: _Optional[int] = ..., self_id: _Optional[int] = ..., sub_type: _Optional[str] = ..., message_id: _Optional[str] = ..., user_id: _Optional[int] = ..., message: _Optional[_Iterable[_Union[ReceivableMessageSegment, _Mapping]]] = ..., raw_message: _Optional[str] = ..., sender: _Optional[_Union[Sender, _Mapping]] = ..., to_me: bool = ..., reply: _Optional[_Union[Reply, _Mapping]] = ...) -> None: ...

class PrivateMessageResponse(_message.Message):
    __slots__ = ["message", "user_id"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    message: _containers.RepeatedCompositeFieldContainer[SendibleMessageSegment]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ..., message: _Optional[_Iterable[_Union[SendibleMessageSegment, _Mapping]]] = ...) -> None: ...

class ReceivableMessageSegment(_message.Message):
    __slots__ = ["at", "dice", "face", "image", "json", "location", "poke", "record", "reply", "rps", "share", "text", "video", "xml"]
    AT_FIELD_NUMBER: _ClassVar[int]
    DICE_FIELD_NUMBER: _ClassVar[int]
    FACE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    JSON_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    POKE_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    RPS_FIELD_NUMBER: _ClassVar[int]
    SHARE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    XML_FIELD_NUMBER: _ClassVar[int]
    at: AtSegment
    dice: DiceSegment
    face: FaceSegment
    image: ImageSegment
    json: JsonSegment
    location: LocationSegment
    poke: PokeSegment
    record: RecordSegment
    reply: ReplySegment
    rps: RpsSegment
    share: ShareSegment
    text: TextSegment
    video: VideoSegment
    xml: XmlSegment
    def __init__(self, text: _Optional[_Union[TextSegment, _Mapping]] = ..., at: _Optional[_Union[AtSegment, _Mapping]] = ..., face: _Optional[_Union[FaceSegment, _Mapping]] = ..., rps: _Optional[_Union[RpsSegment, _Mapping]] = ..., dice: _Optional[_Union[DiceSegment, _Mapping]] = ..., image: _Optional[_Union[ImageSegment, _Mapping]] = ..., record: _Optional[_Union[RecordSegment, _Mapping]] = ..., video: _Optional[_Union[VideoSegment, _Mapping]] = ..., location: _Optional[_Union[LocationSegment, _Mapping]] = ..., share: _Optional[_Union[ShareSegment, _Mapping]] = ..., json: _Optional[_Union[JsonSegment, _Mapping]] = ..., xml: _Optional[_Union[XmlSegment, _Mapping]] = ..., poke: _Optional[_Union[PokeSegment, _Mapping]] = ..., reply: _Optional[_Union[ReplySegment, _Mapping]] = ...) -> None: ...

class RecordSegment(_message.Message):
    __slots__ = ["content", "file", "timeout", "url"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    file: str
    timeout: str
    url: str
    def __init__(self, file: _Optional[str] = ..., url: _Optional[str] = ..., content: _Optional[bytes] = ..., timeout: _Optional[str] = ...) -> None: ...

class Reply(_message.Message):
    __slots__ = ["message", "message_id", "message_type", "real_id", "sender", "time"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    REAL_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    message: _containers.RepeatedCompositeFieldContainer[ReceivableMessageSegment]
    message_id: str
    message_type: str
    real_id: int
    sender: Sender
    time: int
    def __init__(self, time: _Optional[int] = ..., message_type: _Optional[str] = ..., message_id: _Optional[str] = ..., real_id: _Optional[int] = ..., sender: _Optional[_Union[Sender, _Mapping]] = ..., message: _Optional[_Iterable[_Union[ReceivableMessageSegment, _Mapping]]] = ...) -> None: ...

class ReplySegment(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class Request(_message.Message):
    __slots__ = ["delete_message", "get_forward_message", "get_friend_list", "get_group_info", "get_group_list", "get_group_member_info", "get_group_member_list", "get_message", "get_self_info", "get_user_info", "request_id", "self_id", "send_forward_message", "send_like", "send_message", "set_friend_add_request", "set_group_add_request", "set_group_admin", "set_group_anonymous", "set_group_anonymous_ban", "set_group_ban", "set_group_card", "set_group_kick", "set_group_leave", "set_group_name", "set_group_special_title", "set_group_whole_ban"]
    DELETE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    GET_FORWARD_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    GET_FRIEND_LIST_FIELD_NUMBER: _ClassVar[int]
    GET_GROUP_INFO_FIELD_NUMBER: _ClassVar[int]
    GET_GROUP_LIST_FIELD_NUMBER: _ClassVar[int]
    GET_GROUP_MEMBER_INFO_FIELD_NUMBER: _ClassVar[int]
    GET_GROUP_MEMBER_LIST_FIELD_NUMBER: _ClassVar[int]
    GET_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    GET_SELF_INFO_FIELD_NUMBER: _ClassVar[int]
    GET_USER_INFO_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    SEND_FORWARD_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SEND_LIKE_FIELD_NUMBER: _ClassVar[int]
    SEND_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SET_FRIEND_ADD_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SET_GROUP_ADD_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SET_GROUP_ADMIN_FIELD_NUMBER: _ClassVar[int]
    SET_GROUP_ANONYMOUS_BAN_FIELD_NUMBER: _ClassVar[int]
    SET_GROUP_ANONYMOUS_FIELD_NUMBER: _ClassVar[int]
    SET_GROUP_BAN_FIELD_NUMBER: _ClassVar[int]
    SET_GROUP_CARD_FIELD_NUMBER: _ClassVar[int]
    SET_GROUP_KICK_FIELD_NUMBER: _ClassVar[int]
    SET_GROUP_LEAVE_FIELD_NUMBER: _ClassVar[int]
    SET_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    SET_GROUP_SPECIAL_TITLE_FIELD_NUMBER: _ClassVar[int]
    SET_GROUP_WHOLE_BAN_FIELD_NUMBER: _ClassVar[int]
    delete_message: DeleteMessageRequest
    get_forward_message: GetForwardMessageRequest
    get_friend_list: GetFriendListRequest
    get_group_info: GetGroupInfoRequest
    get_group_list: GetGroupListRequest
    get_group_member_info: GetGroupMemberInfoRequest
    get_group_member_list: GetGroupMemberListRequest
    get_message: GetMessageRequest
    get_self_info: GetSelfInfoRequest
    get_user_info: GetUserInfoRequest
    request_id: str
    self_id: str
    send_forward_message: SendForwardMessageRequest
    send_like: SendLikeRequest
    send_message: SendMessageRequest
    set_friend_add_request: SetFriendAddRequestRequest
    set_group_add_request: SetGroupAddRequestRequest
    set_group_admin: SetGroupAdminRequest
    set_group_anonymous: SetGroupAnonymousRequest
    set_group_anonymous_ban: SetGroupAnonymousBanRequest
    set_group_ban: SetGroupBanRequest
    set_group_card: SetGroupCardRequest
    set_group_kick: SetGroupKickRequest
    set_group_leave: SetGroupLeaveRequest
    set_group_name: SetGroupNameRequest
    set_group_special_title: SetGroupSpecialTitleRequest
    set_group_whole_ban: SetGroupWholeBanRequest
    def __init__(self, request_id: _Optional[str] = ..., self_id: _Optional[str] = ..., send_message: _Optional[_Union[SendMessageRequest, _Mapping]] = ..., delete_message: _Optional[_Union[DeleteMessageRequest, _Mapping]] = ..., get_message: _Optional[_Union[GetMessageRequest, _Mapping]] = ..., get_forward_message: _Optional[_Union[GetForwardMessageRequest, _Mapping]] = ..., send_like: _Optional[_Union[SendLikeRequest, _Mapping]] = ..., set_group_kick: _Optional[_Union[SetGroupKickRequest, _Mapping]] = ..., set_group_ban: _Optional[_Union[SetGroupBanRequest, _Mapping]] = ..., set_group_anonymous_ban: _Optional[_Union[SetGroupAnonymousBanRequest, _Mapping]] = ..., set_group_whole_ban: _Optional[_Union[SetGroupWholeBanRequest, _Mapping]] = ..., set_group_admin: _Optional[_Union[SetGroupAdminRequest, _Mapping]] = ..., set_group_anonymous: _Optional[_Union[SetGroupAnonymousRequest, _Mapping]] = ..., set_group_card: _Optional[_Union[SetGroupCardRequest, _Mapping]] = ..., set_group_name: _Optional[_Union[SetGroupNameRequest, _Mapping]] = ..., set_group_leave: _Optional[_Union[SetGroupLeaveRequest, _Mapping]] = ..., set_group_special_title: _Optional[_Union[SetGroupSpecialTitleRequest, _Mapping]] = ..., set_friend_add_request: _Optional[_Union[SetFriendAddRequestRequest, _Mapping]] = ..., set_group_add_request: _Optional[_Union[SetGroupAddRequestRequest, _Mapping]] = ..., get_self_info: _Optional[_Union[GetSelfInfoRequest, _Mapping]] = ..., get_user_info: _Optional[_Union[GetUserInfoRequest, _Mapping]] = ..., get_friend_list: _Optional[_Union[GetFriendListRequest, _Mapping]] = ..., get_group_info: _Optional[_Union[GetGroupInfoRequest, _Mapping]] = ..., get_group_list: _Optional[_Union[GetGroupListRequest, _Mapping]] = ..., get_group_member_info: _Optional[_Union[GetGroupMemberInfoRequest, _Mapping]] = ..., get_group_member_list: _Optional[_Union[GetGroupMemberListRequest, _Mapping]] = ..., send_forward_message: _Optional[_Union[SendForwardMessageRequest, _Mapping]] = ...) -> None: ...

class Result(_message.Message):
    __slots__ = ["delete_message", "get_forward_message", "get_friend_list", "get_group_info", "get_group_list", "get_group_member_info", "get_group_member_list", "get_message", "get_self_info", "get_user_info", "request_id", "self_id", "send_forward_message", "send_like", "send_message", "set_friend_add_request", "set_group_add_request", "set_group_admin", "set_group_anonymous", "set_group_anonymous_ban", "set_group_ban", "set_group_card", "set_group_kick", "set_group_leave", "set_group_name", "set_group_special_title", "set_group_whole_ban"]
    DELETE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    GET_FORWARD_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    GET_FRIEND_LIST_FIELD_NUMBER: _ClassVar[int]
    GET_GROUP_INFO_FIELD_NUMBER: _ClassVar[int]
    GET_GROUP_LIST_FIELD_NUMBER: _ClassVar[int]
    GET_GROUP_MEMBER_INFO_FIELD_NUMBER: _ClassVar[int]
    GET_GROUP_MEMBER_LIST_FIELD_NUMBER: _ClassVar[int]
    GET_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    GET_SELF_INFO_FIELD_NUMBER: _ClassVar[int]
    GET_USER_INFO_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    SEND_FORWARD_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SEND_LIKE_FIELD_NUMBER: _ClassVar[int]
    SEND_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SET_FRIEND_ADD_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SET_GROUP_ADD_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SET_GROUP_ADMIN_FIELD_NUMBER: _ClassVar[int]
    SET_GROUP_ANONYMOUS_BAN_FIELD_NUMBER: _ClassVar[int]
    SET_GROUP_ANONYMOUS_FIELD_NUMBER: _ClassVar[int]
    SET_GROUP_BAN_FIELD_NUMBER: _ClassVar[int]
    SET_GROUP_CARD_FIELD_NUMBER: _ClassVar[int]
    SET_GROUP_KICK_FIELD_NUMBER: _ClassVar[int]
    SET_GROUP_LEAVE_FIELD_NUMBER: _ClassVar[int]
    SET_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    SET_GROUP_SPECIAL_TITLE_FIELD_NUMBER: _ClassVar[int]
    SET_GROUP_WHOLE_BAN_FIELD_NUMBER: _ClassVar[int]
    delete_message: DeleteMessageResult
    get_forward_message: GetForwardMessageResult
    get_friend_list: GetFriendListResult
    get_group_info: GetGroupInfoResult
    get_group_list: GetGroupListResult
    get_group_member_info: GetGroupMemberInfoResult
    get_group_member_list: GetGroupMemberListResult
    get_message: GetMessageResult
    get_self_info: GetSelfInfoResult
    get_user_info: GetUserInfoResult
    request_id: str
    self_id: str
    send_forward_message: SendForwardMessageResult
    send_like: SendLikeResult
    send_message: SendMessageResult
    set_friend_add_request: SetFriendAddRequestResult
    set_group_add_request: SetGroupAddRequestResult
    set_group_admin: SetGroupAdminResult
    set_group_anonymous: SetGroupAnonymousResult
    set_group_anonymous_ban: SetGroupAnonymousBanResult
    set_group_ban: SetGroupBanResult
    set_group_card: SetGroupCardResult
    set_group_kick: SetGroupKickResult
    set_group_leave: SetGroupLeaveResult
    set_group_name: SetGroupNameResult
    set_group_special_title: SetGroupSpecialTitleResult
    set_group_whole_ban: SetGroupWholeBanResult
    def __init__(self, request_id: _Optional[str] = ..., self_id: _Optional[str] = ..., send_message: _Optional[_Union[SendMessageResult, _Mapping]] = ..., delete_message: _Optional[_Union[DeleteMessageResult, _Mapping]] = ..., get_message: _Optional[_Union[GetMessageResult, _Mapping]] = ..., get_forward_message: _Optional[_Union[GetForwardMessageResult, _Mapping]] = ..., send_like: _Optional[_Union[SendLikeResult, _Mapping]] = ..., set_group_kick: _Optional[_Union[SetGroupKickResult, _Mapping]] = ..., set_group_ban: _Optional[_Union[SetGroupBanResult, _Mapping]] = ..., set_group_anonymous_ban: _Optional[_Union[SetGroupAnonymousBanResult, _Mapping]] = ..., set_group_whole_ban: _Optional[_Union[SetGroupWholeBanResult, _Mapping]] = ..., set_group_admin: _Optional[_Union[SetGroupAdminResult, _Mapping]] = ..., set_group_anonymous: _Optional[_Union[SetGroupAnonymousResult, _Mapping]] = ..., set_group_card: _Optional[_Union[SetGroupCardResult, _Mapping]] = ..., set_group_name: _Optional[_Union[SetGroupNameResult, _Mapping]] = ..., set_group_leave: _Optional[_Union[SetGroupLeaveResult, _Mapping]] = ..., set_group_special_title: _Optional[_Union[SetGroupSpecialTitleResult, _Mapping]] = ..., set_friend_add_request: _Optional[_Union[SetFriendAddRequestResult, _Mapping]] = ..., set_group_add_request: _Optional[_Union[SetGroupAddRequestResult, _Mapping]] = ..., get_self_info: _Optional[_Union[GetSelfInfoResult, _Mapping]] = ..., get_user_info: _Optional[_Union[GetUserInfoResult, _Mapping]] = ..., get_friend_list: _Optional[_Union[GetFriendListResult, _Mapping]] = ..., get_group_info: _Optional[_Union[GetGroupInfoResult, _Mapping]] = ..., get_group_list: _Optional[_Union[GetGroupListResult, _Mapping]] = ..., get_group_member_info: _Optional[_Union[GetGroupMemberInfoResult, _Mapping]] = ..., get_group_member_list: _Optional[_Union[GetGroupMemberListResult, _Mapping]] = ..., send_forward_message: _Optional[_Union[SendForwardMessageResult, _Mapping]] = ...) -> None: ...

class RpsSegment(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SendForwardMessageRequest(_message.Message):
    __slots__ = ["detail_type", "group_id", "message", "user_id"]
    DETAIL_TYPE_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    detail_type: str
    group_id: int
    message: _containers.RepeatedCompositeFieldContainer[ForwardSegment]
    user_id: int
    def __init__(self, detail_type: _Optional[str] = ..., user_id: _Optional[int] = ..., group_id: _Optional[int] = ..., message: _Optional[_Iterable[_Union[ForwardSegment, _Mapping]]] = ...) -> None: ...

class SendForwardMessageResult(_message.Message):
    __slots__ = ["message_id", "time"]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    time: int
    def __init__(self, message_id: _Optional[str] = ..., time: _Optional[int] = ...) -> None: ...

class SendLikeRequest(_message.Message):
    __slots__ = ["times", "user_id"]
    TIMES_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    times: int
    user_id: int
    def __init__(self, user_id: _Optional[int] = ..., times: _Optional[int] = ...) -> None: ...

class SendLikeResult(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SendMessageRequest(_message.Message):
    __slots__ = ["detail_type", "group_id", "message", "user_id"]
    DETAIL_TYPE_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    detail_type: str
    group_id: int
    message: _containers.RepeatedCompositeFieldContainer[SendibleMessageSegment]
    user_id: int
    def __init__(self, detail_type: _Optional[str] = ..., user_id: _Optional[int] = ..., group_id: _Optional[int] = ..., message: _Optional[_Iterable[_Union[SendibleMessageSegment, _Mapping]]] = ...) -> None: ...

class SendMessageResult(_message.Message):
    __slots__ = ["message_id", "time"]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    time: int
    def __init__(self, message_id: _Optional[str] = ..., time: _Optional[int] = ...) -> None: ...

class Sender(_message.Message):
    __slots__ = ["age", "area", "card", "level", "nickname", "role", "sex", "title", "user_id"]
    AGE_FIELD_NUMBER: _ClassVar[int]
    AREA_FIELD_NUMBER: _ClassVar[int]
    CARD_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    SEX_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    age: int
    area: str
    card: str
    level: str
    nickname: str
    role: str
    sex: str
    title: str
    user_id: int
    def __init__(self, user_id: _Optional[int] = ..., nickname: _Optional[str] = ..., sex: _Optional[str] = ..., age: _Optional[int] = ..., card: _Optional[str] = ..., area: _Optional[str] = ..., level: _Optional[str] = ..., role: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...

class SendibleMessageSegment(_message.Message):
    __slots__ = ["anonymous", "at", "contact", "custom_music", "dice", "face", "image", "json", "location", "music", "poke", "record", "reply", "rps", "share", "text", "video", "xml"]
    ANONYMOUS_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_MUSIC_FIELD_NUMBER: _ClassVar[int]
    DICE_FIELD_NUMBER: _ClassVar[int]
    FACE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    JSON_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    MUSIC_FIELD_NUMBER: _ClassVar[int]
    POKE_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    RPS_FIELD_NUMBER: _ClassVar[int]
    SHARE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    XML_FIELD_NUMBER: _ClassVar[int]
    anonymous: AnonymousSegment
    at: AtSegment
    contact: ContactSegment
    custom_music: CustomMusicSegment
    dice: DiceSegment
    face: FaceSegment
    image: ImageSegment
    json: JsonSegment
    location: LocationSegment
    music: MusicSegment
    poke: PokeSegment
    record: RecordSegment
    reply: ReplySegment
    rps: RpsSegment
    share: ShareSegment
    text: TextSegment
    video: VideoSegment
    xml: XmlSegment
    def __init__(self, text: _Optional[_Union[TextSegment, _Mapping]] = ..., face: _Optional[_Union[FaceSegment, _Mapping]] = ..., image: _Optional[_Union[ImageSegment, _Mapping]] = ..., record: _Optional[_Union[RecordSegment, _Mapping]] = ..., video: _Optional[_Union[VideoSegment, _Mapping]] = ..., at: _Optional[_Union[AtSegment, _Mapping]] = ..., rps: _Optional[_Union[RpsSegment, _Mapping]] = ..., dice: _Optional[_Union[DiceSegment, _Mapping]] = ..., poke: _Optional[_Union[PokeSegment, _Mapping]] = ..., anonymous: _Optional[_Union[AnonymousSegment, _Mapping]] = ..., share: _Optional[_Union[ShareSegment, _Mapping]] = ..., contact: _Optional[_Union[ContactSegment, _Mapping]] = ..., location: _Optional[_Union[LocationSegment, _Mapping]] = ..., music: _Optional[_Union[MusicSegment, _Mapping]] = ..., custom_music: _Optional[_Union[CustomMusicSegment, _Mapping]] = ..., reply: _Optional[_Union[ReplySegment, _Mapping]] = ..., xml: _Optional[_Union[XmlSegment, _Mapping]] = ..., json: _Optional[_Union[JsonSegment, _Mapping]] = ...) -> None: ...

class SetFriendAddRequestRequest(_message.Message):
    __slots__ = ["approve", "flag", "remark"]
    APPROVE_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    REMARK_FIELD_NUMBER: _ClassVar[int]
    approve: bool
    flag: str
    remark: str
    def __init__(self, flag: _Optional[str] = ..., approve: bool = ..., remark: _Optional[str] = ...) -> None: ...

class SetFriendAddRequestResult(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetGroupAddRequestRequest(_message.Message):
    __slots__ = ["approve", "flag", "reason", "sub_type"]
    APPROVE_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    approve: bool
    flag: str
    reason: str
    sub_type: str
    def __init__(self, flag: _Optional[str] = ..., sub_type: _Optional[str] = ..., approve: bool = ..., reason: _Optional[str] = ...) -> None: ...

class SetGroupAddRequestResult(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetGroupAdminRequest(_message.Message):
    __slots__ = ["enable", "group_id", "user_id"]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    group_id: int
    user_id: int
    def __init__(self, group_id: _Optional[int] = ..., user_id: _Optional[int] = ..., enable: bool = ...) -> None: ...

class SetGroupAdminResult(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetGroupAnonymousBanRequest(_message.Message):
    __slots__ = ["anonymous", "anonymous_flag", "duration", "flag", "group_id"]
    class AnonymousEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ANONYMOUS_FIELD_NUMBER: _ClassVar[int]
    ANONYMOUS_FLAG_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    anonymous: _containers.ScalarMap[str, str]
    anonymous_flag: str
    duration: int
    flag: str
    group_id: int
    def __init__(self, group_id: _Optional[int] = ..., anonymous: _Optional[_Mapping[str, str]] = ..., flag: _Optional[str] = ..., anonymous_flag: _Optional[str] = ..., duration: _Optional[int] = ...) -> None: ...

class SetGroupAnonymousBanResult(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetGroupAnonymousRequest(_message.Message):
    __slots__ = ["enable", "group_id"]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    group_id: int
    def __init__(self, group_id: _Optional[int] = ..., enable: bool = ...) -> None: ...

class SetGroupAnonymousResult(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetGroupBanRequest(_message.Message):
    __slots__ = ["duration", "group_id", "user_id"]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    duration: int
    group_id: int
    user_id: int
    def __init__(self, group_id: _Optional[int] = ..., user_id: _Optional[int] = ..., duration: _Optional[int] = ...) -> None: ...

class SetGroupBanResult(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetGroupCardRequest(_message.Message):
    __slots__ = ["card", "group_id", "user_id"]
    CARD_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    card: str
    group_id: int
    user_id: int
    def __init__(self, group_id: _Optional[int] = ..., user_id: _Optional[int] = ..., card: _Optional[str] = ...) -> None: ...

class SetGroupCardResult(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetGroupKickRequest(_message.Message):
    __slots__ = ["group_id", "reject_add_request", "user_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    REJECT_ADD_REQUEST_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    reject_add_request: bool
    user_id: int
    def __init__(self, group_id: _Optional[int] = ..., user_id: _Optional[int] = ..., reject_add_request: bool = ...) -> None: ...

class SetGroupKickResult(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetGroupLeaveRequest(_message.Message):
    __slots__ = ["group_id", "is_dismiss"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    IS_DISMISS_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    is_dismiss: bool
    def __init__(self, group_id: _Optional[int] = ..., is_dismiss: bool = ...) -> None: ...

class SetGroupLeaveResult(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetGroupNameRequest(_message.Message):
    __slots__ = ["group_id", "group_name"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    group_name: str
    def __init__(self, group_id: _Optional[int] = ..., group_name: _Optional[str] = ...) -> None: ...

class SetGroupNameResult(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetGroupSpecialTitleRequest(_message.Message):
    __slots__ = ["duration", "group_id", "special_title", "user_id"]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SPECIAL_TITLE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    duration: int
    group_id: int
    special_title: str
    user_id: int
    def __init__(self, group_id: _Optional[int] = ..., user_id: _Optional[int] = ..., special_title: _Optional[str] = ..., duration: _Optional[int] = ...) -> None: ...

class SetGroupSpecialTitleResult(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetGroupWholeBanRequest(_message.Message):
    __slots__ = ["enable", "group_id"]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    group_id: int
    def __init__(self, group_id: _Optional[int] = ..., enable: bool = ...) -> None: ...

class SetGroupWholeBanResult(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ShareSegment(_message.Message):
    __slots__ = ["content", "image", "title", "url"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    content: str
    image: str
    title: str
    url: str
    def __init__(self, url: _Optional[str] = ..., title: _Optional[str] = ..., content: _Optional[str] = ..., image: _Optional[str] = ...) -> None: ...

class TextSegment(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: str
    def __init__(self, data: _Optional[str] = ...) -> None: ...

class ToClient(_message.Message):
    __slots__ = ["request"]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: Request
    def __init__(self, request: _Optional[_Union[Request, _Mapping]] = ...) -> None: ...

class ToServer(_message.Message):
    __slots__ = ["event", "head", "result"]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    HEAD_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    event: Event
    head: Head
    result: Result
    def __init__(self, head: _Optional[_Union[Head, _Mapping]] = ..., event: _Optional[_Union[Event, _Mapping]] = ..., result: _Optional[_Union[Result, _Mapping]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ["age", "nickname", "sex", "user_id"]
    AGE_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    SEX_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    age: str
    nickname: str
    sex: str
    user_id: int
    def __init__(self, user_id: _Optional[int] = ..., nickname: _Optional[str] = ..., sex: _Optional[str] = ..., age: _Optional[str] = ...) -> None: ...

class VideoSegment(_message.Message):
    __slots__ = ["content", "file", "timeout", "url"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    file: str
    timeout: str
    url: str
    def __init__(self, file: _Optional[str] = ..., url: _Optional[str] = ..., content: _Optional[bytes] = ..., timeout: _Optional[str] = ...) -> None: ...

class XmlSegment(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: str
    def __init__(self, data: _Optional[str] = ...) -> None: ...
