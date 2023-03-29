export const parse_message = async message => {
  return message.map(segment => {
    //OMIT<MiraiElem,FileElem>
    switch (segment.type) {
      //TextElem
      case "text":
        return {
          text: {
            data: segment.text
          }
        }
      //AtElem
      case "at"://OMIT<id,text,dummy>
        return {
          at: {
            qq: segment.qq,
          }
        }
      //FaceElem
      case "face"://OMIT<text>
        return {
          face: {
            id: segment.id
          }
        }
      case "sface"://PY UNIMPLEMENTED
        return {
          text: {
            data: `[sface ${segment.text}]`
          }
        }
      //BfaceElem
      case "bface"://PY UNIMPLEMENTED
        return {
          text: {
            data: `[bface ${segment.text}]`
          }
        }
      //MfaceElem
      case "rps"://OMIT<id>
        return {
          rps: {}
        }
      case "dice"://OMIT<id>
        return {
          dice: {}
        }
      //ImageElem
      case "image"://OMIT<asface>
        return {
          image: {
            file: segment.file,
            url: segment.url,
          }
        }
      //FlashElem
      case "flash"://OMIT<asface>
        return {
          image: {
            file: segment.file,
            type: "flash",
            url: segment.url,
          }
        }
      //PttElem
      case "record"://OMIT<md5,size,seconds>
        return {
          record: {
            file: segment.file,
            url: segment.url,
          }
        }
      //VideoElem
      case "video"://OMIT<name,fid,md5,size,seconds>
        return {
          video: {
            file: segment.file,
            url: undefined//TODO
          }
        }
      //LocationElem
      case "location"://OMIT<id>
        return {
          location: {
            lat: segment.lat,
            lon: segment.lon,
            title: segment.name,
            content: segment.address
          }
        }
      //ShareElem
      case "share":
        return {
          share: {
            url: segment.url,
            title: segment.title,
            content: segment.content,
            image: segment.image
          }
        }
      //JsonElem
      case "json":
        return {
          json: {
            data: segment.data
          }
        }
      //XmlElem
      case "xml"://OMIT<id>
        return {
          xml: {
            data: segment.data
          }
        }
      //PokeElem
      case "poke":
        return {
          poke: {
            type: segment.type,
            id: segment.id,
            name: segment.text
          }
        }
      //ReplyElem
      case "reply":
        return {
          reply: {
            id: segment.id,
          }
        }
      default:
        logger.warn(`[py-plugin][parse-message] 无法识别的消息:${segment}`)
        return {
          text: {
            data: "[py-plugin未知消息]",
          }
        }
    }
  }).filter(x => x)
}

export const parse_sender = async sender => {
  return {
    user_id: sender.user_id,
    nickname: sender.nickname,
    sex: sender.sex || "unknown",
    age: sender.age,
    card: sender.card,
    area: sender.area,
    level: sender.level?.toString(),
    role: sender.role,
    title: sender.title
  }
}

export const parse_reply = async (handler, flag) => {
  let message = await handler.getChatHistory(flag, 1)
  message = message && message.pop()
  return message && {
    time: message.time,
    message_type: message.message_type,
    message_id: message.message_id,
    sender: await parse_sender(message.sender),
    message: await parse_message(message.message)
  }

}

export const parse_anonymous = async anonymous => {
  return anonymous && {
    id: anonymous.id,
    name: anonymous.name,
    flag: anonymous.flag
  }
}

const call_back = (channel, data) => {
  data && channel.write({
    event: {
      plugins: py_plugin_config.plugins.map(x => x.replace(/-/g, "_")),
      self_id: Bot.uin.toString(),
      ...data
    }
  })
}

export const message_receiver = async (channel, event) => {
  let data
  switch (event.message_type) {
    case "private":
      data = {
        private_message: {
          time: event.time,
          self_id: event.self_id,
          sub_type: event.sub_type,
          message_id: event.message_id,
          user_id: event.user_id,
          message: await parse_message(event.message),
          raw_message: event.raw_message,
          sender: await parse_sender(event.sender),
          to_me: true,
          reply: event.source && await parse_reply(event.friend, event.source.time + 1)
        }
      }
      break
    case "group":
      data = {
        group_message: {
          time: event.time,
          self_id: event.self_id,
          sub_type: event.sub_type,
          message_id: event.message_id,
          group_id: event.group_id,
          user_id: event.user_id,
          anonymous: await parse_anonymous(event.anonymous),
          message: await parse_message(event.message),
          raw_message: event.raw_message,
          sender: await parse_sender(event.sender),
          to_me: event.atme,
          reply: event.source && await parse_reply(event.group, event.source.seq)
        }
      }
      break
    default:
      return `[py-plugin][before-match-message] 未知的message类型`
  }
  call_back(channel, data)
}

export const request_receiver = async (channel, event) => {
  let data
  switch (`${event.request_type}.${event.sub_type}`) {
    case "friend.add":
    case "friend.single":
      data = {
        friend_request: {
          time: event.time,
          self_id: event.self_id,
          user_id: event.user_id,
          comment: event.comment,
          flag: event.flag
        }
      }
      break
    case "group.add":
    case "group.invite":
      data = {
        group_request: {
          time: event.time,
          self_id: event.self_id,
          sub_type: event.sub_type,
          group_id: event.group_id,
          user_id: event.user_id,
          comment: event.comment,
          flag: event.flag
        }
      }
      break
    default:
      return `[py-plugin][before-match-request] 未知的request类型`
  }
  call_back(channel, data)
}

export const notice_receiver = async (channel, event) => {
  let data, time = Math.round(new Date().getTime() / 1000)
  //OMIT<FriendDecreaseEvent,GroupTransferEvent>
  switch (`${event.notice_type}.${event.sub_type}`) {
    //FriendIncreaseEvent
    case "friend.increase":
      data = {
        friend_add_notice: {
          time: time,//OVERWRITE
          self_id: event.self_id,
          user_id: event.user_id
        }
      }
      break
    //FriendDecreaseEvent
    case "friend.recall"://OMIT<operator_id,seq,rand,time>
      data = {
        friend_recall_notice: {
          time: time,//OVERWRITE
          self_id: event.self_id,
          user_id: event.user_id,
          message_id: event.message_id
        }
      }
      break
    //FriendPokeEvent OVERWRITE
    case "friend.poke"://OMIT<operator_id,action,suffix>
      data = {
        private_message: {
          time: time,//OVERWRITE
          self_id: event.self_id,
          sub_type: "friend",//OVERWRITE
          user_id: event.user_id,
          message: [{poke: {}}],//TODO
          sender: {
            user_id: event.operator_id,
            nickname: event.sender.nickname,
          },
          to_me: event.target_id === event.self_id,
        }
      }
      break
    //MemberIncreaseEvent
    case "group.increase"://OMIT<nickname>
      data = {
        group_increase_notice: {
          time: time,//OVERWRITE
          self_id: event.self_id,
          sub_type: event.sub_type,
          user_id: event.user_id,
          group_id: event.group_id,
          operator_id: 0//JS UNIMPLEMENTED
        }
      }
      break
    //MemberDecreaseEvent
    case "group.decrease"://OMIT<dismiss,member>
      data = {
        group_decrease_notice: {
          time: time,//OVERWRITE
          self_id: event.self_id,
          sub_type: event.sub_type,
          user_id: event.user_id,
          group_id: event.group_id,
          operator_id: event.operator_id
        }
      }
      break
    //GroupRecallEvent
    case "group.recall"://OMIT<seq,rand,time>
      data = {
        group_recall_notice: {
          time: time,//OVERWRITE
          self_id: event.self_id,
          user_id: event.user_id,
          group_id: event.group_id,
          operator_id: event.operator_id,
          message_id: event.message_id
        }
      }
      break
    //GroupMuteEvent
    case "group.ban"://OMIT<nickname>
      data = {
        group_ban_notice: {
          time: time,//OVERWRITE
          self_id: event.self_id,
          sub_type: event.duration ? "ban" : "lift_ban",
          user_id: event.user_id,
          group_id: event.group_id,
          operator_id: event.operator_id,
          duration: event.duration
        }
      }
      break
    //GroupAdminEvent
    case "group.admin":
      data = {
        group_admin_notice: {
          time: time,//OVERWRITE
          self_id: event.self_id,
          sub_type: event.set ? "set" : "unset",
          user_id: event.user_id,
          group_id: event.group_id
        }
      }
      break
    //GroupPokeEvent
    case "group.poke"://OMIT<action,suffix>
      data = {
        poke_notify: {
          time: time,//OVERWRITE
          self_id: event.self_id,
          post_type: event.post_type,
          notice_type: "notify",//OVERWRITE
          sub_type: event.sub_type,
          user_id: event.user_id,
          target_id: event.target_id,
          group_id: event.group_id
        }
      }
      break
    default:
      return `[py-plugin][before-match-notice] 未知的notice类型`
  }
  call_back(channel, data)
}
