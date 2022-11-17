import abc
from typing import Any, Dict

from nonebot.config import Config

from .bot import Bot


class Adapter(abc.ABC):
    def __init__(self, config: Config, **kwargs: Any):
        self.config = config
        self.bots: Dict[str, Bot] = {}

    def __repr__(self) -> str:
        return f"Adapter(name={self.get_name()!r})"

    @classmethod
    @abc.abstractmethod
    def get_name(cls) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    async def _call_api(self, bot: Bot, api: str, **data: Any) -> Any:
        raise NotImplementedError
