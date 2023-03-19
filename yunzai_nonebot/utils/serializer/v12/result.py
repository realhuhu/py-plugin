from yunzai_nonebot.rpc import hola_pb2


def result_to_v12(result: hola_pb2.Result):
    result_type = result.WhichOneof("result")
    if result_type == "send_message":
        result = result.send_message
        return {
            "message_id": result.message_id,
            "time": result.time
        }
    if result_type == "delete_message":
        return None
    if result_type == "get_self_info":
        result = result.get_self_info
        return {
            "user_id": str(result.user_id),
            "user_name": result.nickname,
            "user_displayname": "PyBot"
        }
    if result_type == "get_user_info":
        result = result.get_user_info
        return {
            "user_id": str(result.user_id),
            "user_name": result.nickname,
            "user_displayname": result.nickname
        }
    if result_type == "get_friend_list":
        result = result.get_friend_list
        return [
            {
                "user_id": str(friend.user_id),
                "user_name": friend.nickname,
                "user_displayname": friend.nickname
            } for friend in result.friend_list
        ]
    if result_type == "get_group_info":
        result = result.get_group_info
        return {
            "group_id": str(result.group_id),
            "group_name": result.group_name,
        }
    if result_type == "get_group_list":
        result = result.get_group_list
        return [
            {
                "group_id": str(group.group_id),
                "group_name": group.group_name,
            } for group in result.group_list
        ]
    if result_type == "get_group_member_info":
        result = result.get_group_member_info
        return {
            "user_id": str(result.user_id),
            "user_name": result.nickname,
            "user_displayname": result.nickname
        }
    if result_type == "get_group_member_list":
        result = result.get_group_member_list
        return [
            {
                "user_id": str(group_member.user_id),
                "user_name": group_member.nickname,
                "user_displayname": group_member.nickname
            } for group_member in result.group_member_list
        ]
    if result_type == "set_group_name":
        return None
    if result_type == "set_group_leave":
        return None
