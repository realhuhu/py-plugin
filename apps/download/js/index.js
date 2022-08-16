import { render } from "../../../core/util/render.js";
import fetch from "node-fetch";
import { exec } from "child_process";
import path from "path";
import fs from "fs";
import _ from "lodash";

let api = "https://api.miao.seutools.com/";


export const rule = {
  py_query_app: {
    reg: "^#py查询插件",
    priority: 700,
    describe: "查询支持的所有插件",
  },
  py_download_app: {
    reg: "^#py下载插件",
    priority: 700,
    describe: "下载新插件",
  },
  py_update_app: {
    reg: "^#py更新插件",
    priority: 700,
    describe: "更新已安装的插件",
  },
  py_delete_app: {
    reg: "^#py删除插件",
    priority: 700,
    describe: "删除已安装的插件",
  },
};

function pip(requirement) {
  return new Promise((resolve, reject) => {
    exec(`poetry run pip install ${requirement.replace(".", " ")}`, { cwd: global.py_plugin_path }, ((error, stdout, stderr) => {
      if (error) {
        console.log(stderr);
        reject(error);
      } else {
        resolve("pip install失败，请查看控制台");
      }
    }));
  });
}

function clone(url) {
  return new Promise((resolve, reject) => {
    exec(`git clone ${url}`, { cwd: path.join(global.py_plugin_path, "apps") }, ((error, stdout, stderr) => {
      if (error) {
        console.log(stderr);
        console.log(error);
        reject("git clone失败，请查看控制台");
      } else {
        resolve();
      }
    }));
  });
}

function pull(dir) {
  return new Promise((resolve, reject) => {
    exec(`git pull`, { cwd: path.join(global.py_plugin_path, "apps", dir) }, ((error, stdout, stderr) => {
      if (error) {
        console.log(stderr);
        console.log(error);
        reject("git pull失败，请查看控制台");
      } else {
        resolve();
      }
    }));
  });
}

function unlink(url) {
  let files;
  files = fs.readdirSync(url);   //返回文件和子目录的数组
  files.forEach(function(file, index) {
    let curPath = path.join(url, file);

    if (fs.statSync(curPath).isDirectory()) { //同步读取文件夹文件，如果是文件夹，则函数回调
      unlink(curPath);
    } else {
      fs.unlinkSync(curPath);    //是指定文件，则删除
    }
  });

  fs.rmdirSync(url); //清除文件夹
}


export async function py_query_app(e) {
  if (!e.isMaster) return true;

  let apps = await fetch(api + "app").then(res => res.json());
  for (let app of apps) {
    let installed = _.find(global.py_plugin_apps, x => x.group === app.name);
    if (installed && installed.version < app.version.split(".")) {
      app.update = true;
    }
    if (!installed) {
      app.not_installed = true;
    }
  }
  let img = await render("download", "py_query_app", { apps: apps });
  e.reply(img);
  return true;
}

export async function py_download_app(e) {
  if (!e.isMaster) return true;

  let app = e.msg.replace("#py下载插件", "");
  let res = await fetch(api + `app?search=${app}`).then(res => res.json());
  if (res.length === 0) {
    e.reply("没有找到该插件");
    return true;
  }

  if (_.find(global.py_plugin_apps, x => x.group === app)) {
    e.reply("已安装该插件");
    return true;
  }

  res = res[0];
  if (res.requirement) {
    e.reply("安装依赖中");
    pip(res.requirement).then(() => {
      e.reply(`下载插件 ${res.name} 中`);
      return clone(res.url);
    }).then(() => {
      e.reply(`更新完成，版本v${res.version}，请重启云崽`);
    }).catch(error => {
      e.reply(error);
    });
  } else {
    e.reply(`下载插件 ${res.name} 中`);
    clone(res.url).then(() => {
      e.reply(`下载完成，请重启云崽`);
    }).catch(error => {
      e.reply(error);
    });
  }
  return true;
}

export async function py_update_app(e) {
  if (!e.isMaster) return true;

  let app = e.msg.replace("#py更新插件", "");

  let res = await fetch(api + `app?search=${app}`).then(res => res.json());

  if (res.length === 0) {
    e.reply("没有找到该插件");
    return true;
  }

  res = res[0];
  let installed = _.find(global.py_plugin_apps, x => x.group === res.name);
  let dir = installed.dir;

  if (!fs.existsSync(path.join(global.py_plugin_path, "apps", dir))) {
    e.reply("你还没有安装该插件");
    return true;
  }

  if (res.version.split(".") <= installed.version) {
    e.reply("已是最新版");
    return true;
  }


  if (res.requirement) {
    e.reply("安装依赖中");

    pip(res.requirement).then(() => {
      e.reply(`更新插件 ${res.name} 中`);
      return pull(dir);
    }).then(() => {
      e.reply(`更新完成，版本v${res.version}，请重启云崽`);
    }).catch(error => {
      e.reply(error);
    });
  } else {

    e.reply(`更新插件 ${res.name} 中`);
    pull(dir).then(() => {
      e.reply(`更新完成，版本v${res.version}，请重启云崽`);
    }).catch(error => {
      e.reply(error);
    });
  }
  return true;
}

export async function py_delete_app(e) {
  if (!e.isMaster) return true;

  let app = e.msg.replace("#py删除插件", "");
  app = _.find(global.py_plugin_apps, x => x.group === app);

  if (!app) {
    e.reply("你还没有安装该插件");
    return true;
  }

  if (!fs.existsSync(path.join(global.py_plugin_path, "apps", app.dir))) {
    e.reply("你还没有安装该插件");
    return true;
  }

  unlink(path.join(global.py_plugin_path, "apps", app.dir));
  e.reply("已卸载，请重启云崽");
  return true;
}