from typing import Any, Tuple

from nonebot.adapters.onebot.v11 import Bot, Message
from yunzai_nonebot.rpc import hola_pb2, typing as GRPCTyping
from .message import convert, make_forward
from .utils import message_id_to_str
from yunzai_nonebot.utils.exception import DeserializeRequestError


def v11_to_request(bot: Bot, api: str, **data: Any) -> Tuple[str, GRPCTyping.GRPCRequest]:
    if api == "send_msg":
        return "send_message", hola_pb2.SendMessageRequest(
            detail_type=data.get("message_type"),
            user_id=int(data.get("user_id")),
            group_id=int(data.get("group_id")),
            message=convert(bot, Message(data.get("message")))
        )
    if api == "send_private_msg":
        return "send_message", hola_pb2.SendMessageRequest(
            detail_type="private",
            user_id=int(data.get("user_id")),
            message=convert(bot, Message(data.get("message")))
        )
    if api == "send_group_msg":
        return "send_message", hola_pb2.SendMessageRequest(
            detail_type="group",
            group_id=int(data.get("group_id")),
            message=convert(bot, Message(data.get("message")))
        )
    if api == "delete_msg":
        return "delete_message", hola_pb2.DeleteMessageRequest(
            message_id=message_id_to_str(data.get("message_id"))
        )
    if api == "get_msg":
        return "get_message", hola_pb2.GetMessageRequest(
            message_id=message_id_to_str(data.get("message_id"))
        )
    # if api == "get_forward_msg":
    #     return
    #     TODO
    if api == "send_like":
        return "send_like", hola_pb2.SendLikeRequest(
            user_id=int(data.get("user_id")),
            times=data.get("times")
        )
    if api == "set_group_kick":
        return "set_group_kick", hola_pb2.SetGroupKickRequest(
            group_id=int(data.get("group_id")),
            user_id=int(data.get("user_id")),
            reject_add_request=data.get("reject_add_request"),
        )
    if api == "set_group_ban":
        return "set_group_ban", hola_pb2.SetGroupBanRequest(
            group_id=int(data.get("group_id")),
            user_id=int(data.get("user_id")),
            duration=data.get("duration"),
        )
    if api == "set_group_anonymous_ban":
        return "set_group_anonymous_ban", hola_pb2.SetGroupAnonymousBanRequest(
            group_id=int(data.get("group_id")),
            anonymous=data.get("anonymous"),
            flag=data.get("flag"),
            anonymous_flag=data.get("anonymous_flag"),
            duration=data.get("duration"),
        )
    if api == "set_group_whole_ban":
        return "set_group_whole_ban", hola_pb2.SetGroupWholeBanRequest(
            group_id=int(data.get("group_id")),
            enable=data.get("enable")
        )
    if api == "set_group_admin":
        return "set_group_admin", hola_pb2.SetGroupAdminRequest(
            group_id=int(data.get("group_id")),
            user_id=int(data.get("user_id")),
            enable=data.get("enable")
        )
    if api == "set_group_anonymous":
        return "set_group_anonymous", hola_pb2.SetGroupAnonymousRequest(
            group_id=int(data.get("group_id")),
            enable=data.get("enable")
        )
    if api == "set_group_card":
        return "set_group_card", hola_pb2.SetGroupCardRequest(
            group_id=int(data.get("group_id")),
            user_id=int(data.get("user_id")),
            card=data.get("card")
        )
    if api == "set_group_name":
        return "set_group_name", hola_pb2.SetGroupNameRequest(
            group_id=int(data.get("group_id")),
            group_name=data.get("group_name"),
        )
    if api == "set_group_leave":
        return "set_group_leave", hola_pb2.SetGroupLeaveRequest(
            group_id=int(data.get("group_id")),
            is_dismiss=data.get("is_dismiss")
        )
    if api == "set_group_special_title":
        return "set_group_special_title", hola_pb2.SetGroupSpecialTitleRequest(
            group_id=int(data.get("group_id")),
            user_id=int(data.get("user_id")),
            special_title=data.get("special_title"),
            duration=data.get("duration")
        )
    if api == "set_friend_add_request":
        return "set_friend_add_request", hola_pb2.SetFriendAddRequestRequest(
            flag=data.get("flag"),
            approve=data.get("approve"),
            remark=data.get("remark")
        )
    if api == "set_group_add_request":
        return "set_group_add_request", hola_pb2.SetGroupAddRequestRequest(
            flag=data.get("flag"),
            sub_type=data.get("sub_type"),
            approve=data.get("approve"),
            reason=data.get("reason"),
        )
    if api == "get_login_info":
        return "get_self_info", hola_pb2.GetSelfInfoRequest()
    if api == "get_stranger_info":
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
    if api == "send_group_forward_msg":
        return "send_forward_message", hola_pb2.SendForwardMessageRequest(
            detail_type="group",
            group_id=int(data.get("group_id")),
            message=make_forward(bot, data.get("messages"))
        )
    if api == "send_private_forward_msg":
        return "send_forward_message", hola_pb2.SendForwardMessageRequest(
            detail_type="private",
            user_id=int(data.get("user_id")),
            message=make_forward(bot, data.get("messages"))
        )

    raise DeserializeRequestError(bot, api)
