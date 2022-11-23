import asyncio
from collections import deque
from typing import Union, Any, Dict, Optional


class AsyncMapMCS(type):
    instance: Dict[str, Optional["AsyncMap"]] = {}

    def __call__(cls: "AsyncMap", type: str, *args, **kwargs) -> "AsyncMap":
        if not cls.__class__.instance.get(type):
            cls.__class__.instance[type] = super().__call__(type, *args, **kwargs)

        return cls.__class__.instance[type]


class AsyncMap(metaclass=AsyncMapMCS):
    def __init__(self, type):
        self.type = type
        self._map = {}
        self._getters = deque()

    def __str__(self):
        return f"<AsyncMap({self.type}) id={id(self)}>"

    @staticmethod
    def _wakeup_next(waiters: deque):
        while waiters:
            waiter = waiters.popleft()
            if not waiter.done():
                waiter.set_result(None)
                break

    async def set(self, key: Union[int, str], value: Any) -> None:
        self._map[key] = value
        self._wakeup_next(self._getters)

    async def get(self, key: Union[int, str]) -> Any:
        while not self._map.get(key):
            getter = asyncio.Future()
            self._getters.append(getter)
            try:
                await getter
            except:
                getter.cancel()
                try:
                    self._getters.remove(getter)
                except ValueError:
                    pass
                if self._map.get(key) and not getter.cancelled():
                    self._wakeup_next(self._getters)
                raise
        item = self._map[key]
        del self._map[key]
        return item


__all__ = [
    "AsyncMap"
]
