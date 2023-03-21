import importlib
from typing import Any

from pydantic import BaseModel
from nonebot import plugin, logger
from nonebot.utils import path_to_module_name, escape_tag


class Plugin(BaseModel):
    module: Any


def load_plugin(self, name):
    try:
        if name in self.plugins:
            module = importlib.import_module(name)
        elif name in self._third_party_plugin_names:
            module = importlib.import_module(self._third_party_plugin_names[name])
        elif name in self._searched_plugin_names:
            module = importlib.import_module(
                path_to_module_name(self._searched_plugin_names[name])
            )
        else:
            raise RuntimeError(f"没有找到插件: {name}! 请确认是否已安装")

        logger.opt(colors=True).success(
            f'插件导入成功"<y>{escape_tag(name)}</y>"'
        )
        if (plugin := getattr(module, "__plugin__", None)) is None:
            logger.warning(f"修复导入:{name}")
            return Plugin(module=__import__(name))
        return plugin
    except Exception as e:
        logger.opt(colors=True, exception=e).error(
            f'<r><bg #f8bbd0>插件导入失败 "{escape_tag(name)}"</bg #f8bbd0></r>'
        )


def hijack_plugin():
    plugin.PluginManager.load_plugin = load_plugin
