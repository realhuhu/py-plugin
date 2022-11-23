import {segment} from "oicq";

const parse_member = member => {
  return {
    group_id: member.group_id,
    user_id: member.user_id,
    nickname: member.nickname,
    card: member.card,
    sex: member.sex,
    age: member.age,
    area: member.area,
    join_time: member.join_time,
    last_sent_time: member.last_sent_time,
    level: member.level.toString(),
    role: member.role,
    unfriendly: false,//OVERWRITE
    title_expire_time: member.title_expire_time,
    card_changeable: false,//OVERWRITE
    shut_up_timestamp: member.shutup_time,
  }
}

const parse_message = async message => {
  let serialized_message = []
  for (let message_segment of message) {
    let type = message_segment.segment
    let data = message_segment[type]
    switch (type) {
      case "AtSegment":
        serialized_message.push(segment.at(Number(data.qq)))
        break
      case "ImageSegment":
        serialized_message.push(segment.image(data.file || data.content))
        break
      case "RecordSegment":
        serialized_message.push(segment.record(data.file || data.content))
        break
      case "TextSegment":
        serialized_message.push(data.data)
        break
      case "VideoSegment":
        serialized_message.push(segment.video(data.file || data.content))
        break
    }
  }
  return serialized_message
}

const resolve_request = async request => {
  let type = request.request
  let load = request[type]
  switch (type) {
    case "PrivateMessageRequest":
      return await Bot.pickFriend(load.user_id).sendMsg(await parse_message(load.message))
    case "GroupMessageRequest":
      return await Bot.pickGroup(load.group_id).sendMsg(await parse_message(load.message))
    case "DeleteMsgRequest":
      load = load.message_id.split("|")
      if (load[0] === "group") {
        return await Bot.pickGroup(Number(load[1])).recallMsg(load[2])
      } else {
        return await Bot.pickFriend(Number(load[1])).recallMsg(load[2])
      }
    case "GetGroupMemberInfoRequest":
      return await Bot.pickMember(load.group_id, load.user_id).renew()
    case "GetGroupMemberListRequest":
      return await Bot.pickGroup(load.group_id).getMemberMap()
    case "SendPrivateForwardMsgRequest":
      let private_forward_message = []
      for (let i of load.message) {
        private_forward_message.push({
          user_id: 2661467107,
          nickname: i.name,
          message: await parse_message(i.content)
        })
      }
      return await Bot.pickFriend(load.user_id).sendMsg(segment.xml((await Bot.pickFriend(load.user_id).makeForwardMsg(private_forward_message)).data))
    case "SendGroupForwardMsgRequest":
      let group_forward_message = []
      for (let i of load.message) {
        group_forward_message.push({
          user_id: Bot.uin,
          nickname: i.name,
          message: await parse_message(i.content)
        })
      }
      return await Bot.pickGroup(load.group_id).sendMsg(segment.xml((await Bot.pickGroup(load.group_id).makeForwardMsg(group_forward_message)).data))
  }
}

const create_response = async (request, raw) => {
  let type = request.request
  let load = request[type]
  switch (type) {
    case "PrivateMessageRequest":
      return {
        PrivateMessageResult: {
          message_id: `private|${load.user_id}|${raw.message_id}`
        }
      }
    case "GroupMessageRequest":
      return {
        GroupMessageRequest: {
          message_id: `group|${load.group_id}|${raw.message_id}`
        }
      }
    case "DeleteMsgRequest":
      return {
        DeleteMsgResult: {}
      }
    case "GetGroupMemberInfoRequest":
      return {
        GetGroupMemberInfoResult: parse_member(raw)
      }
    case "GetGroupMemberListRequest":
      return {
        GetGroupMemberListResult: {
          member_list: [...raw.values()].map(x => parse_member(x))
        }
      }
    case "SendPrivateForwardMsgRequest":
      return {
        SendPrivateForwardMsgResult: {
          message_id: `private|${load.user_id}|${raw.message_id}`
        }
      }
    case "SendGroupForwardMsgRequest":
      return {
        SendGroupForwardMsgResult: {
          message_id: `group|${load.group_id}|${raw.message_id}`
        }
      }
  }
}

export const channel_test = async client => new Promise(resolve => {
  client.option({code: 100}, (err, response) => {
    resolve(err && err.details)
  })
})

export const channel_setup = async client => {
  const call = client.callBack()
  call.on("data", request => {
    resolve_request(request).then(raw => {
      return create_response(request, raw)
    }).then(response => {
      call.write(response)
    })
  });
  call.on("error", err => {
    logger.error(err.details);
    if (err.details) {
      logger.error("py服务器连接丢失，5秒后尝试重连");
      setTimeout(() => {
        channel_setup(client)
      }, 5000)
    }
  });
  call.on('end', function () {
    console.log('on end');
  });

  call.write({Empty: {}})
}

export const setup = async client => {
  let err = await channel_test(client)
  if (err) {
    return err
  } else {
    logger.info("py服务器连接成功")
  }
  await channel_setup(client)
}
