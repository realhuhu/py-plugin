from yunzai_nonebot.rpc import hola_pb2
from .utils import sender_parser, message_parser


def result_to_v11(result: hola_pb2.Result):
    result_type = result.WhichOneof("result")
    if result_type == "send_message":
        result = result.send_message
        return {
            "message_id": result.message_id,
            "time": result.time
        }
    if result_type == "delete_message":
        return None
    if result_type == "get_message":
        result = result.get_message
        return {
            "message_id": result.message_id,
            "real_id": result.real_id,
            "time": result.time,
            "sender": sender_parser(result.sender),
            "message": message_parser(result.message)
        }
    if result_type == "get_forward_message":
        return  # TODO
    if result_type == "send_like":
        return None
    if result_type == "set_group_kick":
        return None
    if result_type == "set_group_ban":
        return None
    if result_type == "set_group_anonymous_ban":
        return None
    if result_type == "set_group_whole_ban":
        return None
    if result_type == "set_group_admin":
        return None
    if result_type == "set_group_anonymous":
        return None
    if result_type == "set_group_card":
        return None
    if result_type == "set_group_name":
        return None
    if result_type == "set_group_leave":
        return None
    if result_type == "set_group_special_title":
        return None
    if result_type == "set_friend_add_request":
        return None
    if result_type == "set_group_add_request":
        return None
    if result_type == "get_self_info":
        result = result.get_self_info
        return {
            "user_id": result.user_id,
            "nickname": result.nickname
        }
    if result_type == "get_user_info":
        result = result.get_user_info
        return {
            "user_id": result.user_id,
            "nickname": result.nickname
        }
    if result_type == "get_friend_list":
        result = result.get_friend_list
        return [
            {
                "user_id": friend.user_id,
                "nickname": friend.nickname
            } for friend in result.friend_list
        ]
    if result_type == "get_group_info":
        result = result.get_group_info
        return {
            "group_id": result.group_id,
            "group_name": result.group_name,
        }
    if result_type == "get_group_list":
        result = result.get_group_list
        return [
            {
                "group_id": group.group_id,
                "group_name": group.group_name,
            } for group in result.group_list
        ]
    if result_type == "get_group_member_info":
        result = result.get_group_member_info
        return {
            "user_id": result.user_id,
            "nickname": result.nickname
        }
    if result_type == "get_group_member_list":
        result = result.get_group_member_list
        return [
            {
                "user_id": group_member.user_id,
                "nickname": group_member.nickname
            } for group_member in result.group_member_list
        ]
    if result_type == "send_forward_message":
        result = result.send_forward_message
        return {
            "message_id": result.message_id,
            "time": result.time
        }
