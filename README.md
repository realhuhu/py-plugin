# 0.安装

Python==3.8.8

**nodejs:**

​	@grpc/grpc-js

​	@grpc/proto-loader

**python:**

​	grpcio

​	nonebot2

​	googleapis-common-protos

​	nonebot_plugin_imageutils

可在config.json中配置python解释器路径、rpc地址

```json
{
  "version": [1,0,0],
  "pythonPath": "python",
  "host": "127.0.0.1",
  "port": "50051"
}
```

**poetry:**

​	poetry是python的包管理工具之一，被nonebot2采用，添加插件时会使用到它

​	***linux:***

​	在任意目录下输入如下指令

```shell
curl -sSL https://install.python-poetry.org -o install-poetry.py
```

​	运行后目录里多了一个install-poetry.py文件

​	用你的python执行这个文件

```shell
python install-poetry.py
```

​	安装需要一定的时间

​	安装结束后输入poetry仍然无效，因为poetry的文件夹没有被添加到环境变量

​	根据指示要将poetry所在文件夹添加到环境变量中，输入

```shell
vim /etc/profile
```

​	滚动到最后一行，按i进行编辑，将 export PATH="/root/.local/bin:$PATH"

​	粘贴到最后一行

​	粘贴完成后按esc键，输入:wq保存并退出

​	最后输入

```shell
source /etc/profile
```

​	更新配置，之后就能正常使用poetry
