from nonebot import init, logger

init()
import os
import warnings
import traceback
import asyncio
import importlib
from pathlib import Path

from core.server.server import startServer
import logging

logging.getLogger('apscheduler').setLevel(logging.WARN)
warnings.filterwarnings("ignore")

root = Path(os.path.dirname(os.path.abspath(__file__)))


def try_import(x):
    try:
        return importlib.import_module(f"apps.{x}.py")
    except Exception as e:
        logger.warning(f"Fail to load {x}:{e}")
        logger.warning(traceback.format_exc())
        return None


apps = map(
    lambda x: (x.package, x),
    filter(
        lambda x: hasattr(x, "package"),
        map(
            lambda x: try_import(x),
            filter(
                lambda x: x != "__pycache__" and (root / "apps" / x).is_dir() and (root / "apps" / x / "py").exists(),
                os.listdir(os.path.join(root, "apps"))
            )
        )
    )

)


async def main():
    server = await startServer(apps)
    logger.info("Python started")
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except asyncio.exceptions.CancelledError or KeyboardInterrupt as e:
        raise e
