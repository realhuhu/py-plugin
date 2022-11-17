import {segment} from "oicq";


const parse_message = async message => {
  let serialized_message = []
  for (let message_segment of message) {
    let type = message_segment.segment
    let data = message_segment[type]
    switch (type) {
      case "TextSegment":
        serialized_message.push(data.data)
        break
      case "ImageSegment":
        serialized_message.push(segment.image(data.file || data.content))
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

const create_response = async (type, raw) => {
  switch (type) {
    case "PrivateMessageRequest":
      return {
        PrivateMessageResult: {
          message_id: raw.message_id
        }
      }
    case "GroupMessageRequest":
      return {
        GroupMessageRequest: {
          message_id: raw.message_id
        }
      }
    case "SendPrivateForwardMsgRequest":
      return {
        SendPrivateForwardMsgResult: {
          message_id: raw.message_id
        }
      }
    case "SendGroupForwardMsgRequest":
      return {
        SendGroupForwardMsgResult: {
          message_id: raw.message_id
        }
      }
  }
}

export const channel_test = async (client) => new Promise(resolve => {
  client.option({code: 100}, (err, response) => {
    resolve(err && err.details)
  })
})

export const channel_setup = async (client) => {
  const call = client.callBack()
  call.on("data", request => {
    resolve_request(request).then(raw => {
      return create_response(request.request, raw)
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

  call.write({Empty: {}})
}

export const setup = async (client) => {
  let err = await channel_test(client)
  if (err) {
    return err
  } else {
    logger.info("py服务器连接成功")
  }
  await channel_setup(client)
}
