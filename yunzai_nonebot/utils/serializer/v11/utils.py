import base64
from typing import Iterator

from nonebot.adapters.onebot import v11
from yunzai_nonebot.rpc.hola_pb2 import ReceivableMessageSegment, Sender, Reply, Anonymous


def message_id_to_int(message_id: str) -> int:
    return int.from_bytes(base64.b64decode(message_id), "big")


def message_parser(message: Iterator[ReceivableMessageSegment]) -> v11.message.Message:
    serialized_message = v11.message.Message()
    for message_segment in message:
        message_type = message_segment.WhichOneof("segment")
        if message_type == "text":
            message_segment = message_segment.text
            serialized_message_segment = v11.message.MessageSegment(
                type="text",
                data={
                    "text": message_segment.data
                }
            )
        elif message_type == "at":
            message_segment = message_segment.at
            serialized_message_segment = v11.message.MessageSegment(
                type="at",
                data={
                    "qq": message_segment.qq
                }
            )
        elif message_type == "face":
            message_segment = message_segment.face
            serialized_message_segment = v11.message.MessageSegment(
                type="face",
                data={
                    "id": message_segment.id
                }
            )
        elif message_type == "rps":
            serialized_message_segment = v11.message.MessageSegment(
                type="rps",
                data={}
            )
        elif message_type == "dice":
            serialized_message_segment = v11.message.MessageSegment(
                type="dice",
                data={}
            )
        elif message_type == "image":
            message_segment = message_segment.image
            serialized_message_segment = v11.message.MessageSegment(
                type="image",
                data={
                    "file": message_segment.file,
                    "type": message_segment.type,
                    "url": message_segment.url
                }
            )
        elif message_type == "record":
            message_segment = message_segment.record
            serialized_message_segment = v11.message.MessageSegment(
                type="record",
                data={
                    "file": message_segment.file,
                    "url": message_segment.url
                }
            )
        elif message_type == "video":
            message_segment = message_segment.video
            serialized_message_segment = v11.message.MessageSegment(
                type="video",
                data={
                    "file": message_segment.file,
                    "url": message_segment.url
                }
            )
        elif message_type == "location":
            message_segment = message_segment.location
            serialized_message_segment = v11.message.MessageSegment(
                type="location",
                data={
                    "lat": message_segment.lat,
                    "lon": message_segment.lon,
                    "title": message_segment.title,
                    "content": message_segment.content,
                }
            )
        elif message_type == "share":
            message_segment = message_segment.share
            serialized_message_segment = v11.message.MessageSegment(
                type="share",
                data={
                    "url": message_segment.url,
                    "title": message_segment.title,
                    "content": message_segment.content,
                    "image": message_segment.image,
                }
            )
        elif message_type == "json":
            message_segment = message_segment.json
            serialized_message_segment = v11.message.MessageSegment(
                type="json",
                data={
                    "data": message_segment.data,
                }
            )
        elif message_type == "xml":
            message_segment = message_segment.xml
            serialized_message_segment = v11.message.MessageSegment(
                type="xml",
                data={
                    "data": message_segment.data,
                }
            )
        elif message_type == "poke":
            message_segment = message_segment.poke
            serialized_message_segment = v11.message.MessageSegment(
                type="poke",
                data={
                    "type": message_segment.type,
                    "id": message_segment.id,
                }
            )
        elif message_type == "reply":
            message_segment = message_segment.reply
            serialized_message_segment = v11.message.MessageSegment(
                type="reply",
                data={
                    "id": message_segment.id,
                }
            )
        else:
            continue
        serialized_message.append(serialized_message_segment)
    return serialized_message


def sender_parser(sender: Sender) -> v11.event.Sender:
    return v11.event.Sender(
        user_id=sender.user_id,
        nickname=sender.nickname,
        sex=sender.sex,
        age=sender.age,
        card=sender.card,
        area=sender.area,
        level=sender.level,
        role=sender.role,
        title=sender.title,
    )


def reply_parser(reply: Reply) -> v11.event.Reply:
    return v11.event.Reply(
        time=reply.time,
        message_type=reply.message_type,
        message_id=message_id_to_int(reply.message_id),
        real_id=reply.real_id,
        sender=sender_parser(reply.sender),
        message=message_parser(reply.message)
    )


def anonymous_parser(anonymous: Anonymous) -> v11.event.Anonymous:
    return v11.event.Anonymous(
        id=anonymous.id,
        name=anonymous.name,
        flag=anonymous.flag,
    )
