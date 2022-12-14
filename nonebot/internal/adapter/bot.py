import abc
import asyncio
from functools import partial
from typing import TYPE_CHECKING, Any, Set, Union, Optional, Protocol, cast

from nonebot.log import logger
from nonebot.exception import MockApiException
from nonebot.typing import T_CalledAPIHook, T_CallingAPIHook

if TYPE_CHECKING:
    from .event import Event
    from .message import Message, MessageSegment


    class _ApiCall(Protocol):
        async def __call__(self, **kwargs: Any) -> Any:
            ...


class Bot(abc.ABC):
    _calling_api_hook: Set[T_CallingAPIHook] = set()
    _called_api_hook: Set[T_CalledAPIHook] = set()

    def __init__(self, config):
        self.config = config
        self.self_id = ""

    def __repr__(self) -> str:
        return f"Bot(type={self.type!r})"

    def __getattr__(self, name: str) -> "_ApiCall":
        return partial(self.call_api, name)

    @property
    def type(self) -> str:
        return "PyBot"

    async def call_api(self, api: str, **data: Any) -> Any:
        result: Any = None
        skip_calling_api: bool = False
        exception: Optional[Exception] = None

        if coros := [hook(self, api, data) for hook in self._calling_api_hook]:
            try:
                logger.debug("Running CallingAPI hooks...")
                await asyncio.gather(*coros)
            except MockApiException as e:
                skip_calling_api = True
                result = e.result
                logger.debug(
                    f"Calling API {api} is cancelled. Return {result} instead."
                )
            except Exception as e:
                logger.opt(colors=True, exception=e).error(
                    "<r><bg #f8bbd0>Error when running CallingAPI hook. "
                    "Running cancelled!</bg #f8bbd0></r>"
                )

        if not skip_calling_api:
            try:
                result = await getattr(self, api)(**data)
            except Exception as e:
                if isinstance(e, RecursionError):
                    logger.warning(f"接口未实现:{api}")

                exception = e

        if coros := [
            hook(self, exception, api, data, result) for hook in self._called_api_hook
        ]:
            try:
                logger.debug("Running CalledAPI hooks...")
                await asyncio.gather(*coros)
            except MockApiException as e:
                result = e.result
                logger.debug(
                    f"Calling API {api} result is mocked. Return {result} instead."
                )
            except Exception as e:
                logger.opt(colors=True, exception=e).error(
                    "<r><bg #f8bbd0>Error when running CalledAPI hook. "
                    "Running cancelled!</bg #f8bbd0></r>"
                )

        if exception:
            raise exception
        return result

    @abc.abstractmethod
    async def send(
            self,
            event: "Event",
            message: Union[str, "Message", "MessageSegment"],
            **kwargs: Any,
    ) -> Any:
        raise NotImplementedError

    @classmethod
    def on_calling_api(cls, func: T_CallingAPIHook) -> T_CallingAPIHook:
        cls._calling_api_hook.add(func)
        return func

    @classmethod
    def on_called_api(cls, func: T_CalledAPIHook) -> T_CalledAPIHook:
        cls._called_api_hook.add(func)
        return func
