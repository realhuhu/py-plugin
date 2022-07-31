import { exec } from "child_process";
import fs from "fs";
import path from "path";

import { _path, config } from "./core/client/client.js";

exec(`${config.pythonPath} ${path.join(_path, "main.py")}`, function(err, stdout, stderr) {
  if (err) throw err;
});

let files = fs.readdirSync(path.join(_path, "apps", "js"));
let apps = [];

for (let file of files) {
  let tmp = await import(`./apps/js/${file}`);
  if (tmp.rule) {
    apps.push(tmp);
  }
}

export const rule = {
  proxy: {
    reg: "noCheck",
    priority: 800,
    describe: "proxy",
  },
};

export async function proxy(e) {
  for (let app of apps) {
    for (let key of Object.keys(app.rule)) {
      if (new RegExp(app.rule[key].reg).test(e.msg) || app.rule[key].reg === "noCheck") {
        try {
          if (app[key](e)) return true;
        } catch (e) {
          console.log(`py-plugin:${app[key]} error:${e}`);
        }
      }
    }
  }
}
