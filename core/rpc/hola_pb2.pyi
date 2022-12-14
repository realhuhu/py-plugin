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

class DeleteMsgRequest(_message.Message):
    __slots__ = ["message_id"]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    def __init__(self, message_id: _Optional[str] = ...) -> None: ...

class DeleteMsgResult(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DiceSegment(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Event(_message.Message):
    __slots__ = ["FriendAddNoticeEvent", "FriendRecallNoticeEvent", "FriendRequestEvent", "GroupAdminNoticeEvent", "GroupBanNoticeEvent", "GroupDecreaseNoticeEvent", "GroupIncreaseNoticeEvent", "GroupMessageEvent", "GroupRecallNoticeEvent", "GroupRequestEvent", "PokeNotifyEvent", "PrivateMessageEvent", "plugins", "self_id"]
    FRIENDADDNOTICEEVENT_FIELD_NUMBER: _ClassVar[int]
    FRIENDRECALLNOTICEEVENT_FIELD_NUMBER: _ClassVar[int]
    FRIENDREQUESTEVENT_FIELD_NUMBER: _ClassVar[int]
    FriendAddNoticeEvent: FriendAddNoticeEvent
    FriendRecallNoticeEvent: FriendRecallNoticeEvent
    FriendRequestEvent: FriendRequestEvent
    GROUPADMINNOTICEEVENT_FIELD_NUMBER: _ClassVar[int]
    GROUPBANNOTICEEVENT_FIELD_NUMBER: _ClassVar[int]
    GROUPDECREASENOTICEEVENT_FIELD_NUMBER: _ClassVar[int]
    GROUPINCREASENOTICEEVENT_FIELD_NUMBER: _ClassVar[int]
    GROUPMESSAGEEVENT_FIELD_NUMBER: _ClassVar[int]
    GROUPRECALLNOTICEEVENT_FIELD_NUMBER: _ClassVar[int]
    GROUPREQUESTEVENT_FIELD_NUMBER: _ClassVar[int]
    GroupAdminNoticeEvent: GroupAdminNoticeEvent
    GroupBanNoticeEvent: GroupBanNoticeEvent
    GroupDecreaseNoticeEvent: GroupDecreaseNoticeEvent
    GroupIncreaseNoticeEvent: GroupIncreaseNoticeEvent
    GroupMessageEvent: GroupMessageEvent
    GroupRecallNoticeEvent: GroupRecallNoticeEvent
    GroupRequestEvent: GroupRequestEvent
    PLUGINS_FIELD_NUMBER: _ClassVar[int]
    POKENOTIFYEVENT_FIELD_NUMBER: _ClassVar[int]
    PRIVATEMESSAGEEVENT_FIELD_NUMBER: _ClassVar[int]
    PokeNotifyEvent: PokeNotifyEvent
    PrivateMessageEvent: PrivateMessageEvent
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    plugins: _containers.RepeatedScalarFieldContainer[str]
    self_id: int
    def __init__(self, plugins: _Optional[_Iterable[str]] = ..., self_id: _Optional[int] = ..., FriendRequestEvent: _Optional[_Union[FriendRequestEvent, _Mapping]] = ..., GroupRequestEvent: _Optional[_Union[GroupRequestEvent, _Mapping]] = ..., PrivateMessageEvent: _Optional[_Union[PrivateMessageEvent, _Mapping]] = ..., GroupMessageEvent: _Optional[_Union[GroupMessageEvent, _Mapping]] = ..., FriendAddNoticeEvent: _Optional[_Union[FriendAddNoticeEvent, _Mapping]] = ..., FriendRecallNoticeEvent: _Optional[_Union[FriendRecallNoticeEvent, _Mapping]] = ..., GroupIncreaseNoticeEvent: _Optional[_Union[GroupIncreaseNoticeEvent, _Mapping]] = ..., GroupDecreaseNoticeEvent: _Optional[_Union[GroupDecreaseNoticeEvent, _Mapping]] = ..., GroupRecallNoticeEvent: _Optional[_Union[GroupRecallNoticeEvent, _Mapping]] = ..., GroupBanNoticeEvent: _Optional[_Union[GroupBanNoticeEvent, _Mapping]] = ..., GroupAdminNoticeEvent: _Optional[_Union[GroupAdminNoticeEvent, _Mapping]] = ..., PokeNotifyEvent: _Optional[_Union[PokeNotifyEvent, _Mapping]] = ...) -> None: ...

class FaceSegment(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class FriendAddNoticeEvent(_message.Message):
    __slots__ = ["notice_type", "post_type", "self_id", "time", "user_id"]
    NOTICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    POST_TYPE_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    notice_type: str
    post_type: str
    self_id: int
    time: int
    user_id: int
    def __init__(self, time: _Optional[int] = ..., self_id: _Optional[int] = ..., post_type: _Optional[str] = ..., notice_type: _Optional[str] = ..., user_id: _Optional[int] = ...) -> None: ...

class FriendRecallNoticeEvent(_message.Message):
    __slots__ = ["message_id", "notice_type", "post_type", "self_id", "time", "user_id"]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    NOTICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    POST_TYPE_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    notice_type: str
    post_type: str
    self_id: int
    time: int
    user_id: int
    def __init__(self, time: _Optional[int] = ..., self_id: _Optional[int] = ..., post_type: _Optional[str] = ..., notice_type: _Optional[str] = ..., user_id: _Optional[int] = ..., message_id: _Optional[str] = ...) -> None: ...

class FriendRequestEvent(_message.Message):
    __slots__ = ["comment", "flag", "post_type", "request_type", "self_id", "time", "user_id"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    POST_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TYPE_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    comment: str
    flag: str
    post_type: str
    request_type: str
    self_id: int
    time: int
    user_id: int
    def __init__(self, time: _Optional[int] = ..., self_id: _Optional[int] = ..., post_type: _Optional[str] = ..., request_type: _Optional[str] = ..., user_id: _Optional[int] = ..., comment: _Optional[str] = ..., flag: _Optional[str] = ...) -> None: ...

class GetGroupInfoRequest(_message.Message):
    __slots__ = ["group_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    def __init__(self, group_id: _Optional[int] = ...) -> None: ...

class GetGroupInfoResult(_message.Message):
    __slots__ = ["group_create_time", "group_id", "group_level", "group_memo", "group_name", "max_member_count", "member_count"]
    GROUP_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_LEVEL_FIELD_NUMBER: _ClassVar[int]
    GROUP_MEMO_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    MAX_MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    group_create_time: int
    group_id: int
    group_level: int
    group_memo: str
    group_name: str
    max_member_count: int
    member_count: int
    def __init__(self, group_id: _Optional[int] = ..., group_name: _Optional[str] = ..., group_memo: _Optional[str] = ..., group_create_time: _Optional[int] = ..., group_level: _Optional[int] = ..., member_count: _Optional[int] = ..., max_member_count: _Optional[int] = ...) -> None: ...

class GetGroupMemberInfoRequest(_message.Message):
    __slots__ = ["group_id", "user_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    user_id: int
    def __init__(self, group_id: _Optional[int] = ..., user_id: _Optional[int] = ...) -> None: ...

class GetGroupMemberInfoResult(_message.Message):
    __slots__ = ["age", "area", "card", "card_changeable", "group_id", "join_time", "last_sent_time", "level", "nickname", "role", "sex", "shut_up_timestamp", "title", "title_expire_time", "unfriendly", "user_id"]
    AGE_FIELD_NUMBER: _ClassVar[int]
    AREA_FIELD_NUMBER: _ClassVar[int]
    CARD_CHANGEABLE_FIELD_NUMBER: _ClassVar[int]
    CARD_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    JOIN_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_SENT_TIME_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    SEX_FIELD_NUMBER: _ClassVar[int]
    SHUT_UP_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TITLE_EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    UNFRIENDLY_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    age: int
    area: str
    card: str
    card_changeable: bool
    group_id: int
    join_time: int
    last_sent_time: int
    level: str
    nickname: str
    role: str
    sex: str
    shut_up_timestamp: int
    title: str
    title_expire_time: int
    unfriendly: bool
    user_id: int
    def __init__(self, group_id: _Optional[int] = ..., user_id: _Optional[int] = ..., nickname: _Optional[str] = ..., card: _Optional[str] = ..., sex: _Optional[str] = ..., age: _Optional[int] = ..., area: _Optional[str] = ..., join_time: _Optional[int] = ..., last_sent_time: _Optional[int] = ..., level: _Optional[str] = ..., role: _Optional[str] = ..., unfriendly: bool = ..., title: _Optional[str] = ..., title_expire_time: _Optional[int] = ..., card_changeable: bool = ..., shut_up_timestamp: _Optional[int] = ...) -> None: ...

class GetGroupMemberListRequest(_message.Message):
    __slots__ = ["group_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    def __init__(self, group_id: _Optional[int] = ...) -> None: ...

class GetGroupMemberListResult(_message.Message):
    __slots__ = ["member_list"]
    MEMBER_LIST_FIELD_NUMBER: _ClassVar[int]
    member_list: _containers.RepeatedCompositeFieldContainer[GetGroupMemberInfoResult]
    def __init__(self, member_list: _Optional[_Iterable[_Union[GetGroupMemberInfoResult, _Mapping]]] = ...) -> None: ...

class GetMsgRequest(_message.Message):
    __slots__ = ["message_id"]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: int
    def __init__(self, message_id: _Optional[int] = ...) -> None: ...

class GetMsgResult(_message.Message):
    __slots__ = ["message", "message_id", "real_id", "sender", "time"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    REAL_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    message: _containers.RepeatedCompositeFieldContainer[ReceivableMessageSegment]
    message_id: int
    real_id: int
    sender: Sender
    time: int
    def __init__(self, message_id: _Optional[int] = ..., real_id: _Optional[int] = ..., sender: _Optional[_Union[Sender, _Mapping]] = ..., time: _Optional[int] = ..., message: _Optional[_Iterable[_Union[ReceivableMessageSegment, _Mapping]]] = ...) -> None: ...

class GetStrangerInfoRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class GetStrangerInfoResult(_message.Message):
    __slots__ = ["age", "nickname", "sex", "user_id"]
    AGE_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    SEX_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    age: int
    nickname: str
    sex: str
    user_id: int
    def __init__(self, user_id: _Optional[int] = ..., nickname: _Optional[str] = ..., sex: _Optional[str] = ..., age: _Optional[int] = ...) -> None: ...

class GroupAdminNoticeEvent(_message.Message):
    __slots__ = ["group_id", "notice_type", "post_type", "self_id", "sub_type", "time", "user_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NOTICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    POST_TYPE_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    notice_type: str
    post_type: str
    self_id: int
    sub_type: str
    time: int
    user_id: int
    def __init__(self, time: _Optional[int] = ..., self_id: _Optional[int] = ..., post_type: _Optional[str] = ..., notice_type: _Optional[str] = ..., sub_type: _Optional[str] = ..., user_id: _Optional[int] = ..., group_id: _Optional[int] = ...) -> None: ...

class GroupBanNoticeEvent(_message.Message):
    __slots__ = ["duration", "group_id", "notice_type", "operator_id", "post_type", "self_id", "sub_type", "time", "user_id"]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NOTICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_ID_FIELD_NUMBER: _ClassVar[int]
    POST_TYPE_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    duration: int
    group_id: int
    notice_type: str
    operator_id: int
    post_type: str
    self_id: int
    sub_type: str
    time: int
    user_id: int
    def __init__(self, time: _Optional[int] = ..., self_id: _Optional[int] = ..., post_type: _Optional[str] = ..., notice_type: _Optional[str] = ..., sub_type: _Optional[str] = ..., user_id: _Optional[int] = ..., group_id: _Optional[int] = ..., operator_id: _Optional[int] = ..., duration: _Optional[int] = ...) -> None: ...

class GroupDecreaseNoticeEvent(_message.Message):
    __slots__ = ["group_id", "notice_type", "operator_id", "post_type", "self_id", "sub_type", "time", "user_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NOTICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_ID_FIELD_NUMBER: _ClassVar[int]
    POST_TYPE_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    notice_type: str
    operator_id: int
    post_type: str
    self_id: int
    sub_type: str
    time: int
    user_id: int
    def __init__(self, time: _Optional[int] = ..., self_id: _Optional[int] = ..., post_type: _Optional[str] = ..., notice_type: _Optional[str] = ..., sub_type: _Optional[str] = ..., user_id: _Optional[int] = ..., group_id: _Optional[int] = ..., operator_id: _Optional[int] = ...) -> None: ...

class GroupIncreaseNoticeEvent(_message.Message):
    __slots__ = ["group_id", "notice_type", "operator_id", "post_type", "self_id", "sub_type", "time", "user_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NOTICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_ID_FIELD_NUMBER: _ClassVar[int]
    POST_TYPE_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    notice_type: str
    operator_id: int
    post_type: str
    self_id: int
    sub_type: str
    time: int
    user_id: int
    def __init__(self, time: _Optional[int] = ..., self_id: _Optional[int] = ..., post_type: _Optional[str] = ..., notice_type: _Optional[str] = ..., sub_type: _Optional[str] = ..., user_id: _Optional[int] = ..., group_id: _Optional[int] = ..., operator_id: _Optional[int] = ...) -> None: ...

class GroupMessageEvent(_message.Message):
    __slots__ = ["anonymous", "font", "group_id", "message", "message_id", "message_type", "post_type", "raw_message", "reply", "self_id", "sender", "sub_type", "time", "to_me", "user_id"]
    ANONYMOUS_FIELD_NUMBER: _ClassVar[int]
    FONT_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    POST_TYPE_FIELD_NUMBER: _ClassVar[int]
    RAW_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    TO_ME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    anonymous: Anonymous
    font: int
    group_id: int
    message: _containers.RepeatedCompositeFieldContainer[ReceivableMessageSegment]
    message_id: str
    message_type: str
    post_type: str
    raw_message: str
    reply: Reply
    self_id: int
    sender: Sender
    sub_type: str
    time: int
    to_me: bool
    user_id: int
    def __init__(self, time: _Optional[int] = ..., self_id: _Optional[int] = ..., post_type: _Optional[str] = ..., message_type: _Optional[str] = ..., sub_type: _Optional[str] = ..., message_id: _Optional[str] = ..., group_id: _Optional[int] = ..., user_id: _Optional[int] = ..., anonymous: _Optional[_Union[Anonymous, _Mapping]] = ..., message: _Optional[_Iterable[_Union[ReceivableMessageSegment, _Mapping]]] = ..., raw_message: _Optional[str] = ..., font: _Optional[int] = ..., sender: _Optional[_Union[Sender, _Mapping]] = ..., to_me: bool = ..., reply: _Optional[_Union[Reply, _Mapping]] = ...) -> None: ...

class GroupMessageRequest(_message.Message):
    __slots__ = ["group_id", "message"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    message: _containers.RepeatedCompositeFieldContainer[SendibleMessageSegment]
    def __init__(self, group_id: _Optional[int] = ..., message: _Optional[_Iterable[_Union[SendibleMessageSegment, _Mapping]]] = ...) -> None: ...

class GroupMessageResponse(_message.Message):
    __slots__ = ["group_id", "message"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    message: _containers.RepeatedCompositeFieldContainer[SendibleMessageSegment]
    def __init__(self, group_id: _Optional[int] = ..., message: _Optional[_Iterable[_Union[SendibleMessageSegment, _Mapping]]] = ...) -> None: ...

class GroupMessageResult(_message.Message):
    __slots__ = ["message_id"]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    def __init__(self, message_id: _Optional[str] = ...) -> None: ...

class GroupRecallNoticeEvent(_message.Message):
    __slots__ = ["group_id", "message_id", "notice_type", "operator_id", "post_type", "self_id", "time", "user_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    NOTICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_ID_FIELD_NUMBER: _ClassVar[int]
    POST_TYPE_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    message_id: str
    notice_type: str
    operator_id: int
    post_type: str
    self_id: int
    time: int
    user_id: int
    def __init__(self, time: _Optional[int] = ..., self_id: _Optional[int] = ..., post_type: _Optional[str] = ..., notice_type: _Optional[str] = ..., user_id: _Optional[int] = ..., group_id: _Optional[int] = ..., operator_id: _Optional[int] = ..., message_id: _Optional[str] = ...) -> None: ...

class GroupRequestEvent(_message.Message):
    __slots__ = ["comment", "flag", "group_id", "post_type", "request_type", "self_id", "sub_type", "time", "user_id"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    POST_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TYPE_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    comment: str
    flag: str
    group_id: int
    post_type: str
    request_type: str
    self_id: int
    sub_type: str
    time: int
    user_id: int
    def __init__(self, time: _Optional[int] = ..., self_id: _Optional[int] = ..., post_type: _Optional[str] = ..., request_type: _Optional[str] = ..., sub_type: _Optional[str] = ..., group_id: _Optional[int] = ..., user_id: _Optional[int] = ..., comment: _Optional[str] = ..., flag: _Optional[str] = ...) -> None: ...

class Head(_message.Message):
    __slots__ = ["self_id"]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    self_id: int
    def __init__(self, self_id: _Optional[int] = ...) -> None: ...

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

class MusicSegment(_message.Message):
    __slots__ = ["id", "type"]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: str
    def __init__(self, type: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class OptionCode(_message.Message):
    __slots__ = ["code"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: int
    def __init__(self, code: _Optional[int] = ...) -> None: ...

class PokeNotifyEvent(_message.Message):
    __slots__ = ["group_id", "notice_type", "post_type", "self_id", "sub_type", "target_id", "time", "user_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NOTICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    POST_TYPE_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    notice_type: str
    post_type: str
    self_id: int
    sub_type: str
    target_id: int
    time: int
    user_id: int
    def __init__(self, time: _Optional[int] = ..., self_id: _Optional[int] = ..., post_type: _Optional[str] = ..., notice_type: _Optional[str] = ..., sub_type: _Optional[str] = ..., user_id: _Optional[int] = ..., target_id: _Optional[int] = ..., group_id: _Optional[int] = ...) -> None: ...

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
    __slots__ = ["font", "message", "message_id", "message_type", "post_type", "raw_message", "reply", "self_id", "sender", "sub_type", "time", "to_me", "user_id"]
    FONT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    POST_TYPE_FIELD_NUMBER: _ClassVar[int]
    RAW_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    TO_ME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    font: int
    message: _containers.RepeatedCompositeFieldContainer[ReceivableMessageSegment]
    message_id: str
    message_type: str
    post_type: str
    raw_message: str
    reply: Reply
    self_id: int
    sender: Sender
    sub_type: str
    time: int
    to_me: bool
    user_id: int
    def __init__(self, time: _Optional[int] = ..., self_id: _Optional[int] = ..., post_type: _Optional[str] = ..., message_type: _Optional[str] = ..., sub_type: _Optional[str] = ..., message_id: _Optional[str] = ..., user_id: _Optional[int] = ..., message: _Optional[_Iterable[_Union[ReceivableMessageSegment, _Mapping]]] = ..., raw_message: _Optional[str] = ..., font: _Optional[int] = ..., sender: _Optional[_Union[Sender, _Mapping]] = ..., to_me: bool = ..., reply: _Optional[_Union[Reply, _Mapping]] = ...) -> None: ...

class PrivateMessageRequest(_message.Message):
    __slots__ = ["message", "user_id"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    message: _containers.RepeatedCompositeFieldContainer[SendibleMessageSegment]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ..., message: _Optional[_Iterable[_Union[SendibleMessageSegment, _Mapping]]] = ...) -> None: ...

class PrivateMessageResponse(_message.Message):
    __slots__ = ["message", "user_id"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    message: _containers.RepeatedCompositeFieldContainer[SendibleMessageSegment]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ..., message: _Optional[_Iterable[_Union[SendibleMessageSegment, _Mapping]]] = ...) -> None: ...

class PrivateMessageResult(_message.Message):
    __slots__ = ["message_id"]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    def __init__(self, message_id: _Optional[str] = ...) -> None: ...

class ReceivableMessageSegment(_message.Message):
    __slots__ = ["AtSegment", "DiceSegment", "FaceSegment", "ImageSegment", "JsonSegment", "LocationSegment", "PokeSegment", "RecordSegment", "ReplySegment", "RpsSegment", "ShareSegment", "TextSegment", "VideoSegment", "XmlSegment"]
    ATSEGMENT_FIELD_NUMBER: _ClassVar[int]
    AtSegment: AtSegment
    DICESEGMENT_FIELD_NUMBER: _ClassVar[int]
    DiceSegment: DiceSegment
    FACESEGMENT_FIELD_NUMBER: _ClassVar[int]
    FaceSegment: FaceSegment
    IMAGESEGMENT_FIELD_NUMBER: _ClassVar[int]
    ImageSegment: ImageSegment
    JSONSEGMENT_FIELD_NUMBER: _ClassVar[int]
    JsonSegment: JsonSegment
    LOCATIONSEGMENT_FIELD_NUMBER: _ClassVar[int]
    LocationSegment: LocationSegment
    POKESEGMENT_FIELD_NUMBER: _ClassVar[int]
    PokeSegment: PokeSegment
    RECORDSEGMENT_FIELD_NUMBER: _ClassVar[int]
    REPLYSEGMENT_FIELD_NUMBER: _ClassVar[int]
    RPSSEGMENT_FIELD_NUMBER: _ClassVar[int]
    RecordSegment: RecordSegment
    ReplySegment: ReplySegment
    RpsSegment: RpsSegment
    SHARESEGMENT_FIELD_NUMBER: _ClassVar[int]
    ShareSegment: ShareSegment
    TEXTSEGMENT_FIELD_NUMBER: _ClassVar[int]
    TextSegment: TextSegment
    VIDEOSEGMENT_FIELD_NUMBER: _ClassVar[int]
    VideoSegment: VideoSegment
    XMLSEGMENT_FIELD_NUMBER: _ClassVar[int]
    XmlSegment: XmlSegment
    def __init__(self, TextSegment: _Optional[_Union[TextSegment, _Mapping]] = ..., AtSegment: _Optional[_Union[AtSegment, _Mapping]] = ..., FaceSegment: _Optional[_Union[FaceSegment, _Mapping]] = ..., RpsSegment: _Optional[_Union[RpsSegment, _Mapping]] = ..., DiceSegment: _Optional[_Union[DiceSegment, _Mapping]] = ..., ImageSegment: _Optional[_Union[ImageSegment, _Mapping]] = ..., RecordSegment: _Optional[_Union[RecordSegment, _Mapping]] = ..., VideoSegment: _Optional[_Union[VideoSegment, _Mapping]] = ..., LocationSegment: _Optional[_Union[LocationSegment, _Mapping]] = ..., ShareSegment: _Optional[_Union[ShareSegment, _Mapping]] = ..., JsonSegment: _Optional[_Union[JsonSegment, _Mapping]] = ..., XmlSegment: _Optional[_Union[XmlSegment, _Mapping]] = ..., PokeSegment: _Optional[_Union[PokeSegment, _Mapping]] = ..., ReplySegment: _Optional[_Union[ReplySegment, _Mapping]] = ...) -> None: ...

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
    __slots__ = ["DeleteMsgRequest", "GetGroupInfoRequest", "GetGroupMemberInfoRequest", "GetGroupMemberListRequest", "GetMsgRequest", "GetStrangerInfoRequest", "GroupMessageRequest", "PrivateMessageRequest", "SendGroupForwardMsgRequest", "SendPrivateForwardMsgRequest", "request_id", "self_id"]
    DELETEMSGREQUEST_FIELD_NUMBER: _ClassVar[int]
    DeleteMsgRequest: DeleteMsgRequest
    GETGROUPINFOREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETGROUPMEMBERINFOREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETGROUPMEMBERLISTREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETMSGREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETSTRANGERINFOREQUEST_FIELD_NUMBER: _ClassVar[int]
    GROUPMESSAGEREQUEST_FIELD_NUMBER: _ClassVar[int]
    GetGroupInfoRequest: GetGroupInfoRequest
    GetGroupMemberInfoRequest: GetGroupMemberInfoRequest
    GetGroupMemberListRequest: GetGroupMemberListRequest
    GetMsgRequest: GetMsgRequest
    GetStrangerInfoRequest: GetStrangerInfoRequest
    GroupMessageRequest: GroupMessageRequest
    PRIVATEMESSAGEREQUEST_FIELD_NUMBER: _ClassVar[int]
    PrivateMessageRequest: PrivateMessageRequest
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    SENDGROUPFORWARDMSGREQUEST_FIELD_NUMBER: _ClassVar[int]
    SENDPRIVATEFORWARDMSGREQUEST_FIELD_NUMBER: _ClassVar[int]
    SendGroupForwardMsgRequest: SendGroupForwardMsgRequest
    SendPrivateForwardMsgRequest: SendPrivateForwardMsgRequest
    request_id: str
    self_id: int
    def __init__(self, request_id: _Optional[str] = ..., self_id: _Optional[int] = ..., PrivateMessageRequest: _Optional[_Union[PrivateMessageRequest, _Mapping]] = ..., GroupMessageRequest: _Optional[_Union[GroupMessageRequest, _Mapping]] = ..., DeleteMsgRequest: _Optional[_Union[DeleteMsgRequest, _Mapping]] = ..., GetMsgRequest: _Optional[_Union[GetMsgRequest, _Mapping]] = ..., GetStrangerInfoRequest: _Optional[_Union[GetStrangerInfoRequest, _Mapping]] = ..., GetGroupInfoRequest: _Optional[_Union[GetGroupInfoRequest, _Mapping]] = ..., GetGroupMemberInfoRequest: _Optional[_Union[GetGroupMemberInfoRequest, _Mapping]] = ..., GetGroupMemberListRequest: _Optional[_Union[GetGroupMemberListRequest, _Mapping]] = ..., SendPrivateForwardMsgRequest: _Optional[_Union[SendPrivateForwardMsgRequest, _Mapping]] = ..., SendGroupForwardMsgRequest: _Optional[_Union[SendGroupForwardMsgRequest, _Mapping]] = ...) -> None: ...

class Result(_message.Message):
    __slots__ = ["DeleteMsgResult", "GetGroupInfoResult", "GetGroupMemberInfoResult", "GetGroupMemberListResult", "GetMsgResult", "GetStrangerInfoResult", "GroupMessageResult", "PrivateMessageResult", "SendGroupForwardMsgResult", "SendPrivateForwardMsgResult", "request_id", "self_id"]
    DELETEMSGRESULT_FIELD_NUMBER: _ClassVar[int]
    DeleteMsgResult: DeleteMsgResult
    GETGROUPINFORESULT_FIELD_NUMBER: _ClassVar[int]
    GETGROUPMEMBERINFORESULT_FIELD_NUMBER: _ClassVar[int]
    GETGROUPMEMBERLISTRESULT_FIELD_NUMBER: _ClassVar[int]
    GETMSGRESULT_FIELD_NUMBER: _ClassVar[int]
    GETSTRANGERINFORESULT_FIELD_NUMBER: _ClassVar[int]
    GROUPMESSAGERESULT_FIELD_NUMBER: _ClassVar[int]
    GetGroupInfoResult: GetGroupInfoResult
    GetGroupMemberInfoResult: GetGroupMemberInfoResult
    GetGroupMemberListResult: GetGroupMemberListResult
    GetMsgResult: GetMsgResult
    GetStrangerInfoResult: GetStrangerInfoResult
    GroupMessageResult: GroupMessageResult
    PRIVATEMESSAGERESULT_FIELD_NUMBER: _ClassVar[int]
    PrivateMessageResult: PrivateMessageResult
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SELF_ID_FIELD_NUMBER: _ClassVar[int]
    SENDGROUPFORWARDMSGRESULT_FIELD_NUMBER: _ClassVar[int]
    SENDPRIVATEFORWARDMSGRESULT_FIELD_NUMBER: _ClassVar[int]
    SendGroupForwardMsgResult: SendGroupForwardMsgResult
    SendPrivateForwardMsgResult: SendPrivateForwardMsgResult
    request_id: str
    self_id: int
    def __init__(self, request_id: _Optional[str] = ..., self_id: _Optional[int] = ..., PrivateMessageResult: _Optional[_Union[PrivateMessageResult, _Mapping]] = ..., GroupMessageResult: _Optional[_Union[GroupMessageResult, _Mapping]] = ..., DeleteMsgResult: _Optional[_Union[DeleteMsgResult, _Mapping]] = ..., GetMsgResult: _Optional[_Union[GetMsgResult, _Mapping]] = ..., GetStrangerInfoResult: _Optional[_Union[GetStrangerInfoResult, _Mapping]] = ..., GetGroupInfoResult: _Optional[_Union[GetGroupInfoResult, _Mapping]] = ..., GetGroupMemberInfoResult: _Optional[_Union[GetGroupMemberInfoResult, _Mapping]] = ..., GetGroupMemberListResult: _Optional[_Union[GetGroupMemberListResult, _Mapping]] = ..., SendPrivateForwardMsgResult: _Optional[_Union[SendPrivateForwardMsgResult, _Mapping]] = ..., SendGroupForwardMsgResult: _Optional[_Union[SendGroupForwardMsgResult, _Mapping]] = ...) -> None: ...

class RpsSegment(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SendGroupForwardMsgRequest(_message.Message):
    __slots__ = ["group_id", "message"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    message: _containers.RepeatedCompositeFieldContainer[_ForwardSegment]
    def __init__(self, group_id: _Optional[int] = ..., message: _Optional[_Iterable[_Union[_ForwardSegment, _Mapping]]] = ...) -> None: ...

class SendGroupForwardMsgResult(_message.Message):
    __slots__ = ["message_id"]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    def __init__(self, message_id: _Optional[str] = ...) -> None: ...

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

class SendPrivateForwardMsgRequest(_message.Message):
    __slots__ = ["message", "user_id"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    message: _containers.RepeatedCompositeFieldContainer[_ForwardSegment]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ..., message: _Optional[_Iterable[_Union[_ForwardSegment, _Mapping]]] = ...) -> None: ...

class SendPrivateForwardMsgResult(_message.Message):
    __slots__ = ["message_id"]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    def __init__(self, message_id: _Optional[str] = ...) -> None: ...

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
    __slots__ = ["AnonymousSegment", "AtSegment", "ContactSegment", "CustomMusicSegment", "DiceSegment", "FaceSegment", "ImageSegment", "JsonSegment", "LocationSegment", "MusicSegment", "PokeSegment", "RecordSegment", "ReplySegment", "RpsSegment", "ShareSegment", "TextSegment", "VideoSegment", "XmlSegment"]
    ANONYMOUSSEGMENT_FIELD_NUMBER: _ClassVar[int]
    ATSEGMENT_FIELD_NUMBER: _ClassVar[int]
    AnonymousSegment: AnonymousSegment
    AtSegment: AtSegment
    CONTACTSEGMENT_FIELD_NUMBER: _ClassVar[int]
    CUSTOMMUSICSEGMENT_FIELD_NUMBER: _ClassVar[int]
    ContactSegment: ContactSegment
    CustomMusicSegment: CustomMusicSegment
    DICESEGMENT_FIELD_NUMBER: _ClassVar[int]
    DiceSegment: DiceSegment
    FACESEGMENT_FIELD_NUMBER: _ClassVar[int]
    FaceSegment: FaceSegment
    IMAGESEGMENT_FIELD_NUMBER: _ClassVar[int]
    ImageSegment: ImageSegment
    JSONSEGMENT_FIELD_NUMBER: _ClassVar[int]
    JsonSegment: JsonSegment
    LOCATIONSEGMENT_FIELD_NUMBER: _ClassVar[int]
    LocationSegment: LocationSegment
    MUSICSEGMENT_FIELD_NUMBER: _ClassVar[int]
    MusicSegment: MusicSegment
    POKESEGMENT_FIELD_NUMBER: _ClassVar[int]
    PokeSegment: PokeSegment
    RECORDSEGMENT_FIELD_NUMBER: _ClassVar[int]
    REPLYSEGMENT_FIELD_NUMBER: _ClassVar[int]
    RPSSEGMENT_FIELD_NUMBER: _ClassVar[int]
    RecordSegment: RecordSegment
    ReplySegment: ReplySegment
    RpsSegment: RpsSegment
    SHARESEGMENT_FIELD_NUMBER: _ClassVar[int]
    ShareSegment: ShareSegment
    TEXTSEGMENT_FIELD_NUMBER: _ClassVar[int]
    TextSegment: TextSegment
    VIDEOSEGMENT_FIELD_NUMBER: _ClassVar[int]
    VideoSegment: VideoSegment
    XMLSEGMENT_FIELD_NUMBER: _ClassVar[int]
    XmlSegment: XmlSegment
    def __init__(self, TextSegment: _Optional[_Union[TextSegment, _Mapping]] = ..., FaceSegment: _Optional[_Union[FaceSegment, _Mapping]] = ..., ImageSegment: _Optional[_Union[ImageSegment, _Mapping]] = ..., RecordSegment: _Optional[_Union[RecordSegment, _Mapping]] = ..., VideoSegment: _Optional[_Union[VideoSegment, _Mapping]] = ..., AtSegment: _Optional[_Union[AtSegment, _Mapping]] = ..., RpsSegment: _Optional[_Union[RpsSegment, _Mapping]] = ..., DiceSegment: _Optional[_Union[DiceSegment, _Mapping]] = ..., PokeSegment: _Optional[_Union[PokeSegment, _Mapping]] = ..., AnonymousSegment: _Optional[_Union[AnonymousSegment, _Mapping]] = ..., ShareSegment: _Optional[_Union[ShareSegment, _Mapping]] = ..., ContactSegment: _Optional[_Union[ContactSegment, _Mapping]] = ..., LocationSegment: _Optional[_Union[LocationSegment, _Mapping]] = ..., MusicSegment: _Optional[_Union[MusicSegment, _Mapping]] = ..., CustomMusicSegment: _Optional[_Union[CustomMusicSegment, _Mapping]] = ..., ReplySegment: _Optional[_Union[ReplySegment, _Mapping]] = ..., XmlSegment: _Optional[_Union[XmlSegment, _Mapping]] = ..., JsonSegment: _Optional[_Union[JsonSegment, _Mapping]] = ...) -> None: ...

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

class _ForwardSegment(_message.Message):
    __slots__ = ["content", "name", "uin"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UIN_FIELD_NUMBER: _ClassVar[int]
    content: _containers.RepeatedCompositeFieldContainer[SendibleMessageSegment]
    name: str
    uin: str
    def __init__(self, name: _Optional[str] = ..., uin: _Optional[str] = ..., content: _Optional[_Iterable[_Union[SendibleMessageSegment, _Mapping]]] = ...) -> None: ...
