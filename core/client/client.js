import path from "path";
import grpc from "@grpc/grpc-js";
import iconv from 'iconv-lite'
import protoLoader from "@grpc/proto-loader";
import {spawn} from "child_process";
import {setup} from "../utils/channel.js";
import {message_receiver, notice_receiver, request_receiver} from "../utils/receiver.js";


export const create_client = config => {
  const packageDefinition = protoLoader.loadSync(path.join(py_plugin_path, "core", "rpc", "hola.proto"), {
    keepCase: true,
    longs: String,
    enums: String,
    defaults: true,
    oneofs: true,
    includeDirs: [
      process.cwd()
    ],
  });
  const protoDescriptor = grpc.loadPackageDefinition(packageDefinition);
  const channel = protoDescriptor.hola;
  return new channel.Channel(`${config.host || "127.0.0.1"}:${config.port || 50052}`, grpc.credentials.createInsecure(), {
    "grpc.max_receive_message_length": 1024 * 1024 * 128,
    "grpc.max_send_message_length": 1024 * 1024 * 128,
  });
}

export const setup_server = () => new Promise((resolve, reject) => {
  if (py_plugin_config.independent) {
    resolve()
  } else {
    py_plugin_client.option({code: 1}, function (err, response) {
      logger.info("python服务器启动中");
      const cmd = spawn(
        "poetry",
        ["run", "python", "main.py"],
        {
          cwd: global.py_plugin_path,
          shell: false,
        },
      );

      cmd.stdout.on("data", data => {
        data = iconv.decode(data, py_plugin_config.encoding || "utf-8")
        process.stdout.write(data.toString());
        if (data.toString().includes("Py started")) {
          py_plugin_client.option({code: 100}, function (err, response) {
            if (response.code === "100") {
              resolve("python服务器启动成功")
            } else {
              reject(err || response)
            }
          });
        }
      });

      cmd.stderr.on("data", data => {
        process.stderr.write(iconv.decode(data, py_plugin_config.encoding || "utf-8"));
      });

      cmd.stderr.on("end", () => {
        logger.warn("python服务器已关闭");
      });

      cmd.on("error", err => {
        logger.warn("python服务器启动失败");
        logger.warn(iconv.decode(err, py_plugin_config.encoding || "utf-8"));
      });
    });
  }
})

export const setup_client = () => {
  setup(py_plugin_client).then(err => {
    if (err) logger.error(err)
    Bot.on("request", async event => {
      let err = await request_receiver(event, py_plugin_client)
      err && logger.warn(err)
    })

    Bot.on("message", async event => {
      let err = await message_receiver(event, py_plugin_client)
      err && logger.warn(err)
    })

    Bot.on("notice", async event => {
      let err = await notice_receiver(event, py_plugin_client)
      err && logger.warn(err)
    })
  })
}
