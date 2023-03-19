from typing import Union, Any, TYPE_CHECKING

from nonebot.message import handle_event
from nonebot.adapters.onebot import v11, v12
from nonebot.internal.adapter import Bot, Event, Message, MessageSegment

from yunzai_nonebot.rpc import hola_pb2
from yunzai_nonebot.utils import event_to_v11, event_to_v12
from .event import OneEvent

if TYPE_CHECKING:
    from .adapter import OneAdapter


class OneBot(Bot):
    def __init__(self, adapter: "OneAdapter", self_id: str):
        super().__init__(adapter, self_id)
        self.v11 = v11.bot.Bot(adapter, self_id)
        self.v12 = v12.bot.Bot(adapter, self_id, "yunzai", "yunzai")

    async def send(self, event: OneEvent, message: Union[str, Message, MessageSegment], **kwargs: Any) -> Any:
        return await self.adapter._call_api(
            self.v11,
            "send_msg",
            detail_type=event.v11.message_type,
            user_id=event.v11.dict().get("user_id"),
            group_id=event.v11.dict().get("group_id"),
            message=message
        )

    async def handle_event(self, event: hola_pb2.Event) -> None:
        await handle_event(
            self,
            OneEvent(
                v11=event_to_v11(self.v11, event),
                v12=event_to_v12(event),
                plugins=event.plugins
            )
        )
