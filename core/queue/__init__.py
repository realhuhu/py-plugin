from typing import Optional, Dict
from asyncio.queues import LifoQueue


class QueueMCS(type):
    instance: Dict[str, Optional["Queue"]] = {}

    def __call__(cls: "Queue", type: str, *args, **kwargs) -> "Queue":
        if not cls.__class__.instance.get(type):
            cls.__class__.instance[type] = super().__call__(type, *args, **kwargs)

        return cls.__class__.instance[type]


class Queue(metaclass=QueueMCS):
    def __init__(self, type):
        self.queue = LifoQueue()
        self.type = type

    def __aiter__(self):
        return self

    def __str__(self):
        return f"<Queue({self.type}) id={id(self)}>"

    async def __anext__(self):
        return await self.queue.get()

    async def put(self, data):
        await self.queue.put(data)


__all__ = [
    "Queue"
]
