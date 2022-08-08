# 1.安装

**nodejs:**

​	cd到云崽根目录

​	如果是v2版本云崽，输入`npm install @grpc/grpc-js @grpc/proto-loader`

​	如果是v3版本云崽，输入`pnpm install @grpc/grpc-js @grpc/proto-loader -w`

**python:**

​	python版本>=3.8，本人是3.8.8

​	安装教程请百度

​	如果是Linux系统，建议采用源码编译的方式，编译前请一定要安装以下依赖！否则以后可能出现无法安装依赖的情况

```shell
zlib-devel bzip2-devel expat-devel gdbm-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel
```

​	Linux安装python可以参考https://blog.csdn.net/fanxl10/article/details/10685406

**poetry:**

​	poetry是python的包管理工具之一，被nonebot2采用，相当于nodejs的npm。安装依赖时会使用到它

​	**1.获取安装文件**

​	***linux:***

​	在任意目录下输入如下指令

```shell
curl -sSL https://install.python-poetry.org -o install-poetry.py
```

​	运行后目录里多了一个install-poetry.py文件

​	***windows***

​	创建一个空的install-poetry.py文件，然后打开https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py这个网站，将里面所有代码复制进去

​	用你的python执行这个文件

```shell
python install-poetry.py
```

​	安装需要一定的时间

​	安装结束后输入poetry仍然无效，因为poetry的文件夹没有被添加到环境变量	

​	**2.添加环境变量**

​	***linux***

​	输入

```shell
vim /etc/profile
```

​	滚动到最后一行，按i进行编辑，将 `export PATH="/root/.local/bin:$PATH"`

​	粘贴到最后一行

​	粘贴完成后按esc键，输入:wq保存并退出

​	最后输入

```shell
source /etc/profile
```

​	更新配置

​	***windows***

​	在Path环境变量增加`poetry`的路径`%USERPROFILE%\.poetry\bin`

​	**3.测试是否安装成功**

​	输入`poetry`查看是否有输出

# 2.使用

​	对于v2 v3，使用方法相同

## 2.1安装python依赖

​	进入云崽plugins目录，输入

```shell
git clone https://github.com/realhuhu/py-plugin.git
```

​	进入py-plugin文件夹，输入

```shell
poetry install
```

​	此时正在安装python依赖，第一行内容大致如下

```shell
Creating virtualenv py-plugin-8_cve6GP-py3.8 in /root/.cache/pypoetry/virtualenvs
```

​	等待安装完成即可

## 2.2配置config

​	进入py-plugin文件夹，将config_default.json复制一份，命名为config.json

​	输入`poetry env list --full-path`	

​	将带有Activated的路径复制，替换config.json中的pythonPath

​	注意，windows系统的路径是\，需要进行转义，类似

```json
{
  "version": [
    1,
    0,
    0
  ],
  "pythonPath": "C:\\Users\\huhu\\AppData\\Local\\pypoetry\\Cache\\virtualenvs\\py-plugin-ZwhPn4_3-py3.8\\Scripts\\python.exe",
  "host": "127.0.0.1",
  "port": "50051"
}

```

之后重启云崽
