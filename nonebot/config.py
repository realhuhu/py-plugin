# DONE
from datetime import timedelta
from ipaddress import IPv4Address
from typing import Set, Union, Optional

from pydantic import IPvAnyAddress


class Env:
    environment: str = "prod"


class Config:
    host: IPvAnyAddress = IPv4Address("127.0.0.1")

    port: int = 8080

    log_level: Union[int, str] = "INFO"

    api_timeout: Optional[float] = 30.0

    superusers: Set[str] = set()

    nickname: Set[str] = set()

    command_start: Set[str] = {"#"}

    command_sep: Set[str] = {"."}

    session_expire_timeout: timedelta = timedelta(minutes=2)

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

        self.config = {
            **self.__class__.__dict__["__annotations__"],
            **self.__dict__
        }

        self.config["host"] = IPv4Address(self.config["host"])
        self.config["superusers"] = set(self.config["superusers"])
        self.config["nickname"] = set(self.config["nickname"])

    def __getattr__(self, item):
        return self.config.get(item)

    def dict(self):
        return self.config
