# 1.前期准备

### 安装nodejs 依赖

​	cd到云崽根目录

​	如果是v2版本云崽，输入`npm install @grpc/grpc-js @grpc/proto-loader`

​	如果是v3版本云崽，输入`pnpm install @grpc/grpc-js @grpc/proto-loader -w`

### 安装python

​	python版本>=3.8.8，本人是3.8.8

​	安装教程请百度

​	如果是Linux系统，建议采用源码编译的方式，编译前请一定要安装以下依赖！否则以后可能出现无法安装依赖的情况

```shell
zlib-devel bzip2-devel expat-devel gdbm-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel
```

​	Linux安装python可以参考https://blog.csdn.net/weixin_41287692/article/details/105434826

​	注意，安装完成后不要删除源码文件夹，未来可能有用

# 2.使用

### 安装插件

​	对于v2 v3，使用方法相同

​	进入云崽plugins目录，输入

```shell
git clone https://github.com/realhuhu/py-plugin.git
```

​	进入py-plugin文件夹，用你的python运行install文件夹

```shell
python install
```

​	等待安装完成，输入`poetry`查看是否有输出，有则说明poetry安装完成，然后安装依赖，有两种选择：

**方法一（推荐）：**	

```shell
poetry install
```

​	此时正在安装python依赖，第一行内容大致如下

```shell
Creating virtualenv py-plugin-8_cve6GP-py3.8 in /root/.cache/pypoetry/virtualenvs
```

**方法二：**

```shell
poetry run pip install -r requirements.txt
```



​	等待安装完成即可，之后重启云崽

### 使用插件

发送 **#py帮助** 结果如下图所示

![image-1](https://cos.miao.seutools.com/readme/help-default.png)

发送 **#py插件管理帮助** 获取详细介绍

![image-1](https://cos.miao.seutools.com/readme/help-detail.png)

若想安装插件， 先发送 **#py查询插件** 获取支持的插件列表

![image-1](https://cos.miao.seutools.com/readme/all-app.png)

以安装米**游币自动兑换插件**为例，发送 **#py下载插件米游币自动兑换**，等待安装完成

![image-1](https://cos.miao.seutools.com/readme/download-myb.png)

重启后发送 **#py帮助** 结果如下图所示，说明新插件安装完成

![image-1](https://cos.miao.seutools.com/readme/help-new.png)

发送 **#米游币自动兑换帮助** 获取详细帮助

![image-1](https://cos.miao.seutools.com/readme/myb-detail.png)

# 3.常见问题

如果启动时报错，先重启一两遍看看能不能正常运行，如果还是报错按下面方法修复

#### 1.安装nodejs 依赖报错

先安装cnpm

```shell
npm install -g cnpm --registry=https://registry.npm.taobao.org
```

然后用cnpm安装

```shell
cnpm install @grpc/grpc-js @grpc/proto-loader
```

如果还是报错，可能是node版本问题，建议重装node

#### 2.poetry install 报错

![image-1](https://cos.miao.seutools.com/readme/error-http.jpg)

原因：需要安装 Microsoft Visual C++ 14.0 以上

在 https://go.microsoft.com/fwlink/?LinkId=691126 下载安装包，使用默认配置安装即可

#### 3.python安装依赖时提示ModuleNotFoundError:No module named _ctypes

如果是centos输入`sudo yum install libffi-devel `

如果是ubuntu输入`sudo apt install libffi-dev -y `

之后进Python源码文件夹，依次输入

```shell
sudo make clean
sudo ./configure
sudo make && sudo make install
```

之后重启云崽即可

#### 4.python安装依赖时提示ModuleNotFoundError:No module named _sqlite

如果是centos输入`yum install sqlite-devel `

如果是ubuntu输入`sudo apt-get install libsqlite3-dev `

之后进Python源码文件夹，依次输入

```shell
sudo make clean
sudo ./configure
sudo make && sudo make install
```

之后重启云崽即可

#### 5.安装插件时提示 git clone失败，请查看控制台

大部分是因为网络原因连不上github(部分插件被gitee识别为图床，因此只能通过github安装)，多试几次就好了。如果一直卡住并且等不及了，可以发送 #重启，然后再发送安装指令，重新下载安装插件

### 6.发送命令无反应

说明python服务未启动，绝大部分出现于node app启动的情况下。启动时有提示`python服务器启动中`才说明启动成功。如果没有这个提示请重启

```shell
0|Yunzai  | [2022-08-22T10:57:05.110] [MARK] [iPad:1438740274] - ----------
0|Yunzai  | [2022-08-22T10:57:05.111] [MARK] [iPad:1438740274] - Package Version: oicq@2.3.0 (Released on 2022/6/19)
0|Yunzai  | [2022-08-22T10:57:05.111] [MARK] [iPad:1438740274] - View Changelogs：https://github.com/takayama-lily/oicq/releases
0|Yunzai  | [2022-08-22T10:57:05.111] [MARK] [iPad:1438740274] - ----------
0|Yunzai  | [2022-08-22T10:57:05.181] [MARK] [iPad:1438740274] - 120.232.130.13:8080 connected
0|Yunzai  | [2022-08-22T10:57:05.377] [MARK] [iPad:1438740274] - Welcome, 长野原备用机器人 ! 正在加载资源...
0|Yunzai  | [2022-08-22T10:57:06.347] [MARK] [iPad:1438740274] - 加载了1095个好友，53个群，0个陌生人
0|Yunzai  | [2022-08-22T10:57:06.353] [MARK] [iPad:1438740274] - ----------
0|Yunzai  | [2022-08-22T10:57:06.353] [MARK] [iPad:1438740274] - 初始化Yunzai-Bot
0|Yunzai  | [2022-08-22T10:57:06.578] [INFO] [iPad:1438740274] - ---------^_^---------
0|Yunzai  | [2022-08-22T10:57:06.578] [INFO] [iPad:1438740274] - 喵喵插件1.9.6初始化~
0|Yunzai  | python插件1.1.5初始化~
0|Yunzai  | [2022-08-22T10:57:06.675] [MARK] [iPad:1438740274] - Yunzai-Bot 上线成功 版本v2.2.1
0|Yunzai  | [2022-08-22T10:57:06.675] [MARK] [iPad:1438740274] - https://github.com/Le-niao/Yunzai-Bot
0|Yunzai  | [2022-08-22T10:57:06.675] [MARK] [iPad:1438740274] - ----------
0|Yunzai  | [2022-08-22T10:57:06.704] [MARK] 发送好友消息[‪](2661467107)
0|Yunzai  | [2022-08-22T10:57:06.781] [INFO] succeed to send: [Private(2661467107)] 重启成功
0|Yunzai  | python服务器启动中
```

# 4.使用远程

如果实在装不上python的依赖，可以使用远程服务，前提是装上了nodejs的两个依赖

如果所有功能全部使用远程，把config.json中useRemote改成true即可

```json
{
  "local":{
    "host": "127.0.0.1",
    "port":50051
  },
  "remote":{
    "host": "42.193.148.140",
    "port":50051
  },
  "useRemote":true
}
```

如果只希望部分功能用远程，去useRemote添加这个功能的\_package._handler

例如扫雷，在apps/mine_sweep/js/index.js可以看到扫雷的函数是mine_sweep_start，定位后他们的\_package._handler是mine_sweep.sweep

```js
...

export const rule = {
  mine_sweep_start: {
    reg: "^#扫雷",
    priority: 700,
    describe: "开始扫雷",
  },
  mine_sweep_listener: {
    reg: "noCheck",
    priority: 800,
    describe: "开始扫雷",
  },
  mine_sweep_cancel: {
    reg: "^#取消扫雷",
    priority: 701,
    describe: "取消扫雷",
  },
};

...

async function createGame(e) {
  let call = StreamToStream({
    _package: "mine_sweep",//_package
    _handler: "sweep",//_handler
    onData: (errors, response) => {
     	...
      }
    },
    onEnd: () => {
		...
    },
  });

	...
}

async function timer(e, is_group, id) {
  let current;
  if (is_group) {
    current = group_call[id];
  } else {
    current = private_call[id];
  }

  if (current.timer) {
    clearTimeout(current.timer);
  }

  return setTimeout(() => {
    e.reply("扫雷已自动结束");
    current["call"].end();

  }, 5 * 60 * 1000);
}

function valid(e) {
  if (e.isGroup) {
    let qq = e.sender.user_id;
    let current = group_call[e.group_id].participant;
    return current.allow_all || qq === current.owner || current.other.indexOf(qq) !== -1;
  } else {
    return true;
  }
}

export async function mine_sweep_start(e) {
	...
}

export async function mine_sweep_listener(e) {
	...
}

export async function mine_sweep_cancel(e) {
	...
}
```

所以如果向让扫雷远程，将useRemote改成["mine_sweep.sweep"]即可

```json
{
  "local":{
    "host": "127.0.0.1",
    "port":50051
  },
  "remote":{
    "host": "42.193.148.140",
    "port":50051
  },
  "useRemote":[
    "mine_sweep.sweep"
  ]
}
```

对于多个插件同理

```json
{
  "local":{
    "host": "127.0.0.1",
    "port":50051
  },
  "remote":{
    "host": "42.193.148.140",
    "port":50051
  },
  "useRemote":[
    "mine_sweep.sweep",//扫雷使用远程
    "bh3.show_finance",//崩坏三手账使用远程
    "bh3.switch_autosign",//崩坏三自动签到使用远程
    "where_resource.where_resource_is" //地图资源查询使用远程，注意最后一项末尾不要加逗号！
  ]
}
```

修改完后重启

使用时方法相同，要先下载插件，然后使用

如果是需要保存数据的插件，比如崩坏三，你的数据会被保存到我的服务器

