import abc
from typing import Any, Type, TypeVar

from pydantic import BaseModel

from nonebot.utils import DataclassEncoder

from .message import Message

E = TypeVar("E", bound="Event")


class Event(abc.ABC, BaseModel):
    class Config:
        extra = "allow"
        json_encoders = {Message: DataclassEncoder}

    @classmethod
    def validate(cls: Type["E"], value: Any) -> "E":
        if isinstance(value, Event) and not isinstance(value, cls):
            raise TypeError(f"{value} is incompatible with Event type {cls}")
        return super().validate(value)

    @abc.abstractmethod
    def get_type(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def get_event_name(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def get_event_description(self) -> str:
        raise NotImplementedError

    def __str__(self) -> str:
        return f"[{self.get_event_name()}]{self.get_event_description()}"

    def get_log_string(self) -> str:
        return f"[{self.get_event_name()}]{self.get_event_description()}"

    @abc.abstractmethod
    def get_user_id(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def get_session_id(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def get_message(self) -> "Message":
        raise NotImplementedError

    def get_plaintext(self) -> str:
        return self.get_message().extract_plain_text()

    @abc.abstractmethod
    def is_tome(self) -> bool:
        raise NotImplementedError
