from uuid import uuid4
from datetime import datetime
from copy import deepcopy

from yunzai_nonebot.rpc import hola_pb2
from nonebot.adapters.onebot import v12
from .utils import (
    message_parser,
    reply_parser,
)
from yunzai_nonebot.utils.exception import SerializeEventError


def event_to_v12(event: hola_pb2.Event) -> v12.event.Event:
    self = v12.event.BotSelf(platform="yunzai", user_id=event.self_id)
    event_type = event.WhichOneof("event")
    if event_type == "private_message":
        event = event.private_message
        message = message_parser(event.message)
        return v12.event.PrivateMessageEvent(
            id=str(uuid4()),
            time=datetime.utcfromtimestamp(event.time),
            type="message",
            detail_type="private",
            sub_type=event.sub_type,
            self=self,
            message_id=event.message_id,
            message=message,
            original_message=deepcopy(message),
            alt_message=event.raw_message,
            user_id=event.user_id,
            to_me=True,
            reply=None if not event.reply.time else reply_parser(event.reply)
        )
    if event_type == "group_message":
        event = event.group_message
        message = message_parser(event.message)
        return v12.event.PrivateMessageEvent(
            id=str(uuid4()),
            time=datetime.utcfromtimestamp(event.time),
            type="message",
            detail_type="private",
            sub_type=event.sub_type,
            self=self,
            message_id=event.message_id,
            message=message,
            original_message=deepcopy(message),
            alt_message=event.raw_message,
            user_id=event.user_id,
            to_me=event.to_me,
            reply=None if not event.reply.time else reply_parser(event.reply),
            group_id=event.group_id,
        )
    if event_type == "friend_add_notice":
        event = event.friend_add_notice
        return v12.FriendIncreaseEvent(
            id=str(uuid4()),
            time=datetime.utcfromtimestamp(event.time),
            type="notice",
            detail_type="friend_increase",
            sub_type="",
            self=self,
            user_id=str(event.user_id)
        )
    if event_type == "friend_recall_notice":
        event = event.friend_recall_notice
        return v12.PrivateMessageDeleteEvent(
            id=str(uuid4()),
            time=datetime.utcfromtimestamp(event.time),
            type="notice",
            detail_type="private_message_delete",
            sub_type="",
            self=self,
            message_id=event.message_id,
            user_id=str(event.user_id)
        )
    if event_type == "group_increase_notice":
        event = event.group_increase_notice
        return v12.GroupMemberIncreaseEvent(
            id=str(uuid4()),
            time=datetime.utcfromtimestamp(event.time),
            type="notice",
            detail_type="group_member_increase",
            sub_type=event.sub_type,
            self=self,
            user_id=str(event.user_id),
            group_id=str(event.group_id),
            operator_id=str(event.operator_id)
        )
    if event_type == "group_decrease_notice":
        event = event.group_decrease_notice
        return v12.GroupMemberDecreaseEvent(
            id=str(uuid4()),
            time=datetime.utcfromtimestamp(event.time),
            type="notice",
            detail_type="group_member_decrease",
            sub_type=event.sub_type,
            self=self,
            user_id=str(event.user_id),
            group_id=str(event.group_id),
            operator_id=str(event.operator_id)
        )
    if event_type == "group_recall_notice":
        event = event.group_recall_notice
        return v12.GroupMessageDeleteEvent(
            id=str(uuid4()),
            time=datetime.utcfromtimestamp(event.time),
            type="notice",
            detail_type="group_message_delete",
            sub_type="",
            self=self,
            user_id=str(event.user_id),
            group_id=str(event.group_id),
            operator_id=str(event.operator_id),
            message_id=str(event.message_id),
        )

    raise SerializeEventError(event)
