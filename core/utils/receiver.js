function parse_message(message) {
  return message.map(segment => {
    //OMIT<MiraiElem,FileElem>
    switch (segment.type) {
      //TextElem
      case "text":
        return {
          TextSegment: {
            data: segment.text
          }
        }
      //AtElem
      case "at"://OMIT<id,text,dummy>
        return {
          AtSegment: {
            qq: segment.qq,
          }
        }
      //FaceElem
      case "face"://OMIT<text>
        return {
          FaceSegment: {
            id: segment.id
          }
        }
      case "sface"://PY UNIMPLEMENTED
        return {
          TextSegment: {
            data: `[sface ${segment.text}]`
          }
        }
      //BfaceElem
      case "bface"://PY UNIMPLEMENTED
        return {
          TextSegment: {
            data: `[bface ${segment.text}]`
          }
        }
      //MfaceElem
      case "rps"://OMIT<id>
        return {
          DiceSegment: {}
        }
      case "dice"://OMIT<id>
        return {
          DiceSegment: {}
        }
      //ImageElem
      case "image"://OMIT<asface>
        return {
          ImageSegment: {
            file: segment.file,
            url: segment.url,
          }
        }
      //FlashElem
      case "flash"://OMIT<asface>
        return {
          ImageSegment: {
            file: segment.file,
            type: "flash",
            url: segment.url,
          }
        }
      //PttElem
      case "record"://OMIT<md5,size,seconds>
        return {
          RecordSegment: {
            file: segment.file,
            url: segment.url,
          }
        }
      //VideoElem
      case "video"://OMIT<name,fid,md5,size,seconds>
        return {
          VideoSegment: {
            file: segment.file,
            url: undefined//TODO
          }
        }
      //LocationElem
      case "location"://OMIT<id>
        return {
          lat: segment.lat,
          lon: segment.lon,
          title: segment.name,
          content: segment.address
        }
      //ShareElem
      case "share":
        return {
          ShareSegment: {
            url: segment.url,
            title: segment.title,
            content: segment.content,
            image: segment.image
          }
        }
      //JsonElem
      case "json":
        return {
          JsonSegment: {
            data: segment.data
          }
        }
      //XmlElem
      case "xml"://OMIT<id>
        return {
          XmlSegment: {
            data: segment.data
          }
        }
      //PokeElem
      case "poke":
        return {
          PokeSegment: {
            type: segment.type,
            id: segment.id,
            name: segment.text
          }
        }
      //ReplyElem
      case "reply":
        return {
          ReplySegment: {
            id: segment.id,
          }
        }
      default:
        logger.warn(`[py-plugin][parse-message] 无法识别的消息:${segment}`)
    }
  }).filter(x => x)
}

async function parse_sender(sender) {
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

async function parse_reply(handler, flag) {
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

async function parse_anonymous(anonymous) {
  return anonymous && {
    id: anonymous.id,
    name: anonymous.name,
    flag: anonymous.flag
  }
}

async function call_back(data, client, type) {
  return new Promise(resolve => {
    data && client.match(data, err => {
      resolve(err && `[py-plugin][after-match-${type}] ${err.details}`)
    })
  })
}

export async function message_receiver(event, client) {
  let data
  switch (event.message_type) {
    case "private":
      data = {
        PrivateMessageEvent: {
          time: event.time,
          self_id: event.self_id,
          post_type: event.post_type,
          message_type: event.message_type,
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
        GroupMessageEvent: {
          time: event.time,
          self_id: event.self_id,
          post_type: event.post_type,
          message_type: event.message_type,
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
  return await call_back(data, client, "message")
}

export async function request_receiver(event, client) {
  let data
  switch (`${event.request_type}.${event.sub_type}`) {
    case "friend.add":
    case "friend.single":
      data = {
        FriendRequestEvent: {
          time: event.time,
          self_id: event.self_id,
          post_type: event.post_type,
          request_type: event.request_type,
          user_id: event.user_id,
          comment: event.comment,
          flag: event.flag
        }
      }
      break
    case "group.add":
      data = {
        GroupRequestEvent: {
          time: event.time,
          self_id: event.self_id,
          post_type: event.post_type,
          request_type: event.request_type,
          sub_type: event.sub_type,
          group_id: event.group_id,
          user_id: event.user_id,
          comment: event.comment,
          flag: event.flag
        }
      }
      break
    case "group.invite":
      data = {
        GroupRequestEvent: {
          time: event.time,
          self_id: event.self_id,
          post_type: event.post_type,
          request_type: event.request_type,
          sub_type: event.sub_type,
          group_id: event.group_id,
          user_id: event.user_id,
          flag: event.flag
        }
      }
      break
    default:
      return `[py-plugin][before-match-request] 未知的request类型`
  }
  return await call_back(data, client, "request")
}

export async function notice_receiver(event, client) {
  let data, time = Math.round(new Date().getTime() / 1000)
  //OMIT<FriendDecreaseEvent,GroupTransferEvent>
  switch (`${event.notice_type}.${event.sub_type}`) {
    //FriendIncreaseEvent
    case "friend.increase":
      data = {
        FriendAddNoticeEvent: {
          time: time,//OVERWRITE
          self_id: event.self_id,
          post_type: event.post_type,
          notice_type: "friend_add",//OVERWRITE
          user_id: event.user_id
        }
      }
      break
    //FriendDecreaseEvent
    case "friend.recall"://OMIT<operator_id,seq,rand,time>
      data = {
        FriendRecallNoticeEvent: {
          time: time,//OVERWRITE
          self_id: event.self_id,
          post_type: event.post_type,
          notice_type: "friend_add",//OVERWRITE
          user_id: event.user_id,
          message_id: event.message_id
        }
      }
      break
    //FriendPokeEvent
    case "friend.poke"://OMIT<operator_id,action,suffix>
      data = {
        PokeNotifyEvent: {
          time: time,//OVERWRITE
          self_id: event.self_id,
          post_type: event.post_type,
          notice_type: "notify",//OVERWRITE
          sub_type: event.sub_type,
          user_id: event.self_id,
          target_id: event.self_id,
        }
      }
      break
    //MemberIncreaseEvent
    case "group.increase"://OMIT<nickname>
      data = {
        GroupIncreaseNoticeEvent: {
          time: time,//OVERWRITE
          self_id: event.self_id,
          post_type: event.post_type,
          notice_type: "group_increase",//OVERWRITE
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
        GroupDecreaseNoticeEvent: {
          time: time,//OVERWRITE
          self_id: event.self_id,
          post_type: event.post_type,
          notice_type: "group_decrease",//OVERWRITE
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
        GroupRecallNoticeEvent: {
          time: time,//OVERWRITE
          self_id: event.self_id,
          post_type: event.post_type,
          notice_type: "group_recall",//OVERWRITE
          user_id: event.user_id,
          group_id: event.group_id,
          operator_id: event.operator_id,
          message_id: event.message_id
        }
      }
      break
    //GroupPokeEvent
    case "group.poke"://OMIT<action,suffix>
      data = {
        PokeNotifyEvent: {
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
    //GroupAdminEvent
    case "group.admin":
      data = {
        GroupAdminNoticeEvent: {
          time: time,//OVERWRITE
          self_id: event.self_id,
          post_type: event.post_type,
          notice_type: "group_admin",//OVERWRITE
          sub_type: event.set ? "set" : "unset",
          user_id: event.user_id,
          group_id: event.group_id
        }
      }
      break
    //GroupMuteEvent
    case "group.ban"://OMIT<nickname>
      data = {
        GroupBanNoticeEvent: {
          time: time,//OVERWRITE
          self_id: event.self_id,
          post_type: event.post_type,
          notice_type: "group_ban",//OVERWRITE
          sub_type: event.duration ? "ban" : "lift_ban",
          user_id: event.user_id,
          group_id: event.group_id,
          operator_id: event.operator_id,
          duration: event.duration
        }
      }
      break
    default:
      return `[py-plugin][before-match-notice] 未知的notice类型`
  }

  return await call_back(data, client, "notice")
}
