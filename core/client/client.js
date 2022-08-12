import grpc from "@grpc/grpc-js";
import protoLoader from "@grpc/proto-loader";
import path from "path";
import fs from "fs";
import { imageUrlToBuffer } from "../util/transform.js";
import _ from "lodash";

export const __version__ = [1, 0, 1];

export const _path = path.join(process.cwd(), "plugins", "py-plugin");

let _config;

try {
  _config = JSON.parse(fs.readFileSync(path.join(_path, "config.json")).toString());
} catch (e) {
  _config = JSON.parse(fs.readFileSync(path.join(_path, "config_default.json")).toString());
}

export const config = _config;

if(config.host==="127.0.0.1"){
  config.port = _.random(50000, 50100);
}else {
  config.port = 50051;
}


const packageDefinition = protoLoader.loadSync(path.join(_path, "core", "rpc", "type.proto"), {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
});

const protoDescriptor = grpc.loadPackageDefinition(packageDefinition);
const channel = protoDescriptor.hello;

export const client = new channel.Channel(`${config.host}:${config.port}`, grpc.credentials.createInsecure(), {
  "grpc.max_receive_message_length": 1024 * 1024 * 128,
  "grpc.max_send_message_length": 1024 * 1024 * 128,
});

function send(call) {
  return params => {
    call.write(params);
  };
}


export function FrameToFrame({ _package, _handler, params, onData }) {
  let call = client.FrameToFrame({
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
  let call = client.StreamToFrame((err, response) => {
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
  let call = client.FrameToStream({
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
  let call = client.StreamToStream();

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

export async function createEvent(e) {
  let imageList = [];

  for (let val of e.message) {
    if ("image" === val.type) {
      imageList.push(await imageUrlToBuffer(val.url));
    }
  }

  return {
    msg: e.msg,
    sender: {
      qq: e.sender.user_id.toString(),
      name: e.sender.nickname,
    },
    group: e.isGroup && {
      qq: e.group_id.toString(),
      name: e.group_name,
    },
    atList: e.message.filter(x => x.type === "at").map(x => {
      return {
        qq: x.qq.toString(),
        name: x.text.replace("@", ""),
      };
    }),
    imageList: imageList,
  };
}

