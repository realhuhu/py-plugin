from typing import Iterator

from nonebot.adapters.onebot import v12
from yunzai_nonebot.rpc.hola_pb2 import ReceivableMessageSegment, Sender, Reply, Anonymous


def message_parser(message: Iterator[ReceivableMessageSegment]) -> v12.message.Message:
    serialized_message = v12.message.Message()
    for message_segment in message:
        message_type = message_segment.WhichOneof("segment")
        if message_type == "text":
            message_segment = message_segment.text
            serialized_message_segment = v12.message.MessageSegment(
                type="text",
                data={
                    "text": message_segment.data
                }
            )
        elif message_type == "at":
            message_segment = message_segment.at
            serialized_message_segment = v12.message.MessageSegment(
                type="mention",
                data={
                    "user_id": str(message_segment.qq)
                }
            )
        elif message_type == "image":
            message_segment = message_segment.image
            serialized_message_segment = v12.message.MessageSegment(
                type="image",
                data={
                    "file_id": message_segment.file,
                    "type": message_segment.type,
                    "url": message_segment.url,
                }
            )
        elif message_type == "record":
            message_segment = message_segment.record
            serialized_message_segment = v12.message.MessageSegment(
                type="audio",
                data={
                    "file_id": message_segment.file,
                    "url": message_segment.url
                }
            )
        elif message_type == "video":
            message_segment = message_segment.video
            serialized_message_segment = v12.message.MessageSegment(
                type="video",
                data={
                    "file_id": message_segment.file,
                    "url": message_segment.url
                }
            )
        elif message_type == "location":
            message_segment = message_segment.location
            serialized_message_segment = v12.message.MessageSegment(
                type="location",
                data={
                    "latitude": message_segment.lat,
                    "longitude": message_segment.lon,
                    "title": message_segment.title,
                    "content": message_segment.content,
                }
            )
        elif message_type == "reply":
            message_segment = message_segment.reply
            serialized_message_segment = v12.message.MessageSegment(
                type="reply",
                data={
                    "message_id": message_segment.id,
                }
            )
        else:
            continue
        serialized_message.append(serialized_message_segment)
    return serialized_message


def reply_parser(reply: Reply) -> v12.event.Reply:
    return v12.event.Reply(
        message_id=reply.message_id,
        user_id=str(reply.sender.user_id),
    )
