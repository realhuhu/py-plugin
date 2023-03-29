import asyncio
import traceback
from pathlib import Path
from typing import Type, Callable, Union, Awaitable, Set, Optional, AsyncGenerator, Any, TYPE_CHECKING

import nonebot
from nonebot.log import logger
from nonebot.config import Env, Config
from nonebot.internal.driver import Driver
from omegaconf import OmegaConf

from yunzai_nonebot.utils import Servicer, AsyncMap
from yunzai_nonebot.rpc import hola_pb2
from yunzai_nonebot.hijack.bot import OneBot

if TYPE_CHECKING:
    from yunzai_nonebot.hijack.adapter import OneAdapter

HOOK_FUNC = Union[Callable[[], None], Callable[[], Awaitable[None]]]


class GRPCDriver(Driver):

    def __init__(self, config: Config):
        super().__init__(Env(), config)
        self.startup_funcs: Set[HOOK_FUNC] = set()
        self.shutdown_funcs: Set[HOOK_FUNC] = set()
        self.servicer = Servicer(self.handler, config)
        self.adapter: Optional["OneAdapter"] = None

    @property
    def type(self) -> str:
        return "grpc_driver"

    @property
    def logger(self):
        return logger

    def run(self, *args, **kwargs):
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(self.serve())
        except KeyboardInterrupt:
            logger.info("已强制退出Py服务器")
            loop.run_until_complete(self.servicer.server.stop(0))

    def on_startup(self, func: HOOK_FUNC) -> HOOK_FUNC:
        self.startup_funcs.add(func)
        return func

    def on_shutdown(self, func: HOOK_FUNC) -> HOOK_FUNC:
        self.shutdown_funcs.add(func)
        return func

    async def serve(self):
        logger.info("开机中..")
        await self.servicer.server.start()

        if self.config.dict().get("setup_check") is not False:
            logger.info("检查与更新插件资源...")
            await self.startup()

        await asyncio.sleep(2)
        logger.info("Py服务器已开机(Py started)")
        try:
            await self.servicer.server.wait_for_termination()
        except asyncio.exceptions.CancelledError:
            if self.config.dict().get("shutdown_check") is not False:
                logger.info("关机检查...")
                await self.shutdown()
            logger.info("已关机")

    async def startup(self):
        for handler in self.startup_funcs:
            try:
                if asyncio.iscoroutinefunction(handler):
                    await handler()
                else:
                    handler()
            except:
                logger.warning(traceback.format_exc())

    async def shutdown(self):
        for handler in self.shutdown_funcs:
            try:
                if asyncio.iscoroutinefunction(handler):
                    await handler()
                else:
                    handler()
            except:
                logger.warning(traceback.format_exc())

    def register_adapter(self, adapter: Type["OneAdapter"], **kwargs) -> None:
        self.adapter = adapter(self, **kwargs)

    async def handler(self, self_id: str, request_iterator: AsyncGenerator[hola_pb2.ToServer, Any]):
        if bot := self.adapter.bots.get(self_id):
            self.adapter.bot_disconnect(bot)

        self.adapter.bot_connect(OneBot(self.adapter, self_id))
        result_store = AsyncMap(self_id)
        try:
            async for grpc_request in request_iterator:
                try:
                    grpc_request_type = grpc_request.WhichOneof("to_server_type")
                    if grpc_request_type == "event":
                        logger.debug(f"收到消息:{grpc_request}")
                        asyncio.create_task(self.adapter.bots[self_id].handle_event(grpc_request.event))
                    elif grpc_request_type == "result":
                        logger.debug(f"收到请求结果:{grpc_request}")
                        asyncio.create_task(result_store.set(grpc_request.result.request_id, grpc_request.result))
                except Exception:
                    logger.error(traceback.format_exc())
        except StopAsyncIteration:
            logger.warning("中断request连接")


def hijack_driver(config_path: Path):
    fields = Config.__fields__
    yaml = {}
    for k, v in OmegaConf.to_object(OmegaConf.load(config_path)).items():
        if field := fields.get(k):
            yaml[k.lower()] = field.default.__class__(v)
        else:
            yaml[k.lower()] = v
    yaml["plugins"] = yaml.get("plugins") or []
    logger.info(yaml)
    config = Config.parse_obj(yaml)
    driver = GRPCDriver(config)
    nonebot._driver = driver
    return driver
