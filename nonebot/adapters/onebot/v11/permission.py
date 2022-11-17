# DONE
from nonebot.permission import Permission

from .event import GroupMessageEvent, PrivateMessageEvent


async def _private(event: PrivateMessageEvent) -> bool:
    return True


async def _private_friend(event: PrivateMessageEvent) -> bool:
    return event.sub_type == "friend"


async def _private_group(event: PrivateMessageEvent) -> bool:
    return event.sub_type == "group"


async def _private_other(event: PrivateMessageEvent) -> bool:
    return event.sub_type == "other"


async def _group(event: GroupMessageEvent) -> bool:
    return True


async def _group_member(event: GroupMessageEvent) -> bool:
    return event.sender.role == "member"


async def _group_admin(event: GroupMessageEvent) -> bool:
    return event.sender.role == "admin"


async def _group_owner(event: GroupMessageEvent) -> bool:
    return event.sender.role == "owner"


PRIVATE: Permission = Permission(_private)
PRIVATE_FRIEND: Permission = Permission(_private_friend)
PRIVATE_GROUP: Permission = Permission(_private_group)
PRIVATE_OTHER: Permission = Permission(_private_other)
GROUP: Permission = Permission(_group)
GROUP_MEMBER: Permission = Permission(_group_member)
GROUP_ADMIN: Permission = Permission(_group_admin)
GROUP_OWNER: Permission = Permission(_group_owner)

__all__ = [
    "PRIVATE",
    "PRIVATE_FRIEND",
    "PRIVATE_GROUP",
    "PRIVATE_OTHER",
    "GROUP",
    "GROUP_MEMBER",
    "GROUP_ADMIN",
    "GROUP_OWNER",
]
