import path from "path";
import chalk from "chalk";
import grpc from "@grpc/grpc-js";
import iconv from 'iconv-lite'
import protoLoader from "@grpc/proto-loader";
import {spawn} from "child_process";
import {setup_channel} from "./channel.js";
import {request_receiver, message_receiver, notice_receiver} from "./receiver.js";

const py_logger = raw => {
  // try {
  //   let head = chalk.blue(raw.match(/\[.*?\]\[.*?\]/g)[0])
  //   let level = raw.match(/(?<=\[.*?\]\[.*?\])\[.*?\]/g)[0]
  //   switch (level) {
  //     case"[TRACE]":
  //       level = chalk.grey(level)
  //       break
  //     case"[DEBUG]":
  //       level = chalk.gray(level)
  //       break
  //     case"[SUCCESS]":
  //       level = chalk.green(level)
  //       break
  //     case"[WARNING]":
  //       level = chalk.yellow(level)
  //       break
  //     case"[ERROR]":
  //       level = chalk.red(level)
  //       break
  //     case"[CRITICAL]":
  //       level = chalk.bgRed(level)
  //       break
  //   }
  //   let name = chalk.yellow(raw.match(/(?<=\[.*?\]\[.*?\]\[.*?\] )\[.*?\]/g)[0])
  //   let message = raw.match(/(?<=\[.*?\]\[.*?\]\[.*?\] \[.*?\]).*/g)[0]
  //   console.log(head + level, name, message);
  // } catch {
  //   console.log(raw);
  // }
  process.stdout.write(raw);
}
export const create_client = config => {
  const packageDefinition = protoLoader.loadSync(path.join(py_plugin_path, "yunzai_nonebot", "rpc", "hola.proto"), {
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
  return new channel.Pipe(`${config.host || "127.0.0.1"}:${config.port || 50052}`, grpc.credentials.createInsecure(), {
    "grpc.max_receive_message_length": 1024 * 1024 * 128,
    "grpc.max_send_message_length": 1024 * 1024 * 128,
  });
}

export const setup_server = () => new Promise((resolve, reject) => {
  if (py_plugin_config.independent || py_plugin_config.host !== "127.0.0.1") {
    resolve("[py-plugin] 连接服务器中，请确保Py服务器已启动")
  } else {
    py_plugin_client.Option({code: 1}, function (err, response) {
      let encoding = py_plugin_config.encoding || (process.platform === "win32" ? "gbk" : "utf-8")
      logger.info("[py-plugin] python服务器启动中");
      const cmd = spawn(
        "poetry",
        ["run", "python", "main.py"],
        {
          cwd: py_plugin_path,
          shell: false,
        },
      );

      cmd.stdout.on("data", data => {
        py_logger(iconv.decode(data, encoding));
        if (data.toString().includes("Py started")) {
          py_plugin_client.Option({code: 100}, function (err, response) {
            response && response.code === "100" ? resolve("[py-plugin] python服务器启动成功") : reject(err || response)
          });
        }
      });

      cmd.stderr.on("data", data => {
        py_logger(iconv.decode(data, encoding));
      });

      cmd.stderr.on("end", () => {
        logger.warn("[py-plugin] python服务器已关闭");
      });

      cmd.on("error", err => {
        logger.warn("[py-plugin] python服务器启动失败");
        logger.warn(err);
      });
    });
  }
})

export const setup_client = (ignore, retry) => {
  setup_channel(py_plugin_client, ignore, retry).then(channel => {
    Bot.on("request", event => request_receiver(channel, event))
    Bot.on("message", event => message_receiver(channel, event))
    Bot.on("notice", event => notice_receiver(channel, event))
  }).catch(err => {
    logger.error(err)
  })
}
