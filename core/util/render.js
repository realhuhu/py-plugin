import path from "path";
import fs from "fs";


let _render = null, _puppeteer = null;

async function init() {
  try {
    _render = (await import("../../../../lib/render.js")).getPluginRender;
  } catch (e) {
    _puppeteer = await import("../../../lib/puppeteer/puppeteer.js");
  }
}

export async function render(app, func, data, imgType = "png") {
  if (!_render || !_puppeteer) await init();
  if (_render) {
    let layoutPath = path.join(global.py_plugin_path, "resources", "layout");
    return _render(`py-plugin/apps/${app}/js`)(func, "index", {
      ...data,
      _res_path: `../../../../../../../../plugins/py-plugin/apps/${app}/js/resources/${func}`,
      _layout_res: `../../../../../../../../plugins/py-plugin/resources`,
      _layout_path: layoutPath,
      defaultLayout: path.join(layoutPath, "default.html"),
      sys: {
        scale:"style=transform:scale(1.2)",
        copyright: `Created By Yunzai-Bot<span class="version">${JSON.parse(fs.readFileSync("package.json", "utf8")).version}</span> & Py-Plugin<span class="version">${global.py_plugin_version.join(".")}</span>`,
      },
    }, imgType);
  } else if (_puppeteer) {
    console.log(_puppeteer);
  } else {
  }
}