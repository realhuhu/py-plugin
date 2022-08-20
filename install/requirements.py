import os
import json
import asyncio
from pathlib import Path

import httpx

__path__ = Path(os.path.dirname(os.path.abspath(__file__)))

requirements = []


async def get_requirement(title):
    async with httpx.AsyncClient() as client:
        res: httpx.Response = await client.get(
            f"https://api.miao.seutools.com/app?search={title}",
            follow_redirects=True
        )
        if res and res.json():
            if requirement := res.json()[0]["requirement"]:
                return requirement.split(".")

    return []


async def main():
    titles = []
    for app in (__path__.parent / "apps").iterdir():
        if (app / "info.json").exists():
            with open(str(app / "info.json"), "r", encoding="utf-8-sig") as f:
                if title := json.load(f).get("group"):
                    titles.append(title)

    data = []
    done, _ = await asyncio.wait(
        map(lambda x: asyncio.create_task(get_requirement(x), name=x), titles),
        timeout=10
    )

    for i in done:
        data += i.result()

    print(os.system(f"poetry run pip install {' '.join(set(data))}"))


if __name__ == '__main__':
    asyncio.run(main())
