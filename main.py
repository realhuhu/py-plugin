import shutil
from pathlib import Path

import yunzai_nonebot

root = Path(__file__).absolute().parent
config_path = root / "config.yaml"

if not config_path.exists():
    shutil.copy(root / "config_default.yaml", config_path)

yunzai_nonebot.init(Path(__file__).absolute().parent / "config.yaml")
yunzai_nonebot.run()
