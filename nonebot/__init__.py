import sys
from pathlib import Path
from typing import Optional
from omegaconf import OmegaConf

from .log import logger
from .utils import run_sync, is_coroutine_callable
from .adapters.onebot.v11 import Bot, Dict
from .config import Config
from .drivers import GRPCDriver
from .internal.driver import Driver

_driver: Optional[GRPCDriver] = None


def get_driver() -> GRPCDriver:
    global _driver
    if _driver is None:
        raise ValueError("Driver has not been initialized.")
    return _driver


def get_bots() -> Dict[str, Bot]:
    return get_driver().bots


def get_bot(self_id: Optional[str] = None) -> Bot:
    driver = get_driver()
    if self_id is not None:
        if not driver.bots.get(self_id):
            driver.create_bot(self_id)
        return driver.bots[self_id]

    for bot in driver.bots.values():
        return bot

    raise ValueError("There are no bots to get.")


def init(config_path: Path) -> None:
    global _driver
    config = Config(**OmegaConf.load(config_path))
    config.plugins = config.plugins or []
    _driver = GRPCDriver(config=config)


def run(root: Path):
    global _driver

    plugins_path = root / "plugins"
    sys.path.append(str(plugins_path))

    for i in plugins_path.iterdir():
        sys.path.append(str(i))

    _driver.run([str(x) for x in _driver.config.plugins])


class Export:
    pass


_export = Export()


def export():
    global _export
    return _export


from nonebot.plugin import on as on
from nonebot.plugin import on_type as on_type
from nonebot.plugin import require as require
from nonebot.plugin import on_regex as on_regex
from nonebot.plugin import on_notice as on_notice
from nonebot.plugin import get_plugin as get_plugin
from nonebot.plugin import on_command as on_command
from nonebot.plugin import on_keyword as on_keyword
from nonebot.plugin import on_message as on_message
from nonebot.plugin import on_request as on_request
from nonebot.plugin import load_plugin as load_plugin
from nonebot.plugin import on_endswith as on_endswith
from nonebot.plugin import CommandGroup as CommandGroup
from nonebot.plugin import MatcherGroup as MatcherGroup
from nonebot.plugin import load_plugins as load_plugins
from nonebot.plugin import on_fullmatch as on_fullmatch
from nonebot.plugin import on_metaevent as on_metaevent
from nonebot.plugin import on_startswith as on_startswith
from nonebot.plugin import load_from_json as load_from_json
from nonebot.plugin import load_from_toml as load_from_toml
from nonebot.plugin import load_all_plugins as load_all_plugins
from nonebot.plugin import on_shell_command as on_shell_command
from nonebot.plugin import get_loaded_plugins as get_loaded_plugins
from nonebot.plugin import load_builtin_plugin as load_builtin_plugin
from nonebot.plugin import load_builtin_plugins as load_builtin_plugins
from nonebot.plugin import get_plugin_by_module_name as get_plugin_by_module_name
from nonebot.plugin import get_available_plugin_names as get_available_plugin_names
