from typing import Any, Tuple

from nonebot.adapters.onebot.v12 import Bot, Message
from yunzai_nonebot.rpc import hola_pb2, typing as GRPCTyping
from .message import convert
from yunzai_nonebot.utils.exception import DeserializeRequestError


def v12_to_request(bot: Bot, api: str, **data: Any) -> Tuple[str, GRPCTyping.GRPCRequest]:
    if api == "send_message":
        return "send_message", hola_pb2.SendMessageRequest(
            detail_type=data.get("detail_type"),
            user_id=int(data.get("user_id")),
            group_id=int(data.get("group_id")),
            message=convert(bot, Message(data.get("message")))
        )
    if api == "delete_message":
        return "delete_message", hola_pb2.DeleteMessageRequest(
            message_id=data.get("message_id")
        )
    if api == "get_self_info":
        return "get_self_info", hola_pb2.GetSelfInfoRequest()
    if api == "get_user_info":
        return "get_user_info", hola_pb2.GetUserInfoRequest(
            user_id=int(data.get("user_id"))
        )
    if api == "get_friend_list":
        return "get_friend_list", hola_pb2.GetFriendListRequest()
    if api == "get_group_info":
        return "get_group_info", hola_pb2.GetGroupInfoRequest(
            group_id=int(data.get("group_id"))
        )
    if api == "get_group_list":
        return "get_group_list", hola_pb2.GetGroupListRequest()
    if api == "get_group_member_info":
        return "get_group_member_info", hola_pb2.GetGroupMemberInfoRequest(
            group_id=int(data.get("group_id")),
            user_id=int(data.get("user_id"))
        )
    if api == "get_group_member_list":
        return "get_group_member_list", hola_pb2.GetGroupMemberListRequest(
            group_id=int(data.get("group_id"))
        )
    if api == "set_group_name":
        return "set_group_name", hola_pb2.SetGroupNameRequest(
            group_id=int(data.get("group_id")),
            group_name=data.get("group_name"),
        )
    if api == "leave_group":
        return "set_group_leave", hola_pb2.SetGroupLeaveRequest(
            group_id=int(data.get("group_id")),
        )
    raise DeserializeRequestError(bot, api)
