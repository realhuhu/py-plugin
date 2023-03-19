import sys
from pathlib import Path

import nonebot
from nonebot import *

from .hijack import hijack_driver, hijack_logger, hijack_adapter, hijack_params, hijack_event, hijack_matcher


def init(config_path: Path):
    plugins_path = config_path.parent / "plugins"
    sys.path.append(str(plugins_path))
    for i in plugins_path.iterdir():
        sys.path.append(str(i))

    hijack_logger()
    hijack_params()
    hijack_event()
    driver = hijack_driver(config_path)
    logger.configure(
        extra={"log_level": driver.config.log_level, "independent": driver.config.dict().get("independent")}
    )
    adapter = hijack_adapter()
    driver.register_adapter(adapter)
    hijack_matcher()


def run(*args, **kwargs):
    nonebot.run(*args, **kwargs)
