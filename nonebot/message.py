# DONE
import asyncio
import contextlib
from datetime import datetime
from contextlib import AsyncExitStack
from typing import TYPE_CHECKING, Any, Set, Dict, Type, Optional

from .log import logger
from .rule import TrieRule
from .dependencies import Dependent
from .matcher import Matcher, matchers
from .utils import escape_tag, run_coro_with_catch
from .exception import (
    NoLogException,
    StopPropagation,
    IgnoredException,
    SkippedException,
)
from .typing import (
    T_State,
    T_DependencyCache,
    T_RunPreProcessor,
    T_RunPostProcessor,
    T_EventPreProcessor,
    T_EventPostProcessor,
)
from .internal.params import (
    ArgParam,
    BotParam,
    EventParam,
    StateParam,
    DependParam,
    DefaultParam,
    MatcherParam,
    ExceptionParam,
)

if TYPE_CHECKING:
    from .adapters import Bot, Event

_event_preprocessors: Set[Dependent[Any]] = set()
_event_postprocessors: Set[Dependent[Any]] = set()
_run_preprocessors: Set[Dependent[Any]] = set()
_run_postprocessors: Set[Dependent[Any]] = set()

EVENT_PCS_PARAMS = (
    DependParam,
    BotParam,
    EventParam,
    StateParam,
    DefaultParam,
)
RUN_PREPCS_PARAMS = (
    DependParam,
    BotParam,
    EventParam,
    StateParam,
    ArgParam,
    MatcherParam,
    DefaultParam,
)
RUN_POSTPCS_PARAMS = (
    DependParam,
    ExceptionParam,
    BotParam,
    EventParam,
    StateParam,
    ArgParam,
    MatcherParam,
    DefaultParam,
)


def event_preprocessor(func: T_EventPreProcessor) -> T_EventPreProcessor:
    _event_preprocessors.add(
        Dependent[Any].parse(call=func, allow_types=EVENT_PCS_PARAMS)
    )
    return func


def event_postprocessor(func: T_EventPostProcessor) -> T_EventPostProcessor:
    _event_postprocessors.add(
        Dependent[Any].parse(call=func, allow_types=EVENT_PCS_PARAMS)
    )
    return func


def run_preprocessor(func: T_RunPreProcessor) -> T_RunPreProcessor:
    _run_preprocessors.add(
        Dependent[Any].parse(call=func, allow_types=RUN_PREPCS_PARAMS)
    )
    return func


def run_postprocessor(func: T_RunPostProcessor) -> T_RunPostProcessor:
    _run_postprocessors.add(
        Dependent[Any].parse(call=func, allow_types=RUN_POSTPCS_PARAMS)
    )
    return func


async def _check_matcher(
        priority: int,
        Matcher: Type[Matcher],
        bot: "Bot",
        event: "Event",
        state: T_State,
        stack: Optional[AsyncExitStack] = None,
        dependency_cache: Optional[T_DependencyCache] = None,
) -> None:
    if Matcher.expire_time and datetime.now() > Matcher.expire_time:
        with contextlib.suppress(Exception):
            matchers[priority].remove(Matcher)
        return

    try:
        if not await Matcher.check_perm(
                bot, event, stack, dependency_cache
        ) or not await Matcher.check_rule(bot, event, state, stack, dependency_cache):
            return
    except Exception as e:
        logger.opt(colors=True, exception=e).error(
            f"<r><bg #f8bbd0>Rule check failed for {Matcher}.</bg #f8bbd0></r>"
        )
        return

    if Matcher.temp:
        with contextlib.suppress(Exception):
            matchers[priority].remove(Matcher)
    await _run_matcher(Matcher, bot, event, state, stack, dependency_cache)


async def _run_matcher(
        Matcher: Type[Matcher],
        bot: "Bot",
        event: "Event",
        state: T_State,
        stack: Optional[AsyncExitStack] = None,
        dependency_cache: Optional[T_DependencyCache] = None,
) -> None:
    # logger.info(f"消息匹配成功: {Matcher}")

    matcher = Matcher()
    if coros := [
        run_coro_with_catch(
            proc(
                matcher=matcher,
                bot=bot,
                event=event,
                state=state,
                stack=stack,
                dependency_cache=dependency_cache,
            ),
            (SkippedException,),
        )
        for proc in _run_preprocessors
    ]:
        with matcher.ensure_context(bot, event):
            try:
                await asyncio.gather(*coros)
            except IgnoredException:
                logger.opt(colors=True).info(f"{matcher} running is <b>cancelled</b>")
                return
            except Exception as e:
                logger.opt(colors=True, exception=e).error(
                    "<r><bg #f8bbd0>Error when running RunPreProcessors. Running cancelled!</bg #f8bbd0></r>"
                )

                return

    exception = None

    try:
        logger.debug(f"Running {matcher}")
        await matcher.run(bot, event, state, stack, dependency_cache)
    except Exception as e:
        logger.opt(colors=True, exception=e).error(
            f"<r><bg #f8bbd0>Running {matcher} failed.</bg #f8bbd0></r>"
        )
        exception = e

    if coros := [
        run_coro_with_catch(
            proc(
                matcher=matcher,
                exception=exception,
                bot=bot,
                event=event,
                state=matcher.state,
                stack=stack,
                dependency_cache=dependency_cache,
            ),
            (SkippedException,),
        )
        for proc in _run_postprocessors
    ]:
        with matcher.ensure_context(bot, event):
            try:
                await asyncio.gather(*coros)
            except Exception as e:
                logger.opt(colors=True, exception=e).error(
                    "<r><bg #f8bbd0>Error when running RunPostProcessors</bg #f8bbd0></r>"
                )

    if matcher.block:
        raise StopPropagation
    return


async def handle_event(bot: "Bot", event: "Event") -> None:
    show_log = True
    log_msg = ""
    try:
        log_msg += event.get_log_string()
    except NoLogException:
        show_log = False
    if show_log:
        logger.opt(colors=True).success(log_msg)

    state: Dict[Any, Any] = {}
    dependency_cache: T_DependencyCache = {}

    async with AsyncExitStack() as stack:
        if coros := [
            run_coro_with_catch(
                proc(
                    bot=bot,
                    event=event,
                    state=state,
                    stack=stack,
                    dependency_cache=dependency_cache,
                ),
                (SkippedException,),
            )
            for proc in _event_preprocessors
        ]:
            try:
                if show_log:
                    logger.debug("Running PreProcessors...")
                await asyncio.gather(*coros)
            except IgnoredException as e:
                logger.opt(colors=True).info(
                    f"Event {escape_tag(event.get_event_name())} is <b>ignored</b>"
                )
                return
            except Exception as e:
                logger.opt(colors=True, exception=e).error(
                    "<r><bg #f8bbd0>Error when running EventPreProcessors. "
                    "Event ignored!</bg #f8bbd0></r>"
                )
                return

        try:
            TrieRule.get_value(bot, event, state)
        except Exception as e:
            logger.opt(colors=True, exception=e).warning(
                "Error while parsing command for event"
            )

        break_flag = False
        for priority in sorted(matchers.keys()):
            if break_flag:
                break

            if show_log:
                logger.debug(f"Checking for matchers in priority {priority}...")

            pending_tasks = [
                _check_matcher(
                    priority, matcher, bot, event, state.copy(), stack, dependency_cache
                )
                for matcher in matchers[priority]
            ]

            results = await asyncio.gather(*pending_tasks, return_exceptions=True)

            for result in results:
                if not isinstance(result, Exception):
                    continue
                if isinstance(result, StopPropagation):
                    break_flag = True
                    logger.debug("Stop event propagation")
                else:
                    logger.opt(colors=True, exception=result).error(
                        "<r><bg #f8bbd0>Error when checking Matcher.</bg #f8bbd0></r>"
                    )

        if coros := [
            run_coro_with_catch(
                proc(
                    bot=bot,
                    event=event,
                    state=state,
                    stack=stack,
                    dependency_cache=dependency_cache,
                ),
                (SkippedException,),
            )
            for proc in _event_postprocessors
        ]:
            try:
                if show_log:
                    logger.debug("Running PostProcessors...")
                await asyncio.gather(*coros)
            except Exception as e:
                logger.opt(colors=True, exception=e).error(
                    "<r><bg #f8bbd0>Error when running EventPostProcessors</bg #f8bbd0></r>"
                )
