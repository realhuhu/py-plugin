import fs from "node:fs";
import YAML from 'yaml'
import path from "path";
import plugin from '../../lib/plugins/plugin.js'
import {exec} from "child_process";
import {create_client, setup_server, setup_client} from "./core/client/client.js";


global.py_plugin_path = path.join(process.cwd(), "plugins", "py-plugin");
if (!fs.existsSync(path.join(py_plugin_path, "config.yaml"))) {
  fs.copyFileSync(path.join(py_plugin_path, "config_default.yaml"), path.join(py_plugin_path, "config.yaml"));
}
global.py_plugin_config = YAML.parse(fs.readFileSync(path.join(global.py_plugin_path, "config.yaml"), 'utf8'))
py_plugin_config.plugins = py_plugin_config.plugins || []
global.py_plugin_client = create_client(py_plugin_config)

setup_server().then(msg => {
  logger.mark(msg)
  setup_client()
}).catch(err => {
  logger.error(err)
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
          reg: "#?n?py帮助",
          fnc: 'py_help'
        },
        {
          reg: "#?n?py(下载|卸载|启用|禁用|更新|全部|更新全部)插件.*",
          fnc: 'py_manage'
        },
        {
          reg: "#?n?py(强制)?重启",
          fnc: 'py_restart'
        },
        {
          reg: "#?n?py(查看|修改)配置.*",
          fnc: 'py_modify'
        },
      ]
    })

  }

  async py_help(e) {
    if (!e.isMaster) return
    e.reply("py下载|卸载|启用|禁用|更新插件+插件名\npy更新全部插件\npy全部插件\npy重启\npy查看|修改配置")
  }

  async py_manage(e) {
    if (!e.isMaster) return
    let command = e.msg.match(/(?<=#?n?py)(下载|卸载|启用|禁用|更新全部|更新|全部)/g)[0]
    let plugin = e.msg.replace(/#?(n)?py(下载|卸载|启用|禁用|更新|全部|更新全部)插件/, "")
    let err, index
    console.log(command, plugin)
    switch (command) {
      case "下载":
        e.reply(`下载中:${plugin}`)
        err = await this.poetry_run("pip", "install", plugin)
        if (err) {
          e.reply(`出错了:${err}`)
          return
        }
        e.reply(`下载完成:${plugin}`)
        py_plugin_config.plugins.push(plugin)
        break
      case "卸载":
        if (fs.readdirSync(path.join(py_plugin_path, "plugins")).indexOf(plugin) !== -1) {
          e.reply(`无法卸载:${plugin}，只能卸载通过pip安装和指令安装的插件`)
          return
        }
        e.reply(`卸载中:${plugin}`)
        err = await this.poetry_run("pip", "uninstall", plugin, "-y")
        if (err) {
          e.reply(`出错了:${err}`)
          return
        }
        e.reply(`卸载完成:${plugin}`)
        index = py_plugin_config.plugins.indexOf(plugin)
        if (index !== -1) {
          py_plugin_config.plugins.splice(index, 1)
        }
        break
      case "启用":
        if (py_plugin_config.plugins.indexOf(plugin) !== -1) {
          e.reply("该插件已启用!")
          return
        }
        e.reply(`已启用:${plugin}`)
        py_plugin_config.plugins.push(plugin)
        break
      case "禁用":
        if (py_plugin_config.plugins.indexOf(plugin) === -1) {
          e.reply("该插件未启用!")
          return
        }
        e.reply(`已禁用:${plugin}`)
        index = py_plugin_config.plugins.indexOf(plugin)
        if (index !== -1) {
          py_plugin_config.plugins.splice(index, 1)
        }
        break
      case "更新":
        e.reply(`更新中:${plugin}`)
        err = await this.poetry_run("pip", "install", "--upgrade", plugin)
        if (err) {
          e.reply(`出错了:${err}`)
          return
        }
        e.reply(`更新完成:${plugin}`)
        py_plugin_config.plugins.push(plugin)
        break
      case "全部":
        e.reply(`已加载插件:\n${py_plugin_config.plugins.join("\n")}`)
        return
      case "更新全部":
        e.reply(`更新全部插件:\n${py_plugin_config.plugins.join("\n")}`)
        let result = await Promise.all(py_plugin_config.plugins.map(plugin => new Promise(resolve => {
          this.poetry_run("pip", "install", "--upgrade", plugin).then(err => resolve({plugin, err}))
        })))

        let msg = `更新完成:\n${result.filter(x => !x.err).map(x => x.plugin).join("\n")}`
        if (result.filter(x => x.err).length) {
          msg += `\n\n更新失败:\n${result.filter(x => x.err).map(x => `[${x.plugin}]: ${x.err}`).join("\n")}`
        }
        e.reply(msg)
        return
    }
    py_plugin_config.plugins = [...new Set(py_plugin_config.plugins)]
    await this.save_cfg(py_plugin_config)
    await this.py_restart(e)
  }

  async py_restart(e) {
    if (!e.isMaster) return
    setup_server().then(() => {
      e.reply("已重启python服务器")
    }).catch(err => {
      e.reply("重启失败，请查看控制台")
      logger.warn(err)
    })
  }

  async py_modify(e) {
    if (!e.isMaster) return
    let command = e.msg.match(/(?<=#?n?py)(查看|修改)/g)[0]

    switch (command) {
      case "查看":
        e.reply(YAML.stringify(py_plugin_config))
        break
      case "修改":
        let config = py_plugin_config
        try {
          eval(e.msg.replace(/#?n?py(查看|修改)配置/, ""))
        } catch (err) {
          e.reply(`语法错误:${err.message}`)
          return
        }
        e.reply(YAML.stringify(config) + "\n配置已保存，重启python服务器中")
        await this.save_cfg(config)
        await this.py_restart(e)
        break
    }
  }


  async poetry_run(...args) {
    return new Promise(resolve => {
      exec(
        `poetry run ${args.join(" ")}`,
        {cwd: py_plugin_path},
        (error, stdout, stderr) => {
          resolve(error && error.message.replace(/WARNING.*?\r\n/g, ""))
        }
      );
    })
  }

  async save_cfg(data) {
    return new Promise(resolve => {
      let yamlStr = YAML.stringify(data);
      yamlStr = yamlStr.replace("plugins: []", "plugins:")
      fs.writeFile(path.join(py_plugin_path, "config.yaml"), yamlStr, () => {
        resolve()
      });
    })
  }
}
