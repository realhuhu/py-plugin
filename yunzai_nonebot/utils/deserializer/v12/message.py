from typing import List

from nonebot.adapters.onebot.v12 import Message, Bot
from yunzai_nonebot.rpc import hola_pb2, typing as GRPCTyping
from .utils import format_file


def convert(bot: Bot, message: Message) -> List[GRPCTyping.SendibleMessageSegment]:
    grpc_message = []
    message_type = None
    for message_segment in message:
        if message_segment.type == "text":
            data = hola_pb2.TextSegment(
                data=message_segment.data.get("text")
            )
        elif message_segment.type == "mention":
            message_type = "at"
            data = hola_pb2.AtSegment(
                qq=message_segment.data.get("qq")
            )
        elif message_segment.type == "mention_all":
            message_type = "at"
            data = hola_pb2.AtSegment(
                qq="all"
            )
        elif message_segment.type == "image":
            file = format_file(bot, message_segment.data.get("file_id"))
            data = hola_pb2.ImageSegment(
                file=file if isinstance(file, str) else None,
                type=message_segment.data.get("type"),
                content=file if isinstance(file, bytes) else None,
                timeout=message_segment.data.get("timeout"),
            )
        elif message_segment.type == "audio":
            message_type = "record"
            file = format_file(bot, message_segment.data.get("file_id"))
            data = hola_pb2.RecordSegment(
                file=file if isinstance(file, str) else None,
                content=file if isinstance(file, bytes) else None,
                timeout=message_segment.data.get("timeout"),
            )
        elif message_segment.type == "video":
            file = format_file(bot, message_segment.data.get("file_id"))
            data = hola_pb2.VideoSegment(
                file=file if isinstance(file, str) else None,
                content=file if isinstance(file, bytes) else None,
                timeout=message_segment.data.get("timeout"),
            )
        elif message_segment.type == "location":
            data = hola_pb2.LocationSegment(
                lat=message_segment.data.get("latitude"),
                lon=message_segment.data.get("longitude"),
                title=message_segment.data.get("title"),
                content=message_segment.data.get("content"),
            )
        elif message_segment.type == "reply":
            data = hola_pb2.ReplySegment(
                id=message_segment.data.get("message_id")
            )
        else:
            continue

        grpc_message.append(hola_pb2.SendibleMessageSegment(
            **{message_type or message_segment.type: data}
        ))
        return grpc_message
