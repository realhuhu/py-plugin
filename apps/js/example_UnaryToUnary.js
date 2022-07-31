import { UnaryToUnary } from "../../core/client/client.js";


export const rule = {
  upper: {
    reg: "^#upper",
    priority: 800,
    describe: "返回大写",
  },
  lower: {
    reg: "^#lower",
    priority: 800,
    describe: "返回小写",
  },
};

export async function upper(e) {
  UnaryToUnary({
    file: "example_UnaryToUnary",
    func: "upper",
    load: {
      message: {
        raw: e.msg.replace("#upper", ""),
      },
    },
    onData: (err, response) => {
      if (err) {
        e.reply("出错了!");
        console.error(err);
      } else {
        e.reply(response.message.upper);
      }
    },
  });
  return true;
}

export async function lower(e) {
  UnaryToUnary({
    file: "example_UnaryToUnary",
    func: "lower",
    load: {
      message: {
        raw: e.msg.replace("#lower", ""),
      },
    },
    onData: (err, response) => {
      if (err) {
        console.error(err);
        e.reply("出错了!");
      } else {
        e.reply(response.message.lower);
      }
    },
  });
  return true;
}