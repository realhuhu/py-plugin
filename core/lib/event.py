from copy import deepcopy

import nonebot.adapters.onebot.v11.event as _event

from core.lib.parser import *


async def event_parser(event: typing.GRPCEvent):
    event_class = event.WhichOneof("event")
    if event_class == "PrivateMessageEvent":
        event = event.PrivateMessageEvent
        message = await message_parser(event.message)
        return _event.PrivateMessageEvent(
            time=event.time,
            self_id=event.self_id,
            post_type=event.post_type,
            sub_type=event.sub_type,
            user_id=event.user_id,
            message_type=event.message_type,
            message_id=event.message_id,
            message=message,
            original_message=deepcopy(message),
            raw_message=event.raw_message,
            font=0,
            sender=await sender_parser(event.sender),
            to_me=event.to_me,
            reply=None if not event.reply.time else await reply_parser(event.reply)
        )

    elif event_class == "GroupMessageEvent":
        event = event.GroupMessageEvent
        message = await message_parser(event.message)
        return _event.GroupMessageEvent(
            time=event.time,
            self_id=event.self_id,
            post_type=event.post_type,
            sub_type=event.sub_type,
            user_id=event.user_id,
            message_type=event.message_type,
            message_id=event.message_id,
            message=message,
            original_message=deepcopy(message),
            raw_message=event.raw_message,
            font=0,
            sender=await sender_parser(event.sender),
            to_me=event.to_me,
            reply=None if not event.reply.time else await reply_parser(event.reply),
            group_id=event.group_id,
            anonymous=None if not event.anonymous.id else await anonymous_parser(event.anonymous),
        )
    elif event_class == "FriendRecallNoticeEvent":
        event = event.FriendRecallNoticeEvent
        return _event.FriendRecallNoticeEvent(
            time=event.time,
            self_id=event.self_id,
            post_type=event.post_type,
            notice_type=event.notice_type,
            user_id=event.user_id,
            message_id=event.message_id,
        )
    elif event_class == "GroupRecallNoticeEvent":
        event = event.GroupRecallNoticeEvent
        return _event.GroupRecallNoticeEvent(
            time=event.time,
            self_id=event.self_id,
            post_type=event.post_type,
            notice_type=event.notice_type,
            user_id=event.user_id,
            group_id=event.group_id,
            operator_id=event.operator_id,
            message_id=event.message_id,
        )


__all__ = [
    "event_parser"
]
