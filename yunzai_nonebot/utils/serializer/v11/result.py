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
        result = result.get_user_info.user
        return {
            "user_id": result.user_id,
            "nickname": result.nickname,
            "sex": result.sex,
            "age": result.age,
        }
    if result_type == "get_friend_list":
        result = result.get_friend_list
        return [
            {
                "user_id": friend.user_id,
                "nickname": friend.nickname,
                "sex": friend.sex,
                "remark": friend.remark,
            } for friend in result.friend_list
        ]
    if result_type == "get_group_info":
        result = result.get_group_info.group
        return {
            "group_id": result.group_id,
            "group_name": result.group_name,
            "group_create_time": result.group_create_time,
            "group_level": result.group_level,
            "member_count": result.member_count,
            "max_member_count": result.max_member_count,
        }
    if result_type == "get_group_list":
        result = result.get_group_list
        return [
            {
                "group_id": group.group_id,
                "group_name": group.group_name,
                "group_create_time": group.group_create_time,
                "group_level": group.group_level,
                "member_count": group.member_count,
                "max_member_count": group.max_member_count,
            } for group in result.group_list
        ]
    if result_type == "get_group_member_info":
        result = result.get_group_member_info.member
        return {
            "group_id": result.group_id,
            "user_id": result.user_id,
            "nickname": result.nickname,
            "card": result.card,
            "sex": result.sex,
            "age": result.age,
            "area": result.area,
            "join_time": result.join_time,
            "last_sent_time": result.last_sent_time,
            "level": result.level,
            "role": result.role,
            "title": result.title,
            "title_expire_time": result.title_expire_time,
            "shutup_timestamp": result.shutup_timestamp,
        }
    if result_type == "get_group_member_list":
        result = result.get_group_member_list
        return [
            {
                "group_id": group_member.group_id,
                "user_id": group_member.user_id,
                "nickname": group_member.nickname,
                "card": group_member.card,
                "sex": group_member.sex,
                "age": group_member.age,
                "area": group_member.area,
                "join_time": group_member.join_time,
                "last_sent_time": group_member.last_sent_time,
                "level": group_member.level,
                "role": group_member.role,
                "title": group_member.title,
                "title_expire_time": group_member.title_expire_time,
                "shutup_timestamp": group_member.shutup_timestamp,
            } for group_member in result.group_member_list
        ]
    if result_type == "send_forward_message":
        result = result.send_forward_message
        return {
            "message_id": result.message_id,
            "time": result.time
        }
