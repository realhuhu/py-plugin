import { client } from "../../core/client/client.js";


export const rule = {
  who: {
    reg: "^#你是谁",
    priority: 800,
    describe: "你是谁",
  },
};

export async function who(e) {
  let call = client.UnaryToStream({
    file: "example_UnaryToStream",
    function: "who",
  });

  call.on("data", function(response) {
    e.reply(response.message.res);
  });
}