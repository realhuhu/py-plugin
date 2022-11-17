import shutil
from pathlib import Path

import nonebot

root = Path(__file__).absolute().parent
config_path = root / "config.yaml"

if not config_path.exists():
    shutil.copy(root / "config_default.yaml", config_path)

nonebot.init(config_path)
nonebot.run(root)
