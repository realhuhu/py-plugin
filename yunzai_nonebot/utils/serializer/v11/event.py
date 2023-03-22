import re
from copy import deepcopy

from yunzai_nonebot.rpc import hola_pb2
from nonebot.adapters.onebot import v11
from .utils import (
    message_parser,
    sender_parser,
    reply_parser,
    anonymous_parser,
    message_id_to_int
)
from yunzai_nonebot.utils.exception import SerializeEventError


def _check_first_at(bot, event: v11.event.MessageEvent) -> None:
    if len(event.message) < 2:
        return

    if event.message[0].type == "at" and event.message[0].data.get("qq") == event.self_id:
        return

    if event.message[0].type == "at" and event.message[1].type == "text":
        event.message[0], event.message[1] = event.message[1], event.message[0]


def _check_reply(bot, event: v11.event.MessageEvent) -> None:
    reply = event.reply
    if not reply:
        return

    if event.message[0].type == "at" and str(reply.sender.user_id) == event.message[0].data.get("qq"):
        event.message.pop(0)


def _check_at_me(bot, event: v11.event.MessageEvent) -> None:
    if not bot.config.need_at:
        event.to_me = True
        return

    if not isinstance(event, v11.event.MessageEvent):
        return

    # ensure message not empty
    if not event.message:
        event.message.append(v11.message.MessageSegment.text(""))

    if event.message_type == "private":
        event.to_me = True
    else:

        def _is_at_me_seg(segment: v11.message.MessageSegment):
            return segment.type == "at" and str(segment.data.get("qq", "")) == str(
                event.self_id
            )

        # check the first segment
        if _is_at_me_seg(event.message[0]):
            event.to_me = True
            event.message.pop(0)
            if event.message and event.message[0].type == "text":
                event.message[0].data["text"] = event.message[0].data["text"].lstrip()
                if not event.message[0].data["text"]:
                    del event.message[0]
            if event.message and _is_at_me_seg(event.message[0]):
                event.message.pop(0)
                if event.message and event.message[0].type == "text":
                    event.message[0].data["text"] = (
                        event.message[0].data["text"].lstrip()
                    )
                    if not event.message[0].data["text"]:
                        del event.message[0]

        if not event.to_me:
            # check the last segment
            i = -1
            last_msg_seg = event.message[i]
            if (
                    last_msg_seg.type == "text"
                    and not last_msg_seg.data["text"].strip()
                    and len(event.message) >= 2
            ):
                i -= 1
                last_msg_seg = event.message[i]

            if _is_at_me_seg(last_msg_seg):
                event.to_me = True
                del event.message[i:]

        if not event.message:
            event.message.append(v11.message.MessageSegment.text(""))


def _check_nickname(bot, event: v11.event.MessageEvent) -> None:
    if len(event.message) == 0:
        return

    first_msg_seg = event.message[0]
    if first_msg_seg.type != "text":
        return

    nicknames = set(filter(lambda n: n, bot.config.nickname))
    if not nicknames:
        return

    nickname_regex = "|".join(nicknames)
    first_text = first_msg_seg.data["text"]
    if m := re.search(rf"^({nickname_regex})([\s,，]*|$)", first_text, re.IGNORECASE):
        event.to_me = True
        first_msg_seg.data["text"] = first_text[m.end():]


def check(bot, event: v11.event.MessageEvent) -> None:
    _check_reply(bot, event)
    _check_at_me(bot, event)
    _check_nickname(bot, event)
    _check_first_at(bot, event)


def event_to_v11(bot, event: hola_pb2.Event) -> v11.event.Event:
    event_type = event.WhichOneof("event")
    if event_type == "friend_request":
        event = event.friend_request
        return v11.FriendRequestEvent(
            time=event.time,
            self_id=event.self_id,
            post_type="request",
            request_type="friend",
            user_id=event.user_id,
            comment=event.comment,
            flag=event.flag
        )
    if event_type == "group_request":
        event = event.group_request
        return v11.GroupRequestEvent(
            time=event.time,
            self_id=event.self_id,
            post_type="request",
            request_type="group",
            sub_type=event.sub_type,
            group_id=event.group_id,
            user_id=event.user_id,
            comment=event.comment,
            flag=event.flag
        )
    if event_type == "private_message":
        event = event.private_message
        message = message_parser(event.message)
        event = v11.PrivateMessageEvent(
            time=event.time,
            self_id=event.self_id,
            post_type="message",
            sub_type=event.sub_type,
            user_id=event.user_id,
            message_type="private",
            message_id=message_id_to_int(event.message_id),
            message=message,
            original_message=deepcopy(message),
            raw_message=event.raw_message,
            font=0,
            sender=sender_parser(event.sender),
            to_me=event.to_me,
            reply=None if not event.reply.time else reply_parser(event.reply)
        )
        check(bot, event)
        return event
    if event_type == "group_message":
        event = event.group_message
        message = message_parser(event.message)
        event = v11.GroupMessageEvent(
            time=event.time,
            self_id=event.self_id,
            post_type="message",
            sub_type=event.sub_type,
            user_id=event.user_id,
            message_type="group",
            message_id=message_id_to_int(event.message_id),
            message=message,
            original_message=deepcopy(message),
            raw_message=event.raw_message,
            font=0,
            sender=sender_parser(event.sender),
            to_me=event.to_me,
            reply=None if not event.reply.time else reply_parser(event.reply),
            group_id=event.group_id,
            anonymous=None if not event.anonymous.id else anonymous_parser(event.anonymous),
        )
        check(bot, event)
        return event
    if event_type == "friend_add_notice":
        event = event.friend_add_notice
        return v11.FriendAddNoticeEvent(
            time=event.time,
            self_id=event.self_id,
            post_type="notice",
            notice_type="friend_add",
            user_id=event.user_id
        )
    if event_type == "friend_recall_notice":
        event = event.friend_recall_notice
        return v11.FriendRecallNoticeEvent(
            time=event.time,
            self_id=event.self_id,
            post_type="notice",
            notice_type="friend_recall",
            user_id=event.user_id,
            message_id=message_id_to_int(event.message_id),
        )
    if event_type == "group_increase_notice":
        event = event.group_increase_notice
        return v11.GroupIncreaseNoticeEvent(
            time=event.time,
            self_id=event.self_id,
            post_type="notice",
            notice_type="group_increase",
            sub_type=event.sub_type,
            user_id=event.user_id,
            group_id=event.group_id,
            operator_id=event.operator_id
        )
    if event_type == "group_decrease_notice":
        event = event.group_decrease_notice
        return v11.GroupDecreaseNoticeEvent(
            time=event.time,
            self_id=event.self_id,
            post_type="notice",
            notice_type="group_decrease",
            sub_type=event.sub_type,
            user_id=event.user_id,
            group_id=event.group_id,
            operator_id=event.operator_id
        )
    if event_type == "group_recall_notice":
        event = event.group_recall_notice
        return v11.GroupRecallNoticeEvent(
            time=event.time,
            self_id=event.self_id,
            post_type="notice",
            notice_type="group_recall",
            user_id=event.user_id,
            group_id=event.group_id,
            operator_id=event.operator_id,
            message_id=message_id_to_int(event.message_id),
        )
    if event_type == "group_ban_notice":
        event = event.group_ban_notice
        return v11.GroupBanNoticeEvent(
            time=event.time,
            self_id=event.self_id,
            post_type="notice",
            notice_type="group_ban",
            sub_type=event.sub_type,
            user_id=event.user_id,
            group_id=event.group_id,
            operator_id=event.operator_id,
            duration=event.duration
        )
    if event_type == "group_admin_notice":
        event = event.group_admin_notice
        return v11.GroupAdminNoticeEvent(
            time=event.time,
            self_id=event.self_id,
            post_type="notice",
            notice_type="group_admin",
            sub_type=event.sub_type,
            user_id=event.user_id,
            group_id=event.group_id,
        )
    if event_type == "poke_notify":
        event = event.poke_notify
        return v11.PokeNotifyEvent(
            time=event.time,
            self_id=event.self_id,
            post_type="notice",
            notice_type="notify",
            sub_type="poke",
            user_id=event.user_id,
            target_id=event.target_id,
            group_id=event.group_id,
        )

    raise SerializeEventError(event)
