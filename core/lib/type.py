from typing import Protocol, Dict, Type, AsyncGenerator, Any, List, Optional

from ..rpc.type_pb2 import Response as _Response


class User(Protocol):
    qq: str
    name: str


class Group(Protocol):
    qq: str
    name: str


class Event(Protocol):
    msg: str
    sender: User
    group: Group
    atList: List[User]
    imageList: List[bytes]


class Request(Protocol):
    event: Event

    message: str
    messageList: List[str]
    messageDict: Dict[str, str]

    image: bytes
    imageList: List[bytes]
    imageDict: Dict[str, bytes]


def Response(
        message: Optional[str] = None,
        messageList: Optional[List[str]] = None,
        messageDict: Optional[Dict[str, str]] = None,
        image: bytes = None,
        imageList: List[bytes] = None,
        imageDict: Dict[str, bytes] = None,
):
    return _Response(
        message=message,
        messageList=messageList,
        messageDict=messageDict,
        image=image,
        imageList=imageList,
        imageDict=imageDict
    )


RequestIterator = AsyncGenerator[Type[Request], Any]
ResponseIterator = AsyncGenerator[Type[Response], Any]
