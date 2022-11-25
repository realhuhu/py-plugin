from uuid import uuid4
from typing import Optional, Dict
from asyncio.queues import LifoQueue


class AsyncQueueMCS(type):
    instance: Dict[str, Optional["AsyncQueue"]] = {}

    def __call__(cls: "AsyncQueue", type: str, *args, **kwargs) -> "AsyncQueue":
        if not cls.__class__.instance.get(type):
            cls.__class__.instance[type] = super().__call__(type, *args, **kwargs)

        return cls.__class__.instance[type]


class AsyncQueue(metaclass=AsyncQueueMCS):
    def __init__(self, type):
        self.queue = LifoQueue()
        self.type = type

    def __aiter__(self):
        return self

    def __str__(self):
        return f"<AsyncQueue({self.type}) id={id(self)}>"

    async def __anext__(self):
        return await self.queue.get()

    async def put(self, data):
        request_id = str(uuid4())
        await self.queue.put({"request_id": request_id, **data})
        return request_id


__all__ = [
    "AsyncQueue"
]
