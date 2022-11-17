# DONE
from typing import (
    Any,
    Dict,
    Union,
    TypeVar,
    Callable,
    Optional,
    Awaitable,
)

T = TypeVar("T")
_DependentCallable = Union[Callable[..., T], Callable[..., Awaitable[T]]]

T_State = Dict[Any, Any]
T_Wrapped = TypeVar("T_Wrapped", bound=Callable)
T_BotConnectionHook = _DependentCallable[Any]
T_BotDisconnectionHook = _DependentCallable[Any]
T_CallingAPIHook = Callable[["Bot", str, Dict[str, Any]], Awaitable[Any]]
T_CalledAPIHook = Callable[["Bot", Optional[Exception], str, Dict[str, Any], Any], Awaitable[Any]]
T_EventPreProcessor = _DependentCallable[Any]
T_EventPostProcessor = _DependentCallable[Any]
T_RunPreProcessor = _DependentCallable[Any]
T_RunPostProcessor = _DependentCallable[Any]
T_RuleChecker = _DependentCallable[bool]
T_PermissionChecker = _DependentCallable[bool]
T_Handler = _DependentCallable[Any]
T_TypeUpdater = _DependentCallable[str]
T_PermissionUpdater = _DependentCallable["Permission"]
T_DependencyCache = Dict[_DependentCallable[Any], "Task[Any]"]


def overrides(InterfaceClass: object) -> Callable[[T_Wrapped], T_Wrapped]:
    def overrider(func: T_Wrapped) -> T_Wrapped:
        assert func.__name__ in dir(InterfaceClass), f"Error method: {func.__name__}"
        return func

    return overrider
