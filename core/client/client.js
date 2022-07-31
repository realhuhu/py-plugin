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

export function UnaryToUnary({ file, func, load, onData }) {
  return client.UnaryToUnary({
    file: file,
    function: func,
    message: load?.message,
  }, (err, response) => {
    err = err || response.message.error;
    onData(err, response);
  });
}

export function StreamToUnary({ file, func, onInit, onData }) {
  let call = client.StreamToUnary((err, response) => {
    err = err || response.message.error;
    onData(err, response);
  });

  call.write({
    file: file,
    function: func,
  });

  if (onInit) {
    onInit();
  }

  call.send = (load) => {
    call.write({
      message: load?.message,
    });
  };

  return call;
}

export function UnaryToStream({ file, func, load, onData, onEnd }) {
  let call = client.UnaryToStream({
    file: file,
    function: func,
    message: load?.message,
  });

  call.on("data", function(response) {
    onData(response.message.error, response);
  });

  if (onEnd) {
    call.on("end", function(response) {
      onData(response.message.error, response);
    });
  }

  return call;
}

export function StreamToStream({ file, func, onInit, onData, onEnd }) {
  let call = client.StreamToStream();

  call.write({
    file: file,
    function: func,
  });

  if (onInit) {
    onInit();
  }

  call.on("data", function(response) {
    onData(response.message.error, response);
  });

  call.send = (load) => {
    call.write({
      message: load?.message,
    });
  };

  if (onEnd) {
    call.on("end", onEnd);
  }
  return call;
}

