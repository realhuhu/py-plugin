import os
import asyncio
import importlib
from pathlib import Path
import nonebot

nonebot.init()

from core.server.server import startServer
from core import logger

root = Path(os.path.dirname(os.path.abspath(__file__)))

apps = map(
    lambda x: (x.package, x),
    filter(
        lambda x: hasattr(x, "package"),
        map(
            lambda x: importlib.import_module(f"apps.py.{x.replace('.py', '')}"),
            filter(lambda x: "." not in x or x.endswith(".py"), os.listdir(os.path.join(root, "apps", "py")))
        )
    )

)


async def main():
    server = await startServer(apps)
    await server.start()
    logger.success("Python server start")
    await server.wait_for_termination()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except asyncio.exceptions.CancelledError or KeyboardInterrupt:
        logger.success("Python server stop")
