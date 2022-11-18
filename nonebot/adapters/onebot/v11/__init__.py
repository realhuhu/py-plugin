# DONE
from .event import *
from .permission import *
from .bot import Bot as Bot
from .utils import log as log
from .utils import escape as escape
from .message import Message as Message
from .utils import unescape as unescape
from .exception import ActionFailed as ActionFailed
from .exception import NetworkError as NetworkError
from .message import MessageSegment as MessageSegment
from .exception import ApiNotAvailable as ApiNotAvailable
from .exception import OneBotV11AdapterException as OneBotV11AdapterException


class Adapter:
    def __init__(self, config, **kwargs: Any):
        self.config = config
        self.bots: Dict[str, Bot] = {}

    def __repr__(self) -> str:
        return f"Fake Adapter"

    @classmethod
    def get_name(cls) -> str:
        return f"Fake Adapter"

    async def _call_api(self, bot: Bot, api: str, **data: Any) -> Any:
        raise NotImplementedError
