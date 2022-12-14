# DONE
import re
from io import BytesIO
from pathlib import Path
from base64 import b64encode, b64decode
from typing import Type, Tuple, Union, Iterable, Optional

from nonebot.typing import overrides

from nonebot.adapters import Message as BaseMessage
from nonebot.adapters import MessageSegment as BaseMessageSegment

from .utils import log, unescape


class MessageSegment(BaseMessageSegment["Message"]):
    @classmethod
    @overrides(BaseMessageSegment)
    def get_message_class(cls) -> Type["Message"]:
        return Message

    @overrides(BaseMessageSegment)
    def __str__(self) -> str:
        type_ = self.type
        data = self.data.copy()

        if type_ == "text":
            return data.get("text", "")
        if type_ == "at":
            return f"[@{data.get('qq')}]"
        if type_ == "face":
            return f"[表情 id={data.get('id')}]"
        if type_ == "rps":
            return "[猜拳]"
        if type_ == "dice":
            return "[骰子]"
        if type_ == "image":
            file = data.get('file')
            return f"[图片({file if isinstance(file, str) else '二进制'})]"
        if type_ == "record":
            file = data.get('file')
            return f"[音频({file if isinstance(file, str) else '二进制'})]"
        if type_ == "video":
            file = data.get('file')
            return f"[视频({file if isinstance(file, str) else '二进制'})]"
        if type_ == "location":
            return f"[位置({data.get('title')}) lat-{data.get('lat')} lon-{data.get('lon')}]"
        if type_ == "share":
            return f"[分享({data.get('title')}) {data.get('url')}]"
        if type_ == "json":
            return "[JSON消息]"
        if type_ == "xml":
            return "[XML消息]"
        if type_ == "anonymous":
            return "[匿名]"
        if type_ == "contact":
            return f"[推荐{'联系人' if data.get('type') == 'qq' else '群聊'} id={data.get('id')}]"
        if type_ == "music":
            return f"[音乐分享 type={data.get('type_')}]"
        if type_ == "poke":
            return f"[戳一戳 type={data.get('type_')} id={data.get('id_')}]"
        if type_ == "reply":
            return f"[回复 id={data.get('id_')}]"

        return f"[{type_}消息]"

    @overrides(BaseMessageSegment)
    def __add__(
            self, other: Union[str, "MessageSegment", Iterable["MessageSegment"]]
    ) -> "Message":
        return Message(self) + (
            MessageSegment.text(other) if isinstance(other, str) else other
        )

    @overrides(BaseMessageSegment)
    def __radd__(
            self, other: Union[str, "MessageSegment", Iterable["MessageSegment"]]
    ) -> "Message":
        return (
                   MessageSegment.text(other) if isinstance(other, str) else Message(other)
               ) + self

    @overrides(BaseMessageSegment)
    def is_text(self) -> bool:
        return self.type == "text"

    @staticmethod
    def anonymous(ignore_failure: Optional[bool] = False) -> "MessageSegment":
        return MessageSegment("anonymous", {"ignore": ignore_failure})

    @staticmethod
    def at(user_id: Union[int, str]) -> "MessageSegment":
        return MessageSegment("at", {"qq": str(user_id)})

    @staticmethod
    def contact(type_: str, id: int) -> "MessageSegment":
        return MessageSegment("contact", {"type": type_, "id": str(id)})

    @staticmethod
    def contact_group(group_id: int) -> "MessageSegment":
        return MessageSegment("contact", {"type": "group", "id": str(group_id)})

    @staticmethod
    def contact_user(user_id: int) -> "MessageSegment":
        return MessageSegment("contact", {"type": "qq", "id": str(user_id)})

    @staticmethod
    def dice() -> "MessageSegment":
        return MessageSegment("dice", {})

    @staticmethod
    def face(id_: int) -> "MessageSegment":
        return MessageSegment("face", {"id": str(id_)})

    @staticmethod
    def forward(id_: str) -> "MessageSegment":
        log("WARNING", "Forward Message only can be received!")
        return MessageSegment("forward", {"id": id_})

    @staticmethod
    def image(
            file: Union[str, bytes, BytesIO, Path],
            type_: Optional[str] = None,
            cache: bool = True,
            proxy: bool = True,
            timeout: Optional[int] = None,
    ) -> "MessageSegment":
        if isinstance(file, BytesIO):
            file = file.getvalue()
        elif isinstance(file, Path):
            file = file.resolve().as_uri()
        elif isinstance(file, str):
            file = BytesIO(b64decode(file.replace("base64://", ""))).getvalue() if file.startswith("base64") else file
        return MessageSegment(
            "image",
            {
                "file": file,
                "type": type_,
                "cache": cache,
                "proxy": proxy,
                "timeout": timeout,
            },
        )

    @staticmethod
    def json(data: str) -> "MessageSegment":
        return MessageSegment("json", {"data": data})

    @staticmethod
    def location(
            latitude: float,
            longitude: float,
            title: Optional[str] = None,
            content: Optional[str] = None,
    ) -> "MessageSegment":
        return MessageSegment(
            "location",
            {
                "lat": str(latitude),
                "lon": str(longitude),
                "title": title,
                "content": content,
            },
        )

    @staticmethod
    def music(type_: str, id_: int) -> "MessageSegment":
        return MessageSegment("music", {"type": type_, "id": id_})

    @staticmethod
    def music_custom(
            url: str,
            audio: str,
            title: str,
            content: Optional[str] = None,
            img_url: Optional[str] = None,
    ) -> "MessageSegment":
        return MessageSegment(
            "music",
            {
                "type": "custom",
                "url": url,
                "audio": audio,
                "title": title,
                "content": content,
                "image": img_url,
            },
        )

    @staticmethod
    def node(id_: int) -> "MessageSegment":
        return MessageSegment("node", {"id": str(id_)})

    @staticmethod
    def node_custom(
            user_id: int, nickname: str, content: Union[str, "Message"]
    ) -> "MessageSegment":
        return MessageSegment(
            "node", {"user_id": str(user_id), "nickname": nickname, "content": content}
        )

    @staticmethod
    def poke(type_: str, id_: str) -> "MessageSegment":
        return MessageSegment("poke", {"type": type_, "id": id_})

    @staticmethod
    def record(
            file: Union[str, bytes, BytesIO, Path],
            magic: Optional[bool] = None,
            cache: Optional[bool] = None,
            proxy: Optional[bool] = None,
            timeout: Optional[int] = None,
    ) -> "MessageSegment":
        if isinstance(file, BytesIO):
            file = file.getvalue()
        elif isinstance(file, Path):
            file = file.resolve().as_uri()
        elif isinstance(file, str):
            file = BytesIO(b64decode(file.replace("base64://", ""))).getvalue() if file.startswith("base64") else file
        return MessageSegment(
            "record",
            {
                "file": file,
                "magic": magic,
                "cache": cache,
                "proxy": proxy,
                "timeout": timeout,
            },
        )

    @staticmethod
    def reply(id_: int) -> "MessageSegment":
        return MessageSegment("reply", {"id": str(id_)})

    @staticmethod
    def rps() -> "MessageSegment":
        return MessageSegment("rps", {})

    @staticmethod
    def shake() -> "MessageSegment":
        return MessageSegment("shake", {})

    @staticmethod
    def share(
            url: str = "",
            title: str = "",
            content: Optional[str] = None,
            image: Optional[str] = None,
    ) -> "MessageSegment":
        return MessageSegment(
            "share", {"url": url, "title": title, "content": content, "image": image}
        )

    @staticmethod
    def text(text: str) -> "MessageSegment":
        return MessageSegment("text", {"text": text})

    @staticmethod
    def video(
            file: Union[str, bytes, BytesIO, Path],
            cache: Optional[bool] = None,
            proxy: Optional[bool] = None,
            timeout: Optional[int] = None,
    ) -> "MessageSegment":
        if isinstance(file, BytesIO):
            file = file.getvalue()
        elif isinstance(file, Path):
            file = file.resolve().as_uri()
        elif isinstance(file, str):
            file = BytesIO(b64decode(file.replace("base64://", ""))).getvalue() if file.startswith("base64") else file
        return MessageSegment(
            "video",
            {
                "file": file,
                "cache": cache,
                "proxy": proxy,
                "timeout": timeout,
            },
        )

    @staticmethod
    def xml(data: str) -> "MessageSegment":
        return MessageSegment("xml", {"data": data})


class Message(BaseMessage[MessageSegment]):
    @classmethod
    @overrides(BaseMessage)
    def get_segment_class(cls) -> Type[MessageSegment]:
        return MessageSegment

    @overrides(BaseMessage)
    def __add__(
            self, other: Union[str, MessageSegment, Iterable[MessageSegment]]
    ) -> "Message":
        return super(Message, self).__add__(
            MessageSegment.text(other) if isinstance(other, str) else other
        )

    @overrides(BaseMessage)
    def __radd__(
            self, other: Union[str, MessageSegment, Iterable[MessageSegment]]
    ) -> "Message":
        return super(Message, self).__radd__(
            MessageSegment.text(other) if isinstance(other, str) else other
        )

    @overrides(BaseMessage)
    def __iadd__(
            self, other: Union[str, MessageSegment, Iterable[MessageSegment]]
    ) -> "Message":
        return super().__iadd__(
            MessageSegment.text(other) if isinstance(other, str) else other
        )

    @staticmethod
    @overrides(BaseMessage)
    def _construct(msg: str) -> Iterable[MessageSegment]:
        def _iter_message(msg: str) -> Iterable[Tuple[str, str]]:
            text_begin = 0
            py_map = {"图片": "image", "视频": "video", "音频": "record"}
            for cqcode in re.finditer(
                    r"\[CQ:(?P<type>[a-zA-Z0-9-_.]+)"
                    r"(?P<params>"
                    r"(?:,[a-zA-Z0-9-_.]+=[^,\]]*)*"
                    r"),?\]",
                    msg,
            ):
                yield "text", msg[text_begin: cqcode.pos + cqcode.start()]
                text_begin = cqcode.pos + cqcode.end()
                yield cqcode.group("type"), cqcode.group("params").lstrip(",")
            for pycode in re.finditer(
                    r"\[(?P<type>(图片|视频|音频))\((?P<file>.*)\)\]",
                    msg
            ):
                yield py_map[pycode.group("type")], f'file={pycode.group("file")}'
                text_begin = pycode.pos + pycode.end()
            yield "text", msg[text_begin:]

        for type_, data in _iter_message(msg):
            if type_ == "text":
                if data:
                    yield MessageSegment(type_, {"text": unescape(data)})
            else:
                data = {
                    k: unescape(v)
                    for k, v in map(
                        lambda x: x.split("=", maxsplit=1),
                        filter(lambda x: x, (x.lstrip() for x in data.split(","))),
                    )
                }
                yield MessageSegment(type_, data)

    @overrides(BaseMessage)
    def extract_plain_text(self) -> str:
        return "".join(seg.data["text"] for seg in self if seg.is_text())

    def reduce(self) -> None:
        index = 1
        while index < len(self):
            if self[index - 1].type == "text" and self[index].type == "text":
                self[index - 1].data["text"] += self[index].data["text"]
                del self[index]
            else:
                index += 1
