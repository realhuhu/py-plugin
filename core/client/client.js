import grpc from "@grpc/grpc-js";
import protoLoader from "@grpc/proto-loader";
import path from "path";
import fs from "fs";

export const _path = path.join(process.cwd(), "plugins", "py-plugin");

export const config = JSON.parse(fs.readFileSync(path.join(_path, "config.json")).toString());

const packageDefinition = protoLoader.loadSync(path.join(_path, "core", "rpc", "type.proto"), {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
});

const protoDescriptor = grpc.loadPackageDefinition(packageDefinition);
const channel = protoDescriptor.hello;

export const client = new channel.Channel(`${config.host}:${config.port}`, grpc.credentials.createInsecure());

export function createEvent(e) {
  return {
    sender: {
      user_qq: e.user_id,
      nickname: e.nickname,
    },
    group_qq: e?.group?.group_id ?? 0,
  };
}

// client.UnaryToUnary({
//   event: {
//     sender: {
//       user_qq: 1234,
//       nickname: "233",
//     },
//     group_qq: 245,
//   },
//   message:{
//     hello:"qqq"
//   }
// }, function(err, response) {
//   if (err) {
//     console.error("Error: ", err);
//   } else {
//     console.log(response.message);
//   }
// });

// let call = client.UnaryToStream({
//   event: {
//     sender: {
//       user_qq: 1234,
//       nickname: "233",
//     },
//     group_qq: 245,
//   },
//   message: {
//     hello: "qqq",
//   },
// });
//
// call.on("data", function(response) {
//   console.log(response.message);
// });
//
// call.on("end", function() {
//   console.log("All Salaries have been paid");
// });

// let call = client.StreamToUnary(function(error, response) {
//   console.log(error);
//   console.log("Reports successfully generated for: ", response);
// });
// call.write({
//   event: {
//     sender: {
//       user_qq: 1234,
//       nickname: "233",
//     },
//     group_qq: 245,
//   },
//   message:{
//     hello:"qqq"
//   }
// });
// setTimeout(() => {
//   call.write({
//     event: {
//       sender: {
//         user_qq: 1234,
//         nickname: "233",
//       },
//       group_qq: 245,
//     },
//     message:{
//       hello:"abc"
//     }
//   });
//   call.end();
// }, 1000);

// let call = client.StreamToStream();
//
// call.on("data", function(response) {
//   console.log("客户端receive:", response);
// });
//
// call.on("end", function() {
//   console.log("服务器发送end,客户端关闭");
// });
//
// call.write({
//   event: {
//     sender: {
//       user_qq: 1234,
//       nickname: "233",
//     },
//     group_qq: 245,
//   },
//   message: {
//     hello: "qqq",
//   },
// });
// setTimeout(() => {
//   call.write({
//     event: {
//       sender: {
//         user_qq: 1234,
//         nickname: "233",
//       },
//       group_qq: 245,
//     },
//     message: {
//       hello: "abc",
//     },
//   });
//   call.end();
// }, 1000);
