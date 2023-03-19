from typing import List

from nonebot.adapters.onebot.v11 import Message, Bot
from yunzai_nonebot.rpc import hola_pb2, typing as GRPCTyping
from .utils import format_file


def convert(bot: Bot, message: Message) -> List[GRPCTyping.SendibleMessageSegment]:
    grpc_message = []
    for message_segment in message:
        if message_segment.type == "anonymous":
            data = hola_pb2.AnonymousSegment(
                ignore=message_segment.data.get("ignore")
            )
        elif message_segment.type == "at":
            data = hola_pb2.AtSegment(
                qq=message_segment.data.get("qq")
            )
        elif message_segment.type == "contact":
            data = hola_pb2.ContactSegment(
                type=message_segment.data.get("type"),
                id=message_segment.data.get("id")
            )
        elif message_segment.type == "dice":
            data = hola_pb2.DiceSegment()
        elif message_segment.type == "face":
            data = hola_pb2.FaceSegment(
                id=message_segment.data.get("id")
            )
        elif message_segment.type == "image":
            file = format_file(bot, message_segment.data.get("file"))
            data = hola_pb2.ImageSegment(
                file=file if isinstance(file, str) else None,
                type=message_segment.data.get("type"),
                content=file if isinstance(file, bytes) else None,
                timeout=message_segment.data.get("timeout"),
            )
        elif message_segment.type == "json":
            data = hola_pb2.JsonSegment(
                data=message_segment.data.get("data")
            )
        elif message_segment.type == "location":
            data = hola_pb2.LocationSegment(
                lat=message_segment.data.get("lat"),
                lon=message_segment.data.get("lon"),
                title=message_segment.data.get("title"),
                content=message_segment.data.get("content"),
            )
        elif message_segment.type == "music" and message_segment.data.get("type") == "custom":
            data = hola_pb2.CustomMusicSegment(
                type="custom",
                url=message_segment.data.get("url"),
                audio=message_segment.data.get("audio"),
                title=message_segment.data.get("title"),
                content=message_segment.data.get("content"),
                image=message_segment.data.get("image"),
            )
        elif message_segment.type == "music":
            data = hola_pb2.MusicSegment(
                type=message_segment.data.get("type"),
                id=message_segment.data.get("id"),
            )
        elif message_segment.type == "poke":
            data = hola_pb2.PokeSegment(
                type=message_segment.data.get("type"),
                id=message_segment.data.get("id")
            )
        elif message_segment.type == "record":
            file = format_file(bot, message_segment.data.get("file"))
            data = hola_pb2.RecordSegment(
                file=file if isinstance(file, str) else None,
                content=file if isinstance(file, bytes) else None,
                timeout=message_segment.data.get("timeout"),
            )
        elif message_segment.type == "reply":
            data = hola_pb2.ReplySegment(
                id=message_segment.data.get("id")
            )
        elif message_segment.type == "rps":
            data = hola_pb2.RpsSegment()
        elif message_segment.type == "share":
            data = hola_pb2.ShareSegment(
                url=message_segment.data.get("url"),
                title=message_segment.data.get("title"),
                content=message_segment.data.get("content"),
                image=message_segment.data.get("image"),
            )
        elif message_segment.type == "text":
            data = hola_pb2.TextSegment(
                data=message_segment.data.get("text")
            )
        elif message_segment.type == "video":
            file = format_file(bot, message_segment.data.get("file"))
            data = hola_pb2.VideoSegment(
                file=file if isinstance(file, str) else None,
                content=file if isinstance(file, bytes) else None,
                timeout=message_segment.data.get("timeout"),
            )
        elif message_segment.type == "xml":
            data = hola_pb2.XmlSegment(
                data=message_segment.data.get("data")
            )
        else:
            continue
        grpc_message.append(hola_pb2.SendibleMessageSegment(
            **{message_segment.type: data}
        ))
    return grpc_message


def make_forward(bot, nodes) -> List[GRPCTyping.ForwardSegment]:
    forward_list = []
    for node in nodes:
        data = node["data"]
        forward_list.append(hola_pb2.ForwardSegment(
            name=data["name"],
            uin=data["uin"],
            content=convert(bot, Message(data["content"]))
        ))
    return forward_list
