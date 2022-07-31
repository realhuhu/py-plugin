import { client } from "../../core/client/client.js";


export const rule = {
  startAdd: {
    reg: "^#开始计算",
    priority: 800,
    describe: "开始累加计算",
  },
  addNum: {
    reg: "^加[0-9]+",
    priority: 800,
    describe: "开始累加",
  },
  showRes: {
    reg: "^#求解",
    priority: 800,
    describe: "返回结果",
  },
};

let current = {};

export async function startAdd(e) {
  if (e.isGroup) {
    return;
  }

  if (current[e.user_id]) {
    e.reply("计算进行中!");
    return;
  }

  current[e.user_id] = client.StreamToUnary((error, response) => {
    if (error) {
      console.log(error);
    } else {
      e.reply(response?.message?.res ?? "已结束");
    }
  });

  e.reply("请依次输入 （加+数字）,如 加3 加4等");
}

export async function addNum(e) {
  let call = current[e.user_id];

  if (!call) {
    e.reply("计算未开始!");
    return;
  }

  call.write({
    file: "example_StreamToUnary",
    function: "add",
    message: {
      num: e.msg.replace("加", ""),
    },
  });
}


export async function showRes(e) {
  let call = current[e.user_id];

  if (!call) {
    e.reply("计算未开始!");
    return;
  }

  call.end();
  delete current[e.user_id];
}