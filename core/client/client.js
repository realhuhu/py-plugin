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

function send(call) {
  return load => {
    call.write({
      message: load?.message,
    });
  };
}


export function UnaryToUnary({ file, func, load, onData }) {
  return client.UnaryToUnary({
    file: file,
    function: func,
    message: load?.message,
  }, (err, response) => {
    let error = err || response.error;
    onData(error, response);
  });
}

export function StreamToUnary({ file, func, onInit, onData }) {
  let call = client.StreamToUnary((err, response) => {
    let error = err || response.error;
    onData(error, response);
  });

  call.write({
    file: file,
    function: func,
  });

  if (onInit) {
    onInit();
  }

  call.send = send(call);

  return call;
}

export function UnaryToStream({ file, func, load, onData, onEnd }) {
  let call = client.UnaryToStream({
    file: file,
    function: func,
    message: load?.message,
  });

  call.on("data", function(response) {
    onData(response.error, response);
  });

  if (onEnd) call.on("end", onEnd);

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

  call.on("data", (response) => {
    onData(response.error, response);
  });

  call.send = send(call);

  if (onEnd) call.on("end", onEnd);

  return call;
}

