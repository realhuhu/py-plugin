import { UnaryToStream } from "../../core/client/client.js";


export const rule = {
  who: {
    reg: "^#你是谁",
    priority: 800,
    describe: "你是谁",
  },
};

export async function who(e) {
  UnaryToStream({
      file: "example_UnaryToStream",
      func: "who",
      onData: (error, response) => {
        if (error) {
          console.log(error);
          e.reply("出错了!");
        } else {
          e.reply(response.message.res);
        }
      },
    },
  );

  return true;
}