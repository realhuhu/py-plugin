import sys
import logging
import asyncio
from pathlib import Path
from typing import Optional, Union, Callable, Awaitable, Set, cast
from omegaconf import OmegaConf

from nonebot.log import logger
from nonebot.utils import run_sync, is_coroutine_callable
from nonebot.adapters.onebot.v11 import Bot
from nonebot.config import Config
from core.server.server import Server, create_server

HOOK_FUNC = Union[Callable[[], None], Callable[[], Awaitable[None]]]


class Driver:
    def __init__(self, config: Config):
        self.config: Config = config
        self.startup_funcs: Set[HOOK_FUNC] = set()
        self.shutdown_funcs: Set[HOOK_FUNC] = set()
        self.server: Server = create_server(config.host, config.port)
        self.should_exit: asyncio.Event = asyncio.Event()
        self.force_exit: bool = False

    @property
    def type(self) -> str:
        return "grpc"

    @property
    def logger(self):
        return logging.getLogger("grpc")

    def on_startup(self, func: HOOK_FUNC) -> HOOK_FUNC:
        self.startup_funcs.add(func)
        return func

    async def startup(self):
        cors = [
            cast(Callable[..., Awaitable[None]], startup)()
            if is_coroutine_callable(startup)
            else run_sync(startup)()
            for startup in self.startup_funcs
        ]
        if cors:
            try:
                await asyncio.gather(*cors)
            except Exception as e:
                logger.opt(colors=True, exception=e).error(
                    "<r><bg #f8bbd0>Error when running startup function. "
                    "Ignored!</bg #f8bbd0></r>"
                )

        logger.info("Py服务器已启动")

    def on_shutdown(self, func: HOOK_FUNC) -> HOOK_FUNC:
        self.shutdown_funcs.add(func)
        return func

    async def shutdown(self):
        logger.info("关机中")

        cors = [
            cast(Callable[..., Awaitable[None]], shutdown)()
            if is_coroutine_callable(shutdown)
            else run_sync(shutdown)()
            for shutdown in self.shutdown_funcs
        ]
        if cors:
            try:
                await asyncio.gather(*cors)
            except Exception as e:
                logger.opt(colors=True, exception=e).error(
                    "<r><bg #f8bbd0>Error when running shutdown function. "
                    "Ignored!</bg #f8bbd0></r>"
                )

        for task in asyncio.all_tasks():
            if task is not asyncio.current_task() and not task.done():
                task.cancel()
        await asyncio.sleep(0.1)

        tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
        if tasks and not self.force_exit:
            logger.info("Waiting for tasks to finish. (CTRL+C to force quit)")
        while tasks and not self.force_exit:
            await asyncio.sleep(0.1)
            tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]

        for task in tasks:
            task.cancel()

        await asyncio.gather(*tasks, return_exceptions=True)

        logger.info("已关机")
        loop = asyncio.get_event_loop()
        loop.stop()

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.serve())

    async def serve(self):
        await self.startup()
        await self.server.start()
        try:
            await self.server.wait_for_termination()
        except:
            pass
        await self.shutdown()


_driver: Optional[Driver] = None
_bot: Optional[Bot] = None


def get_driver() -> Driver:
    global _driver
    if _driver is None:
        raise ValueError("Driver has not been initialized.")
    return _driver


def get_bot() -> Bot:
    global _bot
    if _bot is None:
        raise ValueError("Bot has not been initialized.")
    return _bot


def init(config_path) -> None:
    global _driver, _bot
    config = Config(**OmegaConf.load(config_path))
    _bot = Bot(config)
    _driver = Driver(config=config)


def run(root: Path):
    global _driver

    plugins_path = root / "plugins"
    sys.path.append(str(plugins_path))

    for i in plugins_path.iterdir():
        sys.path.append(str(i))

    for plugin in _driver.config.plugins:
        load_plugin(plugin.replace("-", "_"))
    _driver.run()


from nonebot.plugin import on as on
from nonebot.plugin import on_type as on_type
from nonebot.plugin import require as require
from nonebot.plugin import on_regex as on_regex
from nonebot.plugin import on_notice as on_notice
from nonebot.plugin import get_plugin as get_plugin
from nonebot.plugin import on_command as on_command
from nonebot.plugin import on_keyword as on_keyword
from nonebot.plugin import on_message as on_message
from nonebot.plugin import on_request as on_request
from nonebot.plugin import load_plugin as load_plugin
from nonebot.plugin import on_endswith as on_endswith
from nonebot.plugin import CommandGroup as CommandGroup
from nonebot.plugin import MatcherGroup as MatcherGroup
from nonebot.plugin import load_plugins as load_plugins
from nonebot.plugin import on_fullmatch as on_fullmatch
from nonebot.plugin import on_metaevent as on_metaevent
from nonebot.plugin import on_startswith as on_startswith
from nonebot.plugin import load_from_json as load_from_json
from nonebot.plugin import load_from_toml as load_from_toml
from nonebot.plugin import load_all_plugins as load_all_plugins
from nonebot.plugin import get_loaded_plugins as get_loaded_plugins
from nonebot.plugin import load_builtin_plugin as load_builtin_plugin
from nonebot.plugin import load_builtin_plugins as load_builtin_plugins
from nonebot.plugin import get_plugin_by_module_name as get_plugin_by_module_name
from nonebot.plugin import get_available_plugin_names as get_available_plugin_names
