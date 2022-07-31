import { StreamToStream } from "../../core/client/client.js";


export const rule = {
  startGuessNum: {
    reg: "^#开始猜数字",
    priority: 800,
    describe: "开始猜数字游戏",
  },
  GuessNum: {
    reg: "^我猜[0-9]+",
    priority: 800,
    describe: "猜数",
  },
  stopGuessNum: {
    reg: "^#不猜了",
    priority: 800,
    describe: "结束",
  },
};
let current = {};

export async function startGuessNum(e) {
  if (!e.isGroup) {
    e.reply("只能在群聊中玩猜数游戏");
    return true;
  }

  if (current[e.group.group_id]) {
    e.reply("猜数游戏进行中");
    return true;
  }

  let call = StreamToStream({
    file: "example_StreamToStream",
    func: "guess",
    onData: (error, response) => {
      if (error) {
        console.log(error);
        e.reply("出错了!");
      } else {
        if (response.message.correct === "true") {
          e.reply("猜对了！");
          call.end();
          delete current[e.group.group_id];
        } else {
          e.reply(response.message.res);
        }
      }
    },
  });

  current[e.group.group_id] = call;
  e.reply("快来猜数吧，数字大于等于0且小于100！");

  return true;
}

export async function GuessNum(e) {
  if (!e.isGroup) {
    e.reply("只能在群聊中玩猜数游戏");
    return true;
  }

  let call = current[e.group.group_id];
  if (!call) {
    e.reply("猜数游戏未开始");
    return true;

  }

  call.send({
    message: {
      num: e.msg.replace("我猜", ""),
    },
  });

  return true;
}

export async function stopGuessNum(e) {
  if (!e.isGroup) {
    e.reply("只能在群聊中玩猜数游戏");
    return true;
  }

  let call = current[e.group.group_id];
  if (!call) {
    e.reply("猜数游戏未开始");
    return true;
  }

  call.end();
  delete current[e.group.group_id];
  e.reply("已结束");

  return true;
}