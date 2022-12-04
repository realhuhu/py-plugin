# DONE
from datetime import timedelta
from ipaddress import IPv4Address


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
        kwargs["command_start"] = set(kwargs.get("command_start", {"#"}))
        kwargs["command_sep"] = set(kwargs.get("command_sep", {"."}))
        kwargs["session_expire_timeout"] = timedelta(minutes=2)
        kwargs["startup_check"] = kwargs.get("startup_check", True)
        kwargs["shutdown_check"] = kwargs.get("shutdown_check", True)
        super().__init__(kwargs)
        for k, v in kwargs.items():
            setattr(self, k, v)

    def dict(self):
        return self
