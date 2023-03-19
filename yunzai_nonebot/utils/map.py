import asyncio
from typing import Any, Dict, Optional

from yunzai_nonebot.rpc import hola_pb2


class AsyncMapMCS(type):
    instance: Dict[str, Optional["AsyncMap"]] = {}

    def __call__(cls: "AsyncMap", type: str, *args, **kwargs) -> "AsyncMap":
        if not cls.__class__.instance.get(type):
            cls.__class__.instance[type] = super().__call__(type, *args, **kwargs)

        return cls.__class__.instance[type]


class AsyncMap(metaclass=AsyncMapMCS):
    def __init__(self, type):
        self.type: str = type
        self._map: Dict[str, asyncio.Future] = {}

    def __str__(self):
        return f"<AsyncMap({self.type}) id={id(self)}>"

    async def set(self, request_id: str, value: Any) -> None:
        future = self._map.get(request_id)
        if future:
            future.set_result(value)

    async def get(self, request_id: str, timeout=10) -> Optional[hola_pb2.Result]:
        future = asyncio.get_event_loop().create_future()
        self._map[request_id] = future
        try:
            return await asyncio.wait_for(future, timeout)
        except asyncio.TimeoutError:
            return None
        finally:
            del self._map[request_id]
