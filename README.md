# ！！！Windows系统不要用git执行命令，用Powershell执行命令！！！

# 3月19日提示：如果你在3月19日更新了py-plugin版本，请先在py-plugin目录输入poetry install

# 1.前期准备

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

# 2. 插件使用

### 2.1 拉取代码

​	进入云崽根目录，输入

```shell
git clone https://github.com/realhuhu/py-plugin.git ./plugins/py-plugin/
```

### 2.2 安装nodejs 依赖

​	cd到云崽根目录

​	如果是v2版本云崽，输入`npm install iconv-lite @grpc/grpc-js @grpc/proto-loader`

​	如果是v3版本云崽，输入`pnpm install --filter=py-plugin `	

### 2.3 安装nodejs 依赖

​	首先进入py-plugin目录，然后有两种选择：

​	**方法一（推荐）：**	

```shell
poetry install
```

​	此时正在安装python依赖，第一行内容大致如下

```shell
Creating virtualenv py-plugin-8_cve6GP-py3.8 in /root/.cache/pypoetry/virtualenvs
```

​	**方法二：**

```shell
poetry run pip install -r requirements.txt --trusted-host mirrors.aliyun.com
```

​	等待安装完成即可，之后重启云崽

### 2.2 使用

### 2.2.1 获取插件

​	插件可以通过clone到plugins文件夹或者poetry run pip install的方式安装

​	可以在github搜索或前往[nonebot商店](https://v2.nonebot.dev/store)获取插件

​	获取插件后，需要将插件名称添加到config.yaml中，重启云崽即可

#### 命令安装（推荐）

​	对于可以pip install或nb plugin install的插件，可以使用```#py下载插件```指令进行安装

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

​	#py帮助：查看py的指令

​	#py信息：查看py解释器的文件夹

​	#py信息+插件名称：查看插件安装位置

​	#py下载插件+插件名称：自动运行poetry run pip install 插件，并将插件添加到config.yaml的plugins下，之后重启服务器

​	#py卸载插件+插件名称：自动运行poetry run pip uninstall 插件，并将将插件从config.yaml的plugins下删除，之后重启服务器

​	#py禁用插件+插件名称：将插件从config.yaml的plugins下删除，之后重启服务器

​	#py启用插件+插件名称：将插件添加到config.yaml的plugins下，之后重启服务器

​	#py全部插件：查看config.yaml的plugins下所有插件

​	#py更新插件+插件名称：更新指定插件，**不支持git安装的插件**

​	#py更新全部插件+插件名称：更新全部插件，**不支持git安装的插件**

​	#py重启：重新启动py服务器

​	#py查看配置，查看当前的config.yaml

​	#py修改配置+指令：修改配置。如`#py修改配置config.nickname=["云崽","yunzai"]`



### 2.2.3 配置文件

```yaml
log_level: INFO #日志等级
command_start:
  - "#"
command_sep:
  - "."
nickname:
  - 云崽
  - yunzai
superusers:
  - 123456
  - 654321
need_at: no #是否需要@机器人或加上机器人名字，默认no
plugins: #加载哪些插件就往下加
host: 127.0.0.1
port: 50052

#输出编码，默认windows使用gbk，其它平台使用utf-8
#开启后强制使用你指定的编码
#encoding:

#是否分开启动py服务器与云崽本体，默认不分开
#开启后需要你手动启动py服务器，再启动云崽
#independent: true

#开机时检查，执行on_startup注册的函数，如petpet开机时会检查更新素材，默认会检查
#开启下面选项跳过检查
#setup_check: false

#关机时检查，执行on_shutdown注册的函数，默认会检查
#开启下面选项跳过检查
#shutdown_check: false
```

若插件支持配置，在config.yaml中配置即可

![image-20221117164035336](https://typora-1304907527.cos.ap-nanjing.myqcloud.com/202211171640377.png)

![image-20221117164106239](https://typora-1304907527.cos.ap-nanjing.myqcloud.com/202211171641279.png)

# 3. 常见问题

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

​	在config.yaml中将host改为159.75.113.47，port改成50053即可，需要使用什么插件就在config.yaml的plugins添加 。[支持的插件](https://gitee.com/realhuhu/py-plugin/issues/I6655A)

![截图_20230321232514](https://typora-1304907527.cos.ap-nanjing.myqcloud.com/202303212325967.png)

