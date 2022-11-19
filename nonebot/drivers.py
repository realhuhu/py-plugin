import signal
import asyncio
import threading
from typing import Set, Union, Callable, Awaitable, cast

from .log import logger
from .internal.driver import Driver
from .typing import overrides
from .config import  Config
from .utils import run_sync, is_coroutine_callable
from core.server.server import Server, create_server

HOOK_FUNC = Union[Callable[[], None], Callable[[], Awaitable[None]]]
HANDLED_SIGNALS = (
    signal.SIGINT,  # Unix signal 2. Sent by Ctrl+C.
    signal.SIGTERM,  # Unix signal 15. Sent by `kill <pid>`.
)


class GRPCDriver(Driver):
    def __init__(self, config: Config):
        super().__init__(config)
        self.startup_funcs: Set[HOOK_FUNC] = set()
        self.shutdown_funcs: Set[HOOK_FUNC] = set()
        self.should_exit: asyncio.Event = asyncio.Event()
        self.force_exit: bool = False
        self.server: Server = create_server(config.host, config.port)

    @property
    @overrides(Driver)
    def type(self) -> str:
        """驱动名称: `block_driver`"""
        return "grpc_driver"

    @property
    @overrides(Driver)
    def logger(self):
        """block driver 使用的 logger"""
        return logger

    @overrides(Driver)
    def on_startup(self, func: HOOK_FUNC) -> HOOK_FUNC:
        """
        注册一个启动时执行的函数
        """
        self.startup_funcs.add(func)
        return func

    @overrides(Driver)
    def on_shutdown(self, func: HOOK_FUNC) -> HOOK_FUNC:
        """
        注册一个停止时执行的函数
        """
        self.shutdown_funcs.add(func)
        return func

    @overrides(Driver)
    def run(self, *args, **kwargs):
        """启动 block driver"""
        super().run(*args, **kwargs)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.serve())

    async def serve(self):
        self.install_signal_handlers()
        await self.startup()
        await self.server.start()
        logger.info("Py started")
        try:
            await self.server.wait_for_termination()
        except:
            pass
        if self.should_exit.is_set():
            return
        await self.main_loop()
        await self.shutdown()

    async def startup(self):
        # run startup
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


    async def main_loop(self):
        await self.should_exit.wait()

    async def shutdown(self):
        logger.info("关机中")

        # run shutdown
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

    def install_signal_handlers(self) -> None:
        if threading.current_thread() is not threading.main_thread():
            # Signals can only be listened to from the main thread.
            return

        loop = asyncio.get_event_loop()

        try:
            for sig in HANDLED_SIGNALS:
                loop.add_signal_handler(sig, self.handle_exit, sig, None)
        except NotImplementedError:
            # Windows
            for sig in HANDLED_SIGNALS:
                signal.signal(sig, self.handle_exit)

    def handle_exit(self, sig, frame):
        if self.should_exit.is_set():
            self.force_exit = True
        else:
            self.should_exit.set()
