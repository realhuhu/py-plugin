import grpc from "@grpc/grpc-js";
import protoLoader from "@grpc/proto-loader";
import path from "path";
import fs from "fs";
import { imageUrlToBuffer } from "../util/transform.js";


global.py_plugin_path = path.join(process.cwd(), "plugins", "py-plugin");

if (!fs.existsSync(path.join(global.py_plugin_path, "config.json"))) {
  fs.copyFileSync(path.join(global.py_plugin_path, "config_default.json"), path.join(global.py_plugin_path, "config.json"));
} else {
  if (!JSON.parse(fs.readFileSync(path.join(global.py_plugin_path, "config.json")).toString()).local) {
    fs.unlinkSync(path.join(global.py_plugin_path, "config.json"));
    fs.copyFileSync(path.join(global.py_plugin_path, "config_default.json"), path.join(global.py_plugin_path, "config.json"));
    console.log("py-plugin版本更新，已清空config.json，请重新配置");
  }
}

export const config = JSON.parse(fs.readFileSync(path.join(global.py_plugin_path, "config.json")).toString());


const packageDefinition = protoLoader.loadSync(path.join(global.py_plugin_path, "core", "rpc", "type.proto"), {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
});

const protoDescriptor = grpc.loadPackageDefinition(packageDefinition);
const channel = protoDescriptor.hello;

export const localClient = config.useRemote === true ? null : new channel.Channel(`${config.local.host}:${config.local.port}`, grpc.credentials.createInsecure(), {
  "grpc.max_receive_message_length": 1024 * 1024 * 128,
  "grpc.max_send_message_length": 1024 * 1024 * 128,
});

export const RemoteClient = typeof config.useRemote !== "object" || !config.useRemote.length ? null : new channel.Channel(`${config.remote.host}:${config.remote.port}`, grpc.credentials.createInsecure(), {
  "grpc.max_receive_message_length": 1024 * 1024 * 128,
  "grpc.max_send_message_length": 1024 * 1024 * 128,
});

function send(call) {
  return params => {
    call.write(params);
  };
}

export function createClient(_package, _handler) {
  if (!localClient || !RemoteClient) {
    return localClient || RemoteClient;
  } else {
    return config.useRemote.includes(`${_package}.${_handler}`) ? RemoteClient : localClient;
  }

}

export function FrameToFrame({ _package, _handler, params, onData }) {
  let call = createClient(_package, _handler).FrameToFrame({
    package: _package,
    handler: _handler,
    ...params,
  }, (err, response) => {
    let error = err || response.error;
    onData(error, response);
  });

  call.on("error", error => {
    console.log(`${_package} ${_handler}出错了\n${error.details}`);
  });

  return call;
}

export function StreamToFrame({ _package, _handler, onInit, onData }) {
  let call = createClient(_package, _handler).StreamToFrame((err, response) => {
    let error = err || response.error;
    onData(error, response);
  });

  call.write({
    package: _package,
    handler: _handler,
  });

  if (onInit) {
    onInit();
  }

  call.on("error", error => {
    console.log(`${_package} ${_handler}出错了\n${error.details}`);
  });

  call.send = send(call);

  return call;
}

export function FrameToStream({ _package, _handler, params, onData, onEnd }) {
  let call = createClient(_package, _handler).FrameToStream({
    package: _package,
    handler: _handler,
    ...params,
  });

  call.on("data", response => {
    onData(response.error, response);
  });

  call.on("error", error => {
    console.log(`${_package} ${_handler}出错了\n${error.details}`);
  });

  if (onEnd) call.on("end", onEnd);

  return call;
}

export function StreamToStream({ _package, _handler, onInit, onData, onEnd }) {
  let call = createClient(_package, _handler).StreamToStream();

  call.write({
    package: _package,
    handler: _handler,
  });

  if (onInit) {
    onInit();
  }

  call.on("data", (response) => {
    onData(response.error, response);
  });

  call.on("error", error => {
    console.log(`${_package} ${_handler}出错了\n${error.details}`);
  });

  call.send = send(call);

  if (onEnd) call.on("end", onEnd);

  return call;
}


export async function createUser(user) {
  return {
    qq: user.user_id.toString(),
    name: user.nickname,
    card: user.card,
    sex: user?.sex,
    age: user?.age?.toString(),
    area: user?.area,
    level: user?.level?.toString(),
    role: user?.role,
    title: user?.title,
  };
}

export async function createMessage(raw_message, is_quote = false) {
  let imageList = [];

  for (let val of raw_message.message) {
    if ("image" === val.type) {
      imageList.push(await imageUrlToBuffer(val.url));
    }
  }

  let message = {
    sender: await createUser(raw_message.sender),
    atList: raw_message.message.filter(x => x.type === "at").map(x => {
      return {
        qq: x.qq.toString(),
        name: x.text.replace("@", ""),
      };
    }),
    imageList: imageList,

  };

  if (is_quote) {
    message["msg"] = raw_message.raw_message;
  } else {
    message["msg"] = raw_message.msg;
    message["group"] = raw_message.isGroup ? {
      qq: raw_message.group_id.toString(),
      name: raw_message.group_name,
    } : null;
  }
  return message;
}

export async function createEvent(e) {

  let event = await createMessage(e);

  if (e.isGroup && e.source) {
    let source = (await e.group.getChatHistory(e.source.seq, 1)).pop();
    event["quote"] = await createMessage(source, true);
  }

  return event;
}
