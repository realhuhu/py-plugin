import {parse_sender, parse_message} from "./receiver.js";
import {setup_client} from "./client.js";

const parse_user = x => {
  return {
    user_id: x.user_id,
    nickname: x.nickname
  }
}
const parse_group = x => {
  return {
    group_id: x.group_id,
    group_name: x.group_name
  }
}

const parse_grpc_message = async message => {
  let serialized_message = [], anonymous = false, music = null, source = null
  for (let message_segment of message) {
    let type = message_segment.segment
    let data = message_segment[type]
    switch (type) {
      case "text":
        serialized_message.push(data.data)
        break
      case "face":
        serialized_message.push(segment.face(data.id))
        break
      case "image":
        serialized_message.push(segment.image(data.file || data.content))
        break
      case "record":
        serialized_message.push(segment.record(data.file || data.content))
        break
      case "video":
        serialized_message.push(segment.video(data.file || data.content))
        break
      case "at":
        serialized_message.push(segment.at(Number(data.qq)))
        break
      case "rps":
        serialized_message.push(segment.rps())
        break
      case "dice":
        serialized_message.push(segment.dice())
        break
      case "poke":
        serialized_message.push(segment.poke(data.id))
        break
      case "anonymous":
        anonymous = true
        break
      case "share":
        serialized_message.push(segment.share(data.url, data.title, data.image, data.content))
        break
      case "contact":
        break
      case "location":
        serialized_message.push(segment.location(data.lat, data.lon, data.title))
        break
      case "music":
        music = data
        break
      case "custom_music":
        break
      case "reply":
        source = await Bot.getMsg(data.id)
        break
      case "xml":
        serialized_message.push(segment.xml(data.data))
        break
      case "json":
        serialized_message.push(segment.json(data.data))
        break
    }
  }
  return {serialized_message, source, anonymous, music}
}

const resolve_request = async request => {
  let type = request.request
  let load = request[type]
  switch (type) {
    case "send_message":
      let {serialized_message, source, anonymous, music} = await parse_grpc_message(load.message), client
      client = (load.detail_type === "group" || Number(load.group_id)) ? Bot.pickGroup(load.group_id) : Bot.pickFriend(load.user_id)
      if (music) return await client.shareMusic(music.type, music.id)
      return await client.sendMsg(serialized_message, source, anonymous)
    case "delete_message":
      return await Bot.deleteMsg(load.message_id)
    case "get_message":
      return await Bot.getMsg(load.message_id)
    case "get_forward_message":
      return await Bot.getForwardMsg(load.id)
    case "send_like":
      return await Bot.sendLike(load.user_id, load.times)
    case "set_group_kick":
      return await Bot.pickGroup(load.group_id).kickMember(load.user_id, "", load.reject_add_request)
    case "set_group_ban":
      return await Bot.pickGroup(load.group_id).muteMember(load.user_id, load.duration)
    case "set_group_anonymous_ban":
      return await Bot.pickGroup(load.group_id).muteAnony(load.anonymous_flag, load.duration)
    case "set_group_whole_ban":
      return await Bot.pickGroup(load.group_id).muteAll(load.enable)
    case "set_group_admin":
      return await Bot.pickGroup(load.group_id).setAdmin(load.user_id, load.enable)
    case "set_group_anonymous":
      return await Bot.pickGroup(load.group_id).allowAnony(load.enable)
    case "set_group_card":
      return await Bot.pickGroup(load.group_id).setCard(load.user_id, load.card)
    case "set_group_name":
      return await Bot.pickGroup(load.group_id).setName(load.group_name)
    case "set_group_leave":
      return await Bot.pickGroup(load.group_id).quit()
    case "set_group_special_title":
      return await Bot.pickGroup(load.group_id).setTitle(load.user_id, load.special_title, load.duration)
    case "set_friend_add_request":
      return await Bot.setFriendAddRequest(load.flag, load.approve, load.remark)
    case "set_group_add_request":
      return await Bot.setGroupAddRequest(load.flag, load.approve, load.reason)
    case "get_self_info":
      return {user_id: Bot.uin, nickname: Bot.nickname}
    case "get_user_info":
      return await Bot.getStrangerInfo(load.user_id)
    case "get_friend_list":
      return Bot.getFriendList()
    case "get_group_info":
      return await Bot.getGroupInfo(load.group_id)
    case "get_group_list":
      return Bot.getGroupList()
    case "get_group_member_info":
      return await Bot.pickMember(load.group_id, load.user_id).renew()
    case "get_group_member_list":
      return await Bot.pickGroup(load.group_id).getMemberMap()
    case "send_forward_message":
      let forward_message = await Promise.all(load.message.map(async node => ({
        user_id: Number(node.uin),
        nickname: node.name,
        message: (await parse_grpc_message(node.content)).serialized_message
      })))
      if (load.detail_type === "group") {
        return await Bot.pickGroup(load.group_id).sendMsg(segment.xml((await Bot.pickGroup(load.group_id).makeForwardMsg(forward_message)).data))
      } else {
        return await Bot.pickFriend(load.user_id).sendMsg(segment.xml((await Bot.pickFriend(load.user_id).makeForwardMsg(forward_message)).data))
      }
  }
}

const create_result = async (request, raw) => {
  let type = request.request
  let data
  switch (type) {
    case "send_message":
      data = {message_id: raw.message_id, time: raw.time}
      break
    case "get_message":
      data = {
        message_id: raw.message_id,
        real_id: 0,//OVERWRITE
        sender: await parse_sender(raw.sender), time: raw.time, message: await parse_message(raw.message)
      }
      break
    case "send_forward_message":
      data = {
        message_id: raw.message_id,
        time: raw.time
      }
      break
    case "get_forward_message":
      data = {} //TODO
      break
    case "get_self_info":
      data = raw
      break
    case "get_user_info":
      data = parse_user(raw)
      break
    case "get_friend_list":
      data = {friend_list: [...raw.values()].map(parse_user)}
      break
    case "get_group_info":
      data = parse_group(raw)
      break
    case "get_group_list":
      data = {group_list: [...raw.values()].map(parse_group)}
      break
    case "get_group_member_info":
      data = parse_user(raw)
      break
    case "get_group_member_list":
      data = {member_list: [...raw.values()].map(parse_user)}
      break
    case "delete_message":
    case "send_like":
    case "set_group_kick":
    case "set_group_ban":
    case "set_group_anonymous_ban":
    case "set_group_whole_ban":
    case "set_group_admin":
    case "set_group_anonymous":
    case "set_group_card":
    case "set_group_name":
    case "set_group_leave":
    case "set_group_special_title":
    case "set_friend_add_request":
    case "set_group_add_request":
      data = {}
      break
  }

  return data && {
    result: {
      request_id: request.request_id, self_id: Bot.uin.toString(), [type]: data
    }
  }
}

export const setup_channel = (client, ignore, retry) => new Promise((resolve, reject) => {
  return new Promise(resolve1 => {
    client.Option({code: 100}, (err, response) => {
      resolve1(err && err.details)
    })
  }).then(err => {
    if (err && !ignore) {
      reject(`[py-plugin] 连接服务器错误: ${err}`)
    } else if (err) {
      logger.error(`[py-plugin] 连接服务器错误: ${err}，${retry}秒后尝试重连`)
      setTimeout(() => {
        setup_client(true, retry >= 320 ? 600 : retry * 2)
      }, retry * 1000)
    } else {
      logger.info("[py-plugin] 连接服务器成功")
      let channel = client.Channel()
      channel.on("data", data => {
        resolve_request(data.request).then(raw => {
          return create_result(data.request, raw)
        }).then(result => {
          result && channel.write(result)
        })
      });
      channel.on("error", err => {
        if (err.details) {
          logger.error(`[py-plugin] 服务器连接丢失：${err.details}，5秒后尝试重连`);
          retry = 5;
          setTimeout(() => {
            setup_client(true, retry >= 320 ? 600 : retry * 2)
          }, retry * 1000)
        }
      });
      channel.write({head: {self_id: Bot.uin.toString()}})
      resolve(channel)
    }
  })
})
