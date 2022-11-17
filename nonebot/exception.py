# Done
from typing import Any, Optional

from pydantic.fields import ModelField


class NoneBotException(Exception):
    ...


class ParserExit(NoneBotException):

    def __init__(self, status: int = 0, message: Optional[str] = None):
        self.status = status
        self.message = message

    def __repr__(self) -> str:
        return (
                f"ParserExit(status={self.status}"
                + (f", message={self.message!r}" if self.message else "")
                + ")"
        )

    __str__ = __repr__


class ProcessException(NoneBotException):
    ...


class IgnoredException(ProcessException):
    def __init__(self, reason: Any):
        self.reason: Any = reason

    def __repr__(self) -> str:
        return f"IgnoredException(reason={self.reason!r})"

    __str__ = __repr__


class SkippedException(ProcessException):
    ...


class TypeMisMatch(SkippedException):
    def __init__(self, param: ModelField, value: Any):
        self.param: ModelField = param
        self.value: Any = value

    def __repr__(self) -> str:
        return (
            f"TypeMisMatch(param={self.param.name}, "
            f"type={self.param._type_display()}, value={self.value!r}>"
        )

    __str__ = __repr__


class MockApiException(ProcessException):

    def __init__(self, result: Any):
        self.result = result

    def __repr__(self) -> str:
        return f"MockApiException(result={self.result!r})"

    __str__ = __repr__


class StopPropagation(ProcessException):
    ...


class MatcherException(NoneBotException):
    ...


class PausedException(MatcherException):
    ...


class RejectedException(MatcherException):
    ...


class FinishedException(MatcherException):
    ...


class AdapterException(NoneBotException):

    def __init__(self, adapter_name: str, *args: object) -> None:
        super().__init__(*args)
        self.adapter_name: str = adapter_name


class NoLogException(AdapterException):
    ...


class ApiNotAvailable(AdapterException):
    ...


class NetworkError(AdapterException):
    ...


class ActionFailed(AdapterException):
    ...


class DriverException(NoneBotException):
    ...


class WebSocketClosed(DriverException):
    def __init__(self, code: int, reason: Optional[str] = None):
        self.code = code
        self.reason = reason

    def __repr__(self) -> str:
        return (
                f"WebSocketClosed(code={self.code}"
                + (f", reason={self.reason!r}" if self.reason else "")
                + ")"
        )

    __str__ = __repr__
