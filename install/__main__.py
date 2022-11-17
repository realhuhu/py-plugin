#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import ssl
import sys
import platform
import subprocess
from pathlib import Path
from functools import partial

ssl._create_default_https_context = ssl._create_unverified_context

__path__ = Path(os.path.dirname(os.path.abspath(__file__)))

__python_path__ = sys.executable

__platform__ = platform.system().lower()

if __platform__ not in ["windows", "linux"]:
    raise Exception("不支持的系统类型")

if __platform__ == "windows":
    __encoding__ = "gbk"
else:
    __encoding__ = "utf-8"

Cmd = partial(subprocess.Popen, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding=__encoding__)


def exec_cmd(command, hide=False):
    print(command)
    cmd = Cmd(command)
    stdout, stderr = cmd.communicate()
    if stdout and not hide:
        print(stdout)
    if stderr:
        raise Exception("!!! 错误 !!!" + stderr)

    return stdout.strip()


os.system('')

print("### 安装poetry中... ###")

exec_cmd(f'"{__python_path__}" {__path__ / "poetry.py"}')

if __platform__ == "windows":
    if exec_cmd(r'echo %APPDATA%\Python\Scripts', True) not in os.getenv("path"):
        print("### 添加环境变量... ###")
        path = exec_cmd(r'echo %Path%', True)
        if len(path) > 900:
            print(r"### 添加环境变量失败，请手动将 %APPDATA%\Python\Scripts 添加到 Path 环境变量 ###")
            exit(-1)
        else:
            res = exec_cmd(r'setx Path "%Path%;%APPDATA%\Python\Scripts"')
            if "警告" in res or "warning" in res:
                print(r"### 添加环境变量失败，请手动将 %APPDATA%\Python\Scripts 添加到 Path 环境变量 ###")
                exit(-1)


else:
    if not os.path.exists("/usr/bin/poetry"):
        print("### 创建软连接... ###")
        exec_cmd(r'ln -s $HOME/.local/bin/poetry /usr/bin')

if __platform__ == "windows":
    print("poetry安装完成，打开新的cmd窗口，输入poetry -V查看是否有输出")
else:
    print("poetry安装完成，请输入poetry -V查看是否有输出")
