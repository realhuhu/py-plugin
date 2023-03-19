from typing import Any, get_args

from nonebot import logger
from nonebot.internal import params
from nonebot.exception import SkippedException
from nonebot.adapters.onebot import v11, v12

from .bot import OneBot
from .event import OneEvent


async def bot_solve(self, bot: OneBot, **kwargs: Any) -> Any:
    checker = self.extra.get("checker")
    if not checker or get_args(checker.type_) or checker.type_ == v11.bot.Bot:
        return bot.v11

    return bot.v12


async def bot_check(self, bot: OneBot, **kwargs: Any) -> None:
    if checker := self.extra.get("checker"):
        types = get_args(checker.type_) or (checker.type_,)
        if not any(map(lambda x: issubclass(x, v11.bot.Bot) or issubclass(x, v12.bot.Bot), types)):
            logger.error("py-plugin只支持OneBot V11和OneBot V12的插件")
            raise SkippedException


async def event_solve(self, event: OneEvent, **kwargs: Any) -> Any:
    checker = self.extra.get("checker")
    if not checker or get_args(checker.type_) or issubclass(checker.type_, v11.event.Event):
        return event.v11

    return event.v12


async def event_check(self, bot: OneBot, **kwargs: Any) -> None:
    if checker := self.extra.get("checker"):
        types = get_args(checker.type_) or (checker.type_,)
        if not any(map(lambda x: issubclass(x, v11.event.Event) or issubclass(x, v12.event.Event), types)):
            logger.error("py-plugin只支持OneBot V11和OneBot V12的插件")
            raise SkippedException


def hijack_params():
    params.BotParam._solve = bot_solve
    params.BotParam._check = bot_check
    params.EventParam._solve = event_solve
    params.EventParam._check = event_check
