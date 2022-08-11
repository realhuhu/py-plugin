# 1.安装

**安装nodejs 依赖**

​	cd到云崽根目录

​	如果是v2版本云崽，输入`npm install @grpc/grpc-js @grpc/proto-loader`

​	如果是v3版本云崽，输入`pnpm install @grpc/grpc-js @grpc/proto-loader -w`

**安装python:**

​	python版本>=3.8，本人是3.8.8

​	安装教程请百度

​	如果是Linux系统，建议采用源码编译的方式，编译前请一定要安装以下依赖！否则以后可能出现无法安装依赖的情况

```shell
zlib-devel bzip2-devel expat-devel gdbm-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel
```

​	Linux安装python可以参考https://blog.csdn.net/weixin_41287692/article/details/105434826

# 2.使用

​	对于v2 v3，使用方法相同

​	进入云崽plugins目录，输入

```shell
git clone https://github.com/realhuhu/py-plugin.git
```

​	进入py-plugin文件夹，输入用你的python运行install-poetry文件夹

```shell
python install-poetry
```

​	等待安装完成，输入`poetry`查看是否有输出，有则说明poetry安装完成

```shell
poetry install
```

​	此时正在安装python依赖，第一行内容大致如下

```shell
Creating virtualenv py-plugin-8_cve6GP-py3.8 in /root/.cache/pypoetry/virtualenvs
```

​	等待安装完成即可，之后重启云崽