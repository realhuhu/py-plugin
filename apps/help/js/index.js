import fs from "fs";
import { render } from "../../../core/util/render.js";
import path from "path";
import _ from "lodash";

export const rule = {
  py_help: {
    reg: "#?(n)?py(命令|帮助|菜单|help|说明|功能|指令|使用说明)$",
    priority: 700,
    describe: "获取帮助列表",
  },
  py_help_detail: {
    reg: "^#.*帮助$",
    priority: 700,
    describe: "获取帮助详情",
  },
};
let apps = [];
let other = {
  group: "其它功能",
  priority: 100,
  skip: true,
  list: [],
};
for (let dir of global.py_plugin_dirs) {
  let dir_path = path.join(global.py_plugin_path, "apps", dir.toString(), "info.json");
  if (fs.existsSync(dir_path)) {
    let info = fs.readFileSync(dir_path).toString();
    info = JSON.parse(info);
    apps.push(info);
    if (!info.list) {
      other.list.push({
        title: info.group,
        desc: info.desc,
        detail: info.detail,
      });
    }
  }
}

apps.push(other);
apps = _.sortBy(apps, x => x.priority);
global.py_plugin_apps = apps;

export async function py_help(e) {
  let all = apps;
  if (!e.isMaster) {
    all = all.filter(x => !x.auth);
  }
  let img = await render("help", "py_help", { apps: all });
  e.reply(img);
  return true;
}

export async function py_help_detail(e) {
  let app_name = e.msg.match(/(?<=#).*?(?=帮助)/g)[0];

  let app = _.find(apps, x => x.group === app_name);

  if (!app) return false;


  if (!e.isMaster && app.auth) {
    e.reply("只有管理员能查看");
    return true;
  }

  let img = await render("help", "py_help_detail", { app });
  e.reply(img);
  return true;
}