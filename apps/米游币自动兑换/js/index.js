import { FrameToFrame, StreamToStream, createEvent } from "../../../core/client/client.js";

export const rule = {
  myb_add: {
    reg: "^#添加米游币任务$",
    priority: 700,
    describe: "添加米游币计划",
  },
  myb_listener: {
    reg: "noCheck",
    priority: 800,
    describe: "添加米游币计划",
  },
  myb_cancel_add: {
    reg: "^#取消添加米游币任务$",
    priority: 701,
    describe: "取消添加米游币任务",
  },
  myb_show: {
    reg: "^#我的米游币任务$",
    priority: 800,
    describe: "我的米游币任务",
  },
  myb_cancel: {
    reg: "^#删除米游币任务[0-9]+",
    priority: 800,
    describe: "取消米游币任务",
  },
};

let current = {};

export async function myb_add(e) {
  if (!e.isPrivate) return true;


  let call = current[e.sender.user_id];

  if (call) {
    e.reply("正在进行中，请按提示输入信息，或者输入 #取消添加米游币任务 结束添加");
  } else {
    current[e.sender.user_id] = StreamToStream({
      _package: "myb",
      _handler: "myb_add",
      onData(error, response) {
        if (error) {
          console.log(error.stack);
        } else {
          e.reply(response.message);
          if (response.messageDict.stop) {
            current[e.sender.user_id].end();
            delete current[e.sender.user_id];
          }
        }
      },
    });
  }

  return true;
}

export async function myb_cancel_add(e) {
  let call = current[e.sender.user_id];
  if (call) {
    delete current[e.sender.user_id];
    e.reply("已取消");
  } else {
    e.reply("没有正在进行的任务");
  }
  return true;
}

export async function myb_listener(e) {
  let call = current[e.sender.user_id];
  if (call) {
    call.send({ event: await createEvent(e) });
    return true;
  }
}

export async function myb_show(e) {
  FrameToFrame({
    _package: "myb",
    _handler: "myb_show",
    params: {
      event: await createEvent(e),
    },
    onData(error, response) {
      if (error) {
        console.log(error.stack);
      } else {
        e.reply(response.message);
      }
    },
  });

  return true;
}

export async function myb_cancel(e) {
  FrameToFrame({
    _package: "myb",
    _handler: "myb_cancel",
    params: {
      event: await createEvent(e),
      message: e.msg.replace("#删除米游币任务", ""),
    },
    onData(error, response) {
      if (error) {
        console.log(error.stack);
      } else {
        e.reply(response.message);
      }
    },
  });

  return true;
}