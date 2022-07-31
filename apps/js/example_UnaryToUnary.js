import { client } from "../../core/client/client.js";


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
  client.UnaryToUnary({
    file: "example_UnaryToUnary",
    function: "upper",
    message: {
      raw: e.msg.replace("#upper", ""),
    },
  }, (err, response) => {
    if (err) {
      console.error("Error: ", err);
    } else {
      e.reply(response.message.upper);
    }
  });
}

export async function lower(e) {
  client.UnaryToUnary({
    file: "example_UnaryToUnary",
    function: "lower",
    message: {
      raw: e.msg.replace("#lower", ""),
    },
  }, (err, response) => {
    if (err) {
      console.error("Error: ", err);
    } else {
      e.reply(response.message.lower);
    }
  });
}