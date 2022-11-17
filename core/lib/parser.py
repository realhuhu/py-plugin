from typing import Iterator

import nonebot.adapters.onebot.v11.event as _event
import nonebot.adapters.onebot.v11.message as _message

from core import typing


async def message_parser(message: Iterator[typing.GRPCReceivableMessageSegment]):
    serialized_message = _message.Message()
    for message_segment in message:
        message_class = message_segment.WhichOneof("segment")
        if message_class == "TextSegment":
            serialized_message_segment = _message.MessageSegment(
                type="text",
                data={
                    "text": message_segment.TextSegment.data
                }
            )

        elif message_class == "AtSegment":
            serialized_message_segment = _message.MessageSegment(
                type="at",
                data={
                    "qq": message_segment.AtSegment.qq
                }
            )

        elif message_class == "FaceSegment":
            serialized_message_segment = _message.MessageSegment(
                type="face",
                data={
                    "id": message_segment.FaceSegment.id
                }
            )

        elif message_class == "RpsSegment":
            serialized_message_segment = _message.MessageSegment(
                type="rps",
                data={}
            )

        elif message_class == "DiceSegment":
            serialized_message_segment = _message.MessageSegment(
                type="dice",
                data={}
            )

        elif message_class == "ImageSegment":
            serialized_message_segment = _message.MessageSegment(
                type="image",
                data={
                    "file": message_segment.ImageSegment.file,
                    "type": message_segment.ImageSegment.type,
                    "url": message_segment.ImageSegment.url
                }
            )

        elif message_class == "RecordSegment":
            serialized_message_segment = _message.MessageSegment(
                type="record",
                data={
                    "file": message_segment.RecordSegment.file,
                    "url": message_segment.RecordSegment.url
                }
            )

        elif message_class == "VideoSegment":
            serialized_message_segment = _message.MessageSegment(
                type="video",
                data={
                    "file": message_segment.VideoSegment.file,
                    "url": message_segment.VideoSegment.url
                }
            )

        elif message_class == "LocationSegment":
            serialized_message_segment = _message.MessageSegment(
                type="location",
                data={
                    "lat": message_segment.LocationSegment.lat,
                    "lon": message_segment.LocationSegment.lon,
                    "title": message_segment.LocationSegment.title,
                    "content": message_segment.LocationSegment.content,
                }
            )

        elif message_class == "ShareSegment":
            serialized_message_segment = _message.MessageSegment(
                type="share",
                data={
                    "url": message_segment.ShareSegment.url,
                    "title": message_segment.ShareSegment.title,
                    "content": message_segment.ShareSegment.content,
                    "image": message_segment.ShareSegment.image,
                }
            )

        elif message_class == "JsonSegment":
            serialized_message_segment = _message.MessageSegment(
                type="json",
                data={
                    "data": message_segment.JsonSegment.data,
                }
            )

        elif message_class == "XmlSegment":
            serialized_message_segment = _message.MessageSegment(
                type="xml",
                data={
                    "data": message_segment.XmlSegment.data,
                }
            )

        elif message_class == "PokeSegment":
            serialized_message_segment = _message.MessageSegment(
                type="poke",
                data={
                    "type": message_segment.PokeSegment.type,
                    "id": message_segment.PokeSegment.id,
                }
            )

        elif message_class == "ReplySegment":
            serialized_message_segment = _message.MessageSegment(
                type="reply",
                data={
                    "id": message_segment.ReplySegment.id,
                }
            )
        else:
            continue

        serialized_message.append(serialized_message_segment)
    return serialized_message


async def sender_parser(sender: typing.GRPCSender):
    return _event.Sender(
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


async def reply_parser(reply: typing.GRPCReply):
    return _event.Reply(
        time=reply.time,
        message_type=reply.message_type,
        message_id=reply.message_id,
        real_id=reply.real_id,
        sender=await sender_parser(reply.sender),
        message=await message_parser(reply.message)
    )


async def anonymous_parser(anonymous: typing.GRPCAnonymous):
    return _event.Anonymous(
        id=anonymous.id,
        name=anonymous.name,
        flag=anonymous.flag,
    )
