import fs from "node:fs";
import YAML from 'yaml'
import path from "path";
import plugin from '../../lib/plugins/plugin.js'
import {create_client, setup_server, setup_client} from "./core/client/client.js";


global.py_plugin_path = path.join(process.cwd(), "plugins", "py-plugin");
if (!fs.existsSync(path.join(py_plugin_path, "config.yaml"))) {
  fs.copyFileSync(path.join(py_plugin_path, "config_default.yaml"), path.join(py_plugin_path, "config.yaml"));
}
global.py_plugin_config = YAML.parse(fs.readFileSync(path.join(global.py_plugin_path, "config.yaml"), 'utf8'))
global.py_plugin_client = create_client(py_plugin_config)

setup_server().then(() => {
  setup_client()
})

export class PyPlugin extends plugin {
  constructor() {
    super({
      name: 'py-plugin',
      dsc: 'py-plugin',
      event: 'message',
      priority: 5000,
      rule: [
        {
          reg: "#?(n)?py帮助",
          fnc: 'py_help'
        },
        {
          reg: "#?(n)?py(下载|卸载|启用|禁用)插件",
          fnc: 'py_manage'
        },
      ]
    })

  }

  async py_help(e) {
    e.reply("还没写")
  }

  async py_manage(e) {
    e.reply("还没写")
  }

}





