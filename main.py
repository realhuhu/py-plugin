import os
import asyncio
import importlib

import nonebot

nonebot.init()

from core.server.server import startServer
from core import logger

root = os.path.dirname(os.path.abspath(__file__))

apps = map(
    lambda x: (x.package, x),
    filter(
        lambda x: hasattr(x, "package"),
        map(
            lambda x: importlib.import_module(f"apps.py.{x.replace('.py', '')}"),
            os.listdir(os.path.join(root, "apps", "py"))
        )
    )

)


async def main():
    server = await startServer(os.path.join(root, "config.json"), apps)
    await server.start()
    logger.success("Python server start")
    await server.wait_for_termination()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except asyncio.exceptions.CancelledError:
        logger.success("Python server stop")
