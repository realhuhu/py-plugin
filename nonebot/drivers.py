import asyncio
from typing import Set, Union, Callable, Awaitable

from .log import logger
from .internal.driver import Driver
from .typing import overrides
from .config import Config
from .plugin import load_plugin
from core.server.server import Server, create_server

HOOK_FUNC = Union[Callable[[], None], Callable[[], Awaitable[None]]]


class GRPCDriver(Driver):
    def __init__(self, config: Config):
        super().__init__(config)
        self.startup_funcs: Set[HOOK_FUNC] = set()
        self.shutdown_funcs: Set[HOOK_FUNC] = set()
        self.server: Server = create_server(config.host, config.port)

    @property
    @overrides(Driver)
    def type(self) -> str:
        return "grpc_driver"

    @property
    @overrides(Driver)
    def logger(self):
        return logger

    @overrides(Driver)
    def on_startup(self, func: HOOK_FUNC) -> HOOK_FUNC:
        self.startup_funcs.add(func)
        return func

    @overrides(Driver)
    def on_shutdown(self, func: HOOK_FUNC) -> HOOK_FUNC:
        self.shutdown_funcs.add(func)
        return func

    @overrides(Driver)
    def run(self, plugins, *args, **kwargs):
        super().run(*args, **kwargs)
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(self.serve(plugins))
        except KeyboardInterrupt or asyncio.exceptions.CancelledError:
            logger.info("已强制退出Py服务器")

    async def serve(self, plugins):
        logger.info("Py服务器开机中")

        await self.server.start()

        for plugin in set(filter(lambda x: x, plugins)):
            load_plugin(plugin.replace("-", "_"))

        if self.config.startup_check is not False:
            await self.startup()

        await asyncio.sleep(2)
        logger.info("Py服务器已开机(Py started)")

        try:
            await self.server.wait_for_termination()
        except asyncio.exceptions.CancelledError:
            raise
        except:
            logger.info("Py服务器关机中")

        if self.config.shutdown_check is not False:
            await self.shutdown()

        logger.info("Py服务器已关机")

    async def startup(self):
        for handler in self.startup_funcs:
            if asyncio.iscoroutinefunction(handler):
                await handler()
            else:
                handler()

    async def shutdown(self):
        for handler in self.shutdown_funcs:
            if asyncio.iscoroutinefunction(handler):
                await handler()
            else:
                handler()
