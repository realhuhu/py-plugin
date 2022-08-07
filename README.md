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

​	安装方法请百度
