# 1.前期准备

### 安装nodejs 依赖

​	cd到云崽根目录

​	如果是v2版本云崽，输入`npm install @grpc/grpc-js @grpc/proto-loader`

​	如果是v3版本云崽，输入`pnpm install @grpc/grpc-js @grpc/proto-loader -w`

### 安装python

​	python版本>=3.8，本人是3.8.8

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

​	等待安装完成，输入`poetry`查看是否有输出，有则说明poetry安装完成，然后安装依赖

```shell
poetry install
```

​	此时正在安装python依赖，第一行内容大致如下

```shell
Creating virtualenv py-plugin-8_cve6GP-py3.8 in /root/.cache/pypoetry/virtualenvs
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

# 4.使用远程

如果实在装不上python的依赖，可以使用远程服务，前提是装上了nodejs的两个依赖

将config_default.json复制一份，命名为config.json，把host的值改成42.193.148.140，重启即可

使用时方法相同，要先下载插件，然后使用

如果是需要保存数据的插件，比如崩坏三，你的数据会被保存到我的服务器
