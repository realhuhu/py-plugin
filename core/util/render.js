import path from "path";
import fs from "fs";
import {segment} from "oicq";

let _render = null, _puppeteer = null;

async function init() {
  try {
    _render = (await import("../../../../lib/render.js")).getPluginRender;
  } catch (e) {
    _puppeteer = (await import("../../../../lib/puppeteer/puppeteer.js")).default;
  }
}


export async function render(app, func, data, imgType = "png") {
  if (!_render || !_puppeteer) await init();

  let layoutPath = path.join(global.py_plugin_path, "resources", "layout");
  let sys = {
    scale: "style=transform:scale(1.2)",
    copyright: `Created By Yunzai-Bot<span class="version">${JSON.parse(fs.readFileSync("package.json", "utf8")).version}</span> & Py-Plugin<span class="version">${global.py_plugin_version.join(".")}</span>`,
  }

  if (_render) {
    let base64 = _render(`py-plugin/apps/${app}/js`)(func, "index", {
      ...data,
      _res_path: `../../../../../../../../plugins/py-plugin/apps/${app}/js/resources/${func}`,
      _layout_res: `../../../../../../../../plugins/py-plugin/resources`,
      _layout_path: layoutPath,
      defaultLayout: path.join(layoutPath, "default.html"),
      sys
    }, imgType);
    return segment.image(`base64://${base64}`)
  } else if (_puppeteer) {
    return await _puppeteer.screenshot(`py-plugin-${app}-${func}`, {
      ...data,
      tplFile: path.join(global.py_plugin_path, "apps", app, "js", "resources", func, "index.html"),
      imgType: imgType,
      defaultLayout: path.join(layoutPath, "default.html"),
      _res_path: `../../../plugins/py-plugin/apps/${app}/js/resources/${func}`,
      _layout_res: `../../../plugins/py-plugin/resources`,
      _layout_path: layoutPath,
      sys
    })
  } else {
    console.log("无法确定渲染引擎")
  }
}

