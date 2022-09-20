import { spawn } from "child_process";
import fs from "fs";
import path from "path";
import _ from "lodash";
import { config, localClient, RemoteClient } from "./core/client/client.js";


if (config.useRemote !== true) {
  localClient.Option({ code: 1 }, function(err, response) {
    logger.info("python服务器启动中");
    const cmd = spawn(
      "poetry",
      ["run", "python", "main.py", "-grpc-host", config.local.host, "-grpc-port", config.local.port],
      {
        cwd: global.py_plugin_path,
        shell: false,
      },
    );

    cmd.stdout.on("data", data => {
      process.stdout.write(data);
      if (data.toString().includes("Python started")) {
        localClient.Option({ code: 100 }, function(err, response) {
          if (response.code === 100) {
            logger.info("python服务器启动成功");
          }
        });
      }
    });

    cmd.stderr.on("data", data => {
      process.stderr.write(data.toString());
    });

    cmd.stderr.on("end", () => {
      logger.warn("python服务器已关闭");
    });

    cmd.on("error", function(err) {
      logger.warn("python服务器启动失败");
      logger.warn(err);
    });
  });
}

if (RemoteClient) {
  RemoteClient.Option({ code: 100 }, function(err, response) {
    if (response && response.code === 100) {
      logger.info("成功连接远程python服务器");
    } else {
      logger.warn("无法连接远程python服务器");
    }
  });
}

let dirs = fs.readdirSync(path.join(global.py_plugin_path, "apps")).filter(x => !x.includes("__") && fs.statSync(path.join(global.py_plugin_path, "apps", x)).isDirectory());
global.py_plugin_dirs = dirs;
global.py_plugin_version = [1, 2, 0];
let apps = [];

for (let file of dirs) {
  try {
    let tmp = await import(`./apps/${file}/js/index.js`);
    if (tmp.rule) {
      for (let key of Object.keys(tmp.rule)) {
        apps.push({
          reg: tmp.rule[key].reg,
          describe: tmp.rule[key].describe,
          priority: tmp.rule[key].priority,
          handler: tmp[key],
          dir:file
        });
      }
    }
  } catch (e) {

  }
}

apps = _.sortBy(apps, app => app.priority);

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
        if (app.reg !== "noCheck") logger.info(`py-plugin:${app.handler.name}`);
        if (app.reg === "noCheck" && stop) logger.info(`py-plugin:${app.handler.name}`);
        if (stop === true) {
          return true;
        }
      } catch (e) {
        logger.warn(`py-plugin:${app.handler.name} error:${e}`);
      }
    }
  }
  return false;
}


export class Proxy {
  get name() {
    return this.e ? apps.filter(app => RegExp(app.reg).test(this.e.msg))?.[0].handler.name ?? "py-plugin" : "py-plugin"
  }
  event = "message";
  priority = 0;
  task = {};
  rule = [
    ...apps.filter(app => app.reg !== "noCheck").map(app => {
      return {
        reg: app.reg,
        fnc: app.handler.name,
      };
    }),
    {
      reg: ".*",
      fnc: "noCheck",
    },
  ];

}

for (let app of apps.filter(app => app.reg !== "noCheck")) {
  Proxy.prototype[app.handler.name] = async (e) => {
    return await app.handler(e) === true;
  };
}
Proxy.prototype.noCheck = async (e) => {
  for (let app of apps.filter(app => app.reg === "noCheck")) {
    let stop = await app.handler(e);
    if (stop) {
      logger.info(app.handler.name);
      return true;
    }
  }
  return false;
};
logger.info(`python插件${global.py_plugin_version.join(".")}初始化~`);
