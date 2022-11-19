# DONE TODO
import re
from typing import Any, Union, Type, Dict, List

from nonebot.typing import overrides
from nonebot.message import handle_event
from nonebot.log import logger
from nonebot.adapters import Bot as BaseBot

from .message import Message, MessageSegment
from .event import (
    Reply,
    Event,
    MessageEvent,
    PrivateMessageEvent,
    GroupMessageEvent,
)

from core.lib.parser import sender_parser, message_parser
from core.queue import Queue
from core.typing import (
    GRPCPrivateMessageResult,
    GRPCGroupMessageResult,
    GRPCDeleteMsgResult,
    GRPCGetMsgResult,
    GRPCSendPrivateForwardMsgResult,
    GRPCSendGroupForwardMsgResult,
)


def _check_first_at(bot: "Bot", event: MessageEvent) -> None:
    if len(event.message) < 2:
        return

    if event.message[0].type == "at" and event.message[0].data.get("qq") == event.self_id:
        return

    if event.message[0].type == "at" and event.message[1].type == "text":
        event.message[0], event.message[1] = event.message[1], event.message[0]


def _check_reply(bot: "Bot", event: MessageEvent) -> None:
    reply = event.reply
    if not reply:
        return

    if event.message[0].type == "at" and str(reply.sender.user_id) == event.message[0].data.get("qq"):
        event.message.pop(0)


def _check_at_me(bot: "Bot", event: MessageEvent) -> None:
    if not bot.config.need_at:
        event.to_me = True
        return

    if not isinstance(event, MessageEvent):
        return

    # ensure message not empty
    if not event.message:
        event.message.append(MessageSegment.text(""))

    if event.message_type == "private":
        event.to_me = True
    else:

        def _is_at_me_seg(segment: MessageSegment):
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
            event.message.append(MessageSegment.text(""))


def _check_nickname(bot: "Bot", event: MessageEvent) -> None:
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


class Bot(BaseBot):
    def __init__(self, config):
        super().__init__(config)
        self.request_queue = Queue("request")
        self.result_queue = Queue("result")

    async def handle_event(self, event: Event) -> None:
        if not event:
            return
        if isinstance(event, MessageEvent):
            _check_reply(self, event)
            _check_at_me(self, event)
            _check_nickname(self, event)
            _check_first_at(self, event)

        await handle_event(self, event)

    @staticmethod
    async def convert(message: Message) -> List[Dict[str, Any]]:
        serialized_message = []
        for message_segment in message:
            if message_segment.type == "anonymous":
                data = {
                    "Anonymous": {
                        "ignore": message_segment.data.get("ignore")
                    }
                }
            elif message_segment.type == "at":
                data = {
                    "AtSegment": {
                        "qq": message_segment.data.get("qq")
                    }
                }
            elif message_segment.type == "contact":
                data = {
                    "AtSegment": {
                        "type": message_segment.data.get("type"),
                        "id": message_segment.data.get("id"),
                    }
                }
            elif message_segment.type == "dice":
                data = {
                    "DiceSegment": {}
                }
            elif message_segment.type == "face":
                data = {
                    "FaceSegment": {
                        "id": message_segment.data.get("id")
                    }
                }
            elif message_segment.type == "image":
                file = message_segment.data.get("file")
                data = {
                    "ImageSegment": {
                        "file": file if isinstance(file, str) else None,
                        "type": message_segment.data.get("type"),
                        "content": file if isinstance(file, bytes) else None,
                        "timeout": message_segment.data.get("timeout"),
                    }
                }
            elif message_segment.type == "json":
                data = {
                    "JsonSegment": {
                        "data": message_segment.data.get("data"),
                    }
                }
            elif message_segment.type == "location":
                data = {
                    "LocationSegment": {
                        "lat": message_segment.data.get("lat"),
                        "lon": message_segment.data.get("lon"),
                        "title": message_segment.data.get("title"),
                        "content": message_segment.data.get("content"),
                    }
                }
            elif message_segment.type == "music":
                data = {
                    "MusicSegment": {
                        "type": message_segment.data.get("type"),
                        "id": message_segment.data.get("id"),
                        "url": message_segment.data.get("url"),
                        "audio": message_segment.data.get("audio"),
                        "title": message_segment.data.get("title"),
                        "image": message_segment.data.get("image"),
                    }
                }
            elif message_segment.type == "poke":
                data = {
                    "PokeSegment": {
                        "type": message_segment.data.get("type"),
                        "id": message_segment.data.get("id")
                    }
                }
            elif message_segment.type == "record":
                data = {
                    "RecordSegment": {
                        "content": message_segment.data.get("file"),
                        "timeout": message_segment.data.get("timeout"),
                    }
                }
            elif message_segment.type == "reply":
                data = {
                    "RpsSegment": {}
                }
            elif message_segment.type == "rps":
                data = {
                    "ReplySegment": {
                        "id": message_segment.data.get("id"),
                    }
                }
            elif message_segment.type == "share":
                data = {
                    "ShareSegment": {
                        "url": message_segment.data.get("url"),
                        "title": message_segment.data.get("title"),
                        "content": message_segment.data.get("content"),
                        "image": message_segment.data.get("image"),
                    }
                }
            elif message_segment.type == "text":
                data = {
                    "TextSegment": {
                        "data": message_segment.data.get("text")
                    }
                }
            elif message_segment.type == "video":
                data = {
                    "ImageSegment": {
                        "content": message_segment.data.get("file"),
                        "timeout": message_segment.data.get("timeout"),
                    }
                }
            elif message_segment.type == "xml":
                data = {
                    "XmlSegment": {
                        "data": message_segment.data.get("data"),
                    }
                }
            else:
                continue
            serialized_message.append(data)
        return serialized_message

    @overrides(BaseBot)
    async def send(
            self,
            event: Event,
            message: Union[str, Message, MessageSegment],
            **kwargs: Any,
    ) -> str:
        if isinstance(event, PrivateMessageEvent):
            await self.request_queue.put({
                "PrivateMessageRequest": {
                    "user_id": event.sender.user_id,
                    "message": await self.convert(Message(message))
                }
            })
            logger.success(f'[回复私聊][用户{event.user_id}] "{message}"')
            result: GRPCPrivateMessageResult = (await self.result_queue.__anext__()).PrivateMessageResult
            return result.message_id

        elif isinstance(event, GroupMessageEvent):
            await self.request_queue.put({
                "GroupMessageRequest": {
                    "group_id": event.group_id,
                    "message": await self.convert(Message(message))
                }
            })
            logger.success(f'[回复群聊][群聊{event.group_id}] "{message}"')
            result: GRPCGroupMessageResult = (await self.result_queue.__anext__()).GroupMessageResult
            return result.message_id

    async def delete_msg(self, message_id: str) -> None:
        type, id, real_message_id = message_id.split("|")
        await self.request_queue.put({
            "DeleteMsgRequest": {
                "message_id": message_id,
            }
        })
        logger.success(f'[撤回消息({type}:{id})] "{real_message_id}"')
        result: GRPCDeleteMsgResult = (await self.result_queue.__anext__()).DeleteMsgResult
        return None

    async def get_msg(self, message_id: int):
        await self.request_queue.put({
            "GetMsgRequest": {
                "message_id": message_id,
            }
        })
        logger.success(f'[获取消息] "{message_id}"')
        result: GRPCGetMsgResult = await self.result_queue.__anext__()
        return {
            "message_id": result.message_id,
            "real_id": result.real_id,
            "sender": await sender_parser(result.sender),
            "time": result.time,
            "message": await message_parser(result.message)
        }

    async def get_forward_msg(self, id: int):
        ...

    async def send_like(self, user_id: int, times: int = 1):
        await self.request_queue.put({
            "SendLikeRequest": {
                "user_id": user_id,
                "times": times,
            }
        })
        logger.success(f'[点赞] "给{user_id}点赞{times}次"')
        result = await self.result_queue.__anext__()
        return None

    async def set_group_kick(self, group_id: int, user_id: int, reject_add_request: bool = False):
        ...

    async def set_group_ban(self, group_id: int, user_id: int, duration: int = 30 * 60):
        ...

    async def set_group_anonymous_ban(
            self,
            group_id: int,
            anonymous: Any,
            flag: str,
            anonymous_flag: str,
            duration: int = 30 * 60
    ):
        ...

    async def set_group_whole_ban(self, group_id: int, enable: bool = True):
        ...

    async def set_group_admin(self, group_id: int, enable: bool = True):
        ...

    async def set_group_anonymous(self, group_id: int, enable: bool = True):
        ...

    async def set_group_card(self, group_id: int, user_id: int, card: str):
        ...

    async def set_group_name(self, group_id: int, group_name: str):
        ...

    async def set_group_leave(self, group_id: int, is_dismiss: bool = False):
        ...

    async def set_group_special_title(
            self,
            group_id: int,
            user_id: int,
            special_title: str = "",
            duration: int = -1
    ):
        ...

    async def set_friend_add_request(self, flag: str, approve: bool = True, remark: str = ""):
        ...

    async def set_group_add_request(self, flag: str, sub_type: str, approve: bool = True, reason: str = ""):
        ...

    async def get_login_info(self):
        ...

    async def get_stranger_info(self, user_id: int, no_cache: bool = False):
        ...

    async def get_friend_list(self):
        ...

    async def get_group_info(self, group_id: int, no_cache: bool = False):
        ...

    async def get_group_list(self, group_id: int, no_cache: bool = False):
        ...

    async def get_group_member_info(self, group_id: int, user_id: int, no_cache: bool = False):
        ...

    async def get_group_member_list(self, group_id: int):
        ...

    async def get_group_honor_info(self, group_id: int, type: str):
        ...

    async def send_group_forward_msg(self, group_id: int, messages):
        message = []
        for i in messages:
            message.append({
                "name": i["data"]["name"],
                "uin": i["data"]["uin"],
                "content": await self.convert(Message(i["data"]["content"])),
            })
        await self.request_queue.put({
            "SendGroupForwardMsgRequest": {
                "group_id": group_id,
                "message": message
            }
        })
        logger.success(f'[发送合并消息][群聊{group_id}] "[合并消息 length={len(messages)}]"')
        result: GRPCSendGroupForwardMsgResult = (await self.result_queue.__anext__()).SendGroupForwardMsgResult
        return result.message_id

    async def send_private_forward_msg(self, user_id: int, messages):
        message = []
        for i in messages:
            message.append({
                "name": i["data"]["name"],
                "uin": i["data"]["uin"],
                "content": await self.convert(Message(i["data"]["content"])),
            })
        await self.request_queue.put({
            "SendPrivateForwardMsgRequest": {
                "user_id": user_id,
                "message": message
            }
        })
        logger.success(f'[发送合并消息][用户{user_id}] "[合并消息 length={len(messages)}]"')
        result: GRPCSendPrivateForwardMsgResult = (await self.result_queue.__anext__()).SendPrivateForwardMsgResult
        return result.message_id