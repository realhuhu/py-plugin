# ！！！Windows系统不要用git执行命令，用cmd或Powershell执行命令！！！

# 1.前期准备

### 安装nodejs 依赖

​	cd到云崽根目录

​	如果是v2版本云崽，输入`npm install iconv-lite @grpc/grpc-js @grpc/proto-loader`

​	如果是v3版本云崽，输入`pnpm add iconv-lite @grpc/grpc-js @grpc/proto-loader -w`

### 安装python

​	python版本>=3.8 **不要使用python3.11**

​	Linux系统安装python教程请百度

​	ubuntu系统使用apt-get即可，如果是centos系统，建议采用源码编译的方式，编译前请一定要安装以下依赖！否则以后可能出现无法安装依赖的情况

```shell
zlib-devel bzip2-devel expat-devel gdbm-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel
```

​	centos系统安装python可以参考https://blog.csdn.net/weixin_41287692/article/details/105434826

​	注意，安装完成后不要删除源码文件夹，未来可能有用

​	Windows安装python，请下载软件一路安装过去，[python3.9.10](https://www.123pan.com/s/jqW9-w78JH.html)


### 安装poetry

[poetry官网](https://python-poetry.org/docs/)

**Linux, macOS**

```shell
curl -sSL https://install.python-poetry.org | python -
```
poetry可执行文件位于```$HOME/.local/bin```，将其添加到环境变量或给```$HOME/.local/bin/poetry```添加软连接

**Windows**

请按住shift键+右键打开Powershell运行下面命令

```shell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

注意这里的```python```指你的python解释器，若你的python对应的命令为python3或其它自定义的命令，请注意替换原命令中的```python```

然后将```%APPDATA%\Python\Scripts```添加到PATH环境变量(位置在右键此电脑→属性→高级系统设置→环境变量)

等待安装完成，输入`poetry`查看是否有输出，有则说明poetry安装完成

# 2.使用

### 2.1 安装

​	进入云崽根目录，输入

```shell
git clone https://github.com/realhuhu/py-plugin.git ./plugins/py-plugin/
```

​	然后安装python依赖，首先进入py-plugin目录，然后有两种选择：

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
poetry run pip install -r requirements.txt --trusted-host mirrors.aliyun.com
```

​	等待安装完成即可，之后重启云崽

### 2.2 使用

### 2.2.1 获取插件

​	插件可以通过clone到plugins文件夹或者poetry run pip install的方式安装，内置的两个表情制作插件采用了前一种方式。

​	可以在github搜索或前往[nonebot商店](https://v2.nonebot.dev/store)获取插件

​	获取插件后，需要将插件名称添加到config.yaml中，重启云崽即可

​	未来将支持通过命令下载/卸载和启动/禁用插件

#### 命令安装（推荐）

对于可以pip install或nb plugin install的插件，可以使用```#py下载插件```指令进行安装

![image-20221120202102903](https://typora-1304907527.cos.ap-nanjing.myqcloud.com/202211202021020.png)

![image-20221120202148165](https://typora-1304907527.cos.ap-nanjing.myqcloud.com/202211202021203.png)

​	此方法能自动安装依赖，并自动将插件添加到config.yaml的plugins下

#### pip安装（推荐）

​	如果无法命令安装，也可以使用pip安装，

​	如上图插件，进入py-plugin目录，输入命令```poetry run pip install nonebot-plugin-gspanel```即可安装

​	此方法能自动安装依赖，但需要手动将插件名称添加到config.yaml的plugins下

![image-20221117164932853](https://typora-1304907527.cos.ap-nanjing.myqcloud.com/202211202025156.png)

​	输入命令```poetry run pip uninstall nonebot-plugin-gspanel```彻底卸载插件

####    clone到plugins文件夹（不推荐）

​	![image-20221117163456296](https://typora-1304907527.cos.ap-nanjing.myqcloud.com/202211171635372.png)

​	例如安装该插件，点击右上角跳转到github，获取clone链接

![image-20221117163642282](https://typora-1304907527.cos.ap-nanjing.myqcloud.com/202211171636344.png)

​	进入plugins文件夹，输入git clone 你的链接，完成后可以发现文件夹中多了这一项

![](https://typora-1304907527.cos.ap-nanjing.myqcloud.com/202211171639292.png)

​	在config.yaml中添加这个插件，重启即可

![image-20221117163841418](https://typora-1304907527.cos.ap-nanjing.myqcloud.com/202211171638464.png)

![image-20221117163950890](https://typora-1304907527.cos.ap-nanjing.myqcloud.com/202211171639930.png)

​	

若同时采用了两种安装方式，则会优先运行pip/命令安装的插件

nonebot机器人的命令以/开头，注意替换为#

![image-20221117165119644](https://typora-1304907527.cos.ap-nanjing.myqcloud.com/202211171651686.png)

![image-20221117165127354](https://typora-1304907527.cos.ap-nanjing.myqcloud.com/202211171651398.png)

### 2.2.2 指令

​	#py下载插件+插件名称：自动运行poetry run pip install 插件，并将插件添加到config.yaml的plugins下，之后重启服务器

​	#py禁用插件+插件名称：将插件从config.yaml的plugins下删除，之后重启服务器

​	#py启用插件+插件名称：将插件添加到config.yaml的plugins下，之后重启服务器

### 2.2.3 配置文件

```yaml
log_level: INFO #大于等于log_level的日志才会打印
command_start: #命令前缀，可以写多个
  - "#"
command_sep:
  - "."
nickname: #机器人的名字
  - 云崽
  - yunzai
superusers: #机器人主人
  - 123456
  - 654321
need_at: no #是否需要@机器人或加上机器人名字才能触发指令，默认no
plugins: #运行哪些插件
  - nonebot-plugin-petpet
  - nonebot-plugin-memes
  # 加载哪些插件就继续往下加
host: 127.0.0.1 #python服务器启动的地址
port: 50052 #python服务器启动的端口
independent: false #py服务器是否独立运行，开启此项后需要你手动启动py服务器，然后启动云崽
encoding: gbk #如果输出乱码，可以开启这项试试看，主要是windows平台
setup_check: utf-8 #启动时是否检查资源
```

若插件支持配置，在config.yaml中配置即可

![image-20221117164035336](https://typora-1304907527.cos.ap-nanjing.myqcloud.com/202211171640377.png)

![image-20221117164106239](https://typora-1304907527.cos.ap-nanjing.myqcloud.com/202211171641279.png)

# 3.部分插件安装方法

**直接 #py下载插件[插件名] 或 进入py-plugin目录输入 poetry run pip install [插件名]**

| 插件名称                                                     | 备注                                       |
| ------------------------------------------------------------ | ------------------------------------------ |
| [nonebot-plugin-status](https://github.com/cscs181/QQ-GitHub-Bot/tree/master/src/plugins/nonebot_plugin_status) |                                            |
| [haruka-bot](https://github.com/SK-415/HarukaBot)            |                                            |
| [nonebot-plugin-picsearcher](https://github.com/synodriver/nonebot_plugin_picsearcher)                               | 需要配置，如exhentai的cookie，具体见原插件 |
| [nonebot-plugin-biliav](https://github.com/knva/nonebot_plugin_biliav) |                                            |
| [nonebot-plugin-abbrreply](https://github.com/anlen123/nonebot_plugin_abbrreply) | 无需命令前缀                               |
| [nonebot-plugin-guess](https://github.com/ffreemt/nonebot-plugin-guess-game) | 自带题库少，需要自定义题目                 |
| [nonebot-plugin-r6s](https://github.com/abrahum/nonebot_plugin_r6s) |                                            |

太多了，懒得写了...

**git clone安装**

*崩坏三*

在py的plugins文件夹git clone -b nonebot https://github.com/chingkingm/honkai_mys.git
到plugins/honkai_mys 把config_default.yaml复制一份，命名为config.yaml，填上自己cookie
在py plugin文件夹输入poetry run pip install genshinhelper sqlitedict
最后在config.yaml加上插件honkai_mys就行了

也许还有其它插件，懒得找了...

# 4.常见问题

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

说明python服务未启动，绝大部分出现于node app启动的情况下。启动时有提示`成功建立连接`才说明启动成功。如果没有这个提示请重启

```shell
[PyBot][14:03:07.125][INFO] [drivers]Py服务器开机中
[PyBot][14:03:07.786][SUCCESS] [plugin.manager]插件导入成功： "nonebot_plugin_gspanel"
[PyBot][14:03:07.909][SUCCESS] [plugin.manager]插件导入成功： "nonebot_plugin_abstract"
[PyBot][14:03:07.989][SUCCESS] [plugin.manager]插件导入成功： "nonebot_plugin_minesweeper"
[PyBot][14:03:08.001][SUCCESS] [plugin.manager]插件导入成功： "nonebot_plugin_remake"
[PyBot][14:03:08.060][SUCCESS] [plugin.manager]插件导入成功： "honkai_mys"
[PyBot][14:03:08.862][SUCCESS] [plugin.manager]插件导入成功： "nonebot_plugin_memes"
[PyBot][14:03:10.015][SUCCESS] [plugin.manager]插件导入成功： "nonebot_plugin_petpet"
[PyBot][14:03:10.015][INFO] [gspanel.__utils__]正在检查面板插件所需资源...
[PyBot][14:03:10.017][INFO] [gspanel.__utils__]面板插件所需资源检查完毕！
[PyBot][14:03:10.253][INFO] [htmlrender.browser]使用 chromium 启动
[PyBot][14:03:10.385][INFO] [htmlrender]Browser Started.
[PyBot][14:03:10.385][INFO] [memes.download]正在检查资源文件...
[PyBot][14:03:10.386][INFO] [petpet.download]正在检查资源文件...
[PyBot][14:03:12.387][INFO] [drivers]Py服务器已开机(Py started)
[PyBot][14:05:03.188][SUCCESS] [core.server.server]成功建立request连接
[PyBot][14:05:03.188][SUCCESS] [core.server.server]成功建立result连接
```

# 5.使用远程

在config.yaml中将host改为159.75.113.47即可，需要使用什么插件就在config.yaml的plugins添加  
### 支持的插件

  - [nonebot-plugin-memes](https://github.com/noneplugin/nonebot-plugin-memes)
  - [nonebot-plugin-petpet](https://github.com/noneplugin/nonebot-plugin-petpet)
  - [nonebot-plugin-minesweeper](https://github.com/noneplugin/nonebot-plugin-minesweeper)
  - [nonebot-plugin-remake](https://github.com/noneplugin/nonebot-plugin-remake)
  - [nonebot-plugin-abstract](https://github.com/CherryCherries/nonebot-plugin-abstract)
  - [nonebot-plugin-gspanel](https://github.com/monsterxcn/nonebot-plugin-gspanel)
  - [nonebot-plugin-reborn](https://github.com/Aziteee/nonebot_plugin_reborn)
  - [nonebot-plugin-sky](https://github.com/Kaguya233qwq/nonebot_plugin_sky)
  - [nonebot-plugin-roll](https://github.com/MinatoAquaCrews/nonebot_plugin_roll)
  - [nonebot-plugin-analysis-bilibili](https://github.com/mengshouer/nonebot_plugin_analysis_bilibili)
  - [nonebot-plugin-miragetank](https://github.com/RafuiiChan/nonebot_plugin_miragetank)
  - [nonebot-plugin-wordle](https://github.com/noneplugin/nonebot-plugin-wordle)
  - [nonebot-plugin-wordsnorote](https://github.com/GC-ZF/nonebot_plugin_wordsnorote)
  - [nonebot-plugin-abstract](https://github.com/CherryCherries/nonebot-plugin-abstract)
  - [nonebot-plugin-tarot](https://github.com/MinatoAquaCrews/nonebot_plugin_tarot)
  - [nonebot-plugin-groupmate-waifu](https://github.com/KarisAya/nonebot_plugin_groupmate_waifu)
  - [nonebot-plugin-atri](https://github.com/FYWinds/nonebot-plugin-atri)
  - [nonebot-plugin-withdraw](https://github.com/noneplugin/nonebot-plugin-withdraw)
  - [nonebot-plugin-abbrreply](https://github.com/anlen123/nonebot_plugin_abbrreply)
  - [nonebot-plugin-emojimix](https://github.com/noneplugin/nonebot-plugin-emojimix)
  - [nonebot-plugin-arktools](https://github.com/NumberSir/nonebot_plugin_arktools)
  - [nonebot-plugin-arkrecord](https://github.com/zheuziihau/nonebot_plugin_arkrecord)
  - [nonebot-plugin-cchess](https://github.com/noneplugin/nonebot-plugin-cchess)
  - [nonebot-plugin-animeres](https://github.com/Melodyknit/nonebot_plugin_animeres)
  - [nonebot-plugin-epicfree](https://github.com/monsterxcn/nonebot_plugin_epicfree)
### 不支持的插件

  - [nonebot-plugin-mystool](https://github.com/Ljzd-PRO/nonebot-plugin-mystool)  无法分bot存储数据
  - [honkai-mys](https://github.com/chingkingm/honkai_mys) 无法分bot存储数据
  - [nonebot-plugin-trpglogger](https://github.com/thereisnodice/TRPGLogger) 无法分bot存储数据
  - [nonebot-plugin-cocdicer](https://github.com/abrahum/nonebot_plugin_cocdicer) 不支持onebot12
  - [nonebot-plugin-directlinker](https://github.com/ninthseason/nonebot-plugin-directlinker) 不支持群文件搜索
  - [nonebot-plugin-myb-exchange](https://github.com/CMHopeSunshine/LittlePaimon/tree/Bot/src/plugins/nonebot_plugin_myb_exchange) 无法分bot发消息
  - [LittlePaimon](https://github.com/CMHopeSunshine/LittlePaimon/tree/nonebot2) 无法分bot发消息
  - [nonebot-plugin-novelai](https://github.com/sena-nana/nonebot-plugin-novelai) 没钱买账号
  - [GenshinUID](https://github.com/KimigaiiWuyi/GenshinUID/tree/nonebot2-beta1) 我绑不上cookie


### 未来支持的插件
  - [YetAnotherPicSearch](https://github.com/NekoAria/YetAnotherPicSearch) 待修复bug