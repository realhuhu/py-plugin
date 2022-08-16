from nonebot import init

init()
import os
import asyncio
import importlib
from pathlib import Path

from core.server.server import startServer

root = Path(os.path.dirname(os.path.abspath(__file__)))

apps = map(
    lambda x: (x.package, x),
    filter(
        lambda x: hasattr(x, "package"),
        map(
            lambda x: importlib.import_module(f"apps.{x}.py"),
            filter(
                lambda x: x != "__pycache__" and (root / "apps" / x).is_dir() and (root / "apps" / x / "py").exists(),
                os.listdir(os.path.join(root, "apps"))
            )
        )
    )

)


async def main():
    server = await startServer(apps)
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except asyncio.exceptions.CancelledError or KeyboardInterrupt as e:
        raise e
