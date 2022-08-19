import os
import json
from pathlib import Path

import requests

__path__ = Path(os.path.dirname(os.path.abspath(__file__)))

requirements = []

for app in (__path__.parent / "apps").iterdir():
    if (app / "info.json").exists():
        with open(str(app / "info.json"), "r", encoding="utf-8-sig") as f:
            if title := json.load(f).get("group"):
                if res := requests.get(f"https://api.miao.seutools.com/app?search={title}").json():
                    print(res)
                    if requirement := res[0]["requirement"]:
                        requirements += requirement.split(".")

print(os.system(f"poetry run pip install {' '.join(set(requirements))}"))
