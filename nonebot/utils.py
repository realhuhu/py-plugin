# Done
import re
import json
import asyncio
import inspect
import dataclasses
from pathlib import Path
from functools import wraps, partial
from contextlib import asynccontextmanager
from typing_extensions import ParamSpec, get_args, get_origin
from typing import (
    Any,
    Type,
    Tuple,
    Union,
    TypeVar,
    Callable,
    Optional,
    Coroutine,
    AsyncGenerator,
    ContextManager,
    overload,
)

from pydantic.typing import is_union, is_none_type

from .log import logger
from .typing import overrides

P = ParamSpec("P")
R = TypeVar("R")
T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


def escape_tag(s: str) -> str:
    return re.sub(r"</?((?:[fb]g\s)?[^<>\s]*)>", r"\\\g<0>", s)


def generic_check_issubclass(
        cls: Any, class_or_tuple: Union[Type[Any], Tuple[Type[Any], ...]]
) -> bool:
    try:
        return issubclass(cls, class_or_tuple)
    except TypeError:
        origin = get_origin(cls)
        if is_union(origin):
            return all(
                is_none_type(type_) or generic_check_issubclass(type_, class_or_tuple)
                for type_ in get_args(cls)
            )
        elif origin:
            return issubclass(origin, class_or_tuple)
        return False


def is_coroutine_callable(call: Callable[..., Any]) -> bool:
    if inspect.isroutine(call):
        return inspect.iscoroutinefunction(call)
    if inspect.isclass(call):
        return False
    func_ = getattr(call, "__call__", None)
    return inspect.iscoroutinefunction(func_)


def is_gen_callable(call: Callable[..., Any]) -> bool:
    if inspect.isgeneratorfunction(call):
        return True
    func_ = getattr(call, "__call__", None)
    return inspect.isgeneratorfunction(func_)


def is_async_gen_callable(call: Callable[..., Any]) -> bool:
    if inspect.isasyncgenfunction(call):
        return True
    func_ = getattr(call, "__call__", None)
    return inspect.isasyncgenfunction(func_)


def run_sync(call: Callable[P, R]) -> Callable[P, Coroutine[None, None, R]]:
    @wraps(call)
    async def _wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        loop = asyncio.get_running_loop()
        pfunc = partial(call, *args, **kwargs)
        result = await loop.run_in_executor(None, pfunc)
        return result

    return _wrapper


@asynccontextmanager
async def run_sync_ctx_manager(
        cm: ContextManager[T],
) -> AsyncGenerator[T, None]:
    try:
        yield await run_sync(cm.__enter__)()
    except Exception as e:
        ok = await run_sync(cm.__exit__)(type(e), e, None)
        if not ok:
            raise e
    else:
        await run_sync(cm.__exit__)(None, None, None)


@overload
async def run_coro_with_catch(
        coro: Coroutine[Any, Any, T],
        exc: Tuple[Type[Exception], ...],
) -> Union[T, None]:
    ...


@overload
async def run_coro_with_catch(
        coro: Coroutine[Any, Any, T],
        exc: Tuple[Type[Exception], ...],
        return_on_err: R,
) -> Union[T, R]:
    ...


async def run_coro_with_catch(
        coro: Coroutine[Any, Any, T],
        exc: Tuple[Type[Exception], ...],
        return_on_err: Optional[R] = None,
) -> Optional[Union[T, R]]:
    try:
        return await coro
    except exc:
        return return_on_err


def get_name(obj: Any) -> str:
    if inspect.isfunction(obj) or inspect.isclass(obj):
        return obj.__name__
    return obj.__class__.__name__


def path_to_module_name(path: Path) -> str:
    rel_path = path.resolve().relative_to(Path(".").resolve())
    if rel_path.stem == "__init__":
        return ".".join(rel_path.parts[:-1])
    else:
        return ".".join(rel_path.parts[:-1] + (rel_path.stem,))


class DataclassEncoder(json.JSONEncoder):
    @overrides(json.JSONEncoder)
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return {f.name: getattr(o, f.name) for f in dataclasses.fields(o)}
        return super().default(o)


def logger_wrapper(logger_name: str):
    def log(level: str, message: str, exception: Optional[Exception] = None):
        logger.opt(colors=True, exception=exception).log(
            level, f"<m>{escape_tag(logger_name)}</m> | {message}"
        )

    return log
