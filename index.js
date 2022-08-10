import { exec } from "child_process";
import fs from "fs";
import path from "path";
import _ from "lodash";
import { _path, config, __version__ } from "./core/client/client.js";

if (config.host === "127.0.0.1") {
  exec(`poetry run python main.py`, { cwd: _path }, function(err, stdout, stderr) {
    if (err) throw err;
  });
}

let files = fs.readdirSync(path.join(_path, "apps", "js")).filter(x => x.endsWith(".js"));
let apps = [];

for (let file of files) {
  let tmp = await import(`./apps/js/${file}`);
  if (tmp.rule) {
    for (let key of Object.keys(tmp.rule)) {
      apps.push({
        reg: tmp.rule[key].reg,
        describe: tmp.rule[key].describe,
        priority: tmp.rule[key].priority,
        handler: tmp[key],
      });
    }
  }

  apps = _.sortBy(apps, app => app.priority);
}

export const rule = {
  proxy: {
    reg: "noCheck",
    priority: 0,
    describe: "proxy",
  },
};

export async function proxy(e) {
  for (let app of apps) {
    if (new RegExp(app.reg).test(e.msg) || app.reg === "noCheck") {
      try {
        let stop = await app.handler(e);
        if (app.reg !== "noCheck") console.log(`py-plugin:${app.handler.name}`);
        if (app.reg === "noCheck" && stop) console.log(`py-plugin:${app.handler.name}`);
        if (stop) return true;
      } catch (e) {
        console.log(`py-plugin:${app[key].name} error:${e}`);
      }
    }
  }
}


export class Proxy {
  name = "py-plugin";
  event = "message";
  priority = 0;
  task = {};
  rule = [{ reg: ".*", fnc: "v3_proxy" }];
  v3_proxy = proxy;
}

console.log(`python插件${__version__.join(".")}初始化~`);