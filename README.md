# 1.前期准备

### 安装nodejs 依赖

​	cd到云崽根目录

​	如果是v2版本云崽，输入`npm install iconv-lite @grpc/grpc-js @grpc/proto-loader`

​	如果是v3版本云崽，输入`pnpm install iconv-lite @grpc/grpc-js @grpc/proto-loader  -w`

### 安装python

​	python版本>=3.9

​	安装教程请百度

​	如果是Linux系统，建议采用源码编译的方式，编译前请一定要安装以下依赖！否则以后可能出现无法安装依赖的情况

```shell
zlib-devel bzip2-devel expat-devel gdbm-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel
```

​	Linux安装python可以参考https://blog.csdn.net/weixin_41287692/article/details/105434826

​	注意，安装完成后不要删除源码文件夹，未来可能有用

# 2.使用

### 2.1 安装

​	进入云崽plugins目录，输入

```shell
git clone https://github.com/realhuhu/py-plugin.git
```

​	进入py-plugin文件夹，输入

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

​	第一次启动时，需要下载petpet和memes的依赖，需要等待一段时间

### 2.2 使用

### 2.2.1 获取插件

​	插件可以通过clone到plugins文件夹或者poetry run pip install的方式安装，内置的两个表情制作插件采用了前一种方式。

​	可以在github搜索或前往[nonebot商店](https://v2.nonebot.dev/store)获取插件

​	获取插件后，需要将插件名称添加到config.yaml中，重启云崽即可

​	未来将支持通过命令下载/卸载和启动/禁用插件

	#### 	clone到plugins文件夹

​	![image-20221117163456296](https://typora-1304907527.cos.ap-nanjing.myqcloud.com/202211171635372.png)

​	例如安装该插件，点击右上角跳转到github，获取clone链接

![image-20221117163642282](https://typora-1304907527.cos.ap-nanjing.myqcloud.com/202211171636344.png)

​	进入plugins文件夹，输入git clone 你的链接，完成后可以发现文件夹中多了这一项

![](https://typora-1304907527.cos.ap-nanjing.myqcloud.com/202211171639292.png)

​	在config.yaml中添加这个插件，重启即可

![image-20221117163841418](https://typora-1304907527.cos.ap-nanjing.myqcloud.com/202211171638464.png)

![image-20221117163950890](https://typora-1304907527.cos.ap-nanjing.myqcloud.com/202211171639930.png)

​	若插件支持配置，再config.yaml中配置即可

![image-20221117164035336](https://typora-1304907527.cos.ap-nanjing.myqcloud.com/202211171640377.png)

![image-20221117164106239](https://typora-1304907527.cos.ap-nanjing.myqcloud.com/202211171641279.png)

#### 	pip安装

​	点击卡片的复制安装命令

![image-20221117164235599](https://typora-1304907527.cos.ap-nanjing.myqcloud.com/202211171642641.png)

​	内容为```nb plugin install nonebot-plugin-remake```

​	则进入py-plugin文件夹，输入```poetry run pip install nonebot-plugin-remake```

​	完成后在config.yaml添加插件即可

![image-20221117164932853](https://typora-1304907527.cos.ap-nanjing.myqcloud.com/202211171649897.png)

![image-20221117164956910](https://typora-1304907527.cos.ap-nanjing.myqcloud.com/202211171649951.png)

​	通过```poetry run pip uninstall nonebot-plugin-remake```卸载插件



若同时采用了两种安装方式，则会运行pip安装的插件

nonebot机器人的命令以/开头，注意替换为#

![image-20221117165119644](https://typora-1304907527.cos.ap-nanjing.myqcloud.com/202211171651686.png)

![image-20221117165127354](https://typora-1304907527.cos.ap-nanjing.myqcloud.com/202211171651398.png)

### 2.2.2 配置文件

```yaml
log_level: INFO #大于等于log_level的日志才会打印
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
#encoding: gbk #如果输出乱码，可以开启这项试试看，主要是windows平台
```

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

说明python服务未启动，绝大部分出现于node app启动的情况下。启动时有提示`成功建立双向连接`才说明启动成功。如果没有这个提示请重启

```shell
[YzBot][16:49:46.170][INFO] 加载插件中..
[YzBot][16:49:46.355][INFO] python服务器启动中
[YzBot][16:49:46.383][INFO] 加载定时任务[2个]
[YzBot][16:49:46.384][INFO] 加载插件完成[15个]
[YzBot][16:49:46.384][INFO] -----------
[PyBot][08:49:47.742]][WARNING] Failed to extract font properties from F:\Bot\YunZaiV3\plugins\py-plugin\data\fonts\consola.ttf: In FT2Font: Can not load face (invalid stream operation; error code 0x55)
[PyBot][08:49:47.743]][WARNING] Failed to extract font properties from F:\Bot\YunZaiV3\plugins\py-plugin\data\fonts\FZSEJW.ttf: In FT2Font: Can not load face (invalid stream operation; error code 0x55)
[PyBot][08:49:47.743]][WARNING] Failed to extract font properties from F:\Bot\YunZaiV3\plugins\py-plugin\data\fonts\FZSJ-QINGCRJ.ttf: In FT2Font: Can not load face (invalid stream operation; error code 0x55)
[PyBot][08:49:47.743]][WARNING] Failed to extract font properties from F:\Bot\YunZaiV3\plugins\py-plugin\data\fonts\FZXS14.ttf: In FT2Font: Can not load face (invalid stream operation; error code 0x55)
[PyBot][08:49:47.744]][WARNING] Failed to extract font properties from F:\Bot\YunZaiV3\plugins\py-plugin\data\fonts\NotoSansSC-Regular.otf: In FT2Font: Can not load face (invalid stream operation; error code 0x55)
[PyBot][08:49:47.744]][WARNING] Failed to extract font properties from F:\Bot\YunZaiV3\plugins\py-plugin\data\fonts\NotoSerifSC-Regular.otf: In FT2Font: Can not load face (invalid stream operation; error code 0x55)
[PyBot][08:49:47.745]][SUCCESS] 插件导入成功： "nonebot_plugin_imageutils"
[PyBot][08:49:48.511]][SUCCESS] 插件导入成功： "nonebot_plugin_petpet"
[PyBot][08:49:48.770]][SUCCESS] 插件导入成功： "nonebot_plugin_memes"
[PyBot][08:49:48.845]][SUCCESS] 插件导入成功： "nonebot_plugin_analysis_bilibili"
[PyBot][08:49:48.857]][SUCCESS] 插件导入成功： "nonebot_plugin_remake"
[PyBot][08:49:48.857]][INFO] petpet正在检查资源文件...
[PyBot][08:49:48.870]][INFO] memes正在检查资源文件...
[PyBot][08:49:49.745]][INFO] memes资源文件检查完成
[PyBot][08:49:49.888]][INFO] petpet资源文件检查完成
[PyBot][08:49:49.888]][INFO] Py服务器已启动
[YzBot][16:49:49.894][INFO] python服务器启动成功
[YzBot][16:49:49.895][INFO] py服务器连接成功
[PyBot][08:49:49.898]][SUCCESS] 成功建立双向连接
```

# 4.使用远程

敬请期待
