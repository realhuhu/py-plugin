# DONE
from datetime import timedelta
from ipaddress import IPv4Address
from typing import Set, Union, Optional

from pydantic import IPvAnyAddress


class Env:
    environment: str = "prod"


class Config(dict):
    def __init__(self, **kwargs):
        kwargs["host"] = IPv4Address(kwargs.get("host", "127.0.0.1"))
        kwargs["port"] = int(kwargs.get("port", 50052))
        kwargs["log_level"] = kwargs.get("log_level", "INFO")
        kwargs["api_timeout"] = float(kwargs.get("api_timeout", 30.0))
        kwargs["superusers"] = set(map(str, kwargs.get("superusers", {})))
        kwargs["nickname"] = set(map(str, kwargs.get("nickname", {})))
        kwargs["command_start"] = set(map(str, kwargs.get("command_start", {})))
        kwargs["session_expire_timeout"] = timedelta(minutes=2)
        super().__init__(kwargs)

    def __getattr__(self, item):
        return self.get(item)

    def dict(self):
        return self
