import fs from "node:fs";
import YAML from 'yaml'
import path from "path";
import plugin from '../../lib/plugins/plugin.js'
import {spawn} from "child_process";
import {create_client, setup_server, setup_client} from "./core/client/client.js";


global.py_plugin_path = path.join(process.cwd(), "plugins", "py-plugin");
if (!fs.existsSync(path.join(py_plugin_path, "config.yaml"))) {
  fs.copyFileSync(path.join(py_plugin_path, "config_default.yaml"), path.join(py_plugin_path, "config.yaml"));
}
global.py_plugin_config = YAML.parse(fs.readFileSync(path.join(global.py_plugin_path, "config.yaml"), 'utf8'))
global.py_plugin_client = create_client(py_plugin_config)

setup_server().then(msg => {
  logger.mark(msg)
  setup_client()
}).catch(err => {
  logger.error(err)
})

// export class PyPlugin extends plugin {
//   constructor() {
//     super({
//       name: 'py-plugin',
//       dsc: 'py-plugin',
//       event: 'message',
//       priority: 5000,
//       rule: [
//         {
//           reg: "#?(n)?py帮助",
//           fnc: 'py_help'
//         },
//         {
//           reg: "#?(n)?py(下载|卸载|启用|禁用)插件.*",
//           fnc: 'py_manage'
//         },
//       ]
//     })
//
//   }
//
//   async py_help(e) {
//
//     e.reply("还没写")
//   }
//
//   async py_manage(e) {
//     if (!e.isMaster) return
//     let cfg = py_plugin_config
//     let plugin = e.msg.replace(/#?(n)?py(下载|卸载|启用|禁用)插件/, "")
//
//     if (e.msg.indexOf("下载") !== -1) {
//       e.reply(`下载中:${plugin}`)
//       let err = await this.poetry_run("pip", "install", plugin)
//       if (err) {
//         logger.error(err)
//         e.reply("出错了，请查看控制台")
//         return
//       }
//       e.reply(`下载完成:${plugin}`)
//       cfg.plugins.push(plugin)
//     }
//
//     if (e.msg.indexOf("卸载") !== -1) {
//       if (fs.readdirSync(path.join(py_plugin_path, "plugins")).indexOf(plugin) !== -1) {
//         e.reply(`无法卸载:${plugin}，只能卸载通过pip安装和指令安装的插件`)
//         return
//       }
//       e.reply(`卸载中:${plugin}`)
//       let err = await this.poetry_run("pip", "uninstall", plugin)
//       if (err) {
//         logger.error(err)
//         e.reply("出错了，请查看控制台")
//         return
//       }
//       e.reply(`卸载完成:${plugin}`)
//       let index = cfg.plugins.indexOf(plugin)
//       if (index !== -1) {
//         cfg.plugins.splice(index, 1)
//       }
//     }
//
//     if (e.msg.indexOf("启用") !== -1) {
//       if (cfg.plugins.indexOf(plugin) !== -1) {
//         e.reply("该插件已启用!")
//         return
//       }
//       e.reply(`已启用:${plugin}`)
//       cfg.plugins.push(plugin)
//     }
//
//     if (e.msg.indexOf("禁用") !== -1) {
//       if (cfg.plugins.indexOf(plugin) === -1) {
//         e.reply("该插件未启用!")
//         return
//       }
//       e.reply(`已禁用:${plugin}`)
//       let index = cfg.plugins.indexOf(plugin)
//       if (index !== -1) {
//         cfg.plugins.splice(index, 1)
//       }
//     }
//
//     await this.save_cfg(cfg)
//     await setup_server()
//     e.reply(`已重启python服务器`)
//   }
//
//   async poetry_run(...args) {
//     return new Promise(resolve => {
//       const cmd = spawn(
//         "poetry",
//         ["run", ...args],
//         {
//           cwd: global.py_plugin_path,
//         },
//       );
//
//       cmd.on("exit", () => {
//         resolve()
//       })
//
//       cmd.on("error", resolve)
//     })
//   }
//
//   async save_cfg(data) {
//     return new Promise(resolve => {
//       let yamlStr = YAML.stringify(data);
//       fs.writeFile(path.join(py_plugin_path, "config.yaml"), yamlStr, () => {
//         resolve()
//       });
//     })
//   }
// }
