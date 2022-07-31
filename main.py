import os
import time
import importlib

from core.server.server import startServer

root = os.path.dirname(os.path.abspath(__file__))

apps = map(
    lambda x: (x, importlib.import_module(f"apps.py.{x}")),
    map(lambda x: x.replace(".py", ""), os.listdir(os.path.join(root, "apps", "py")))
)

server, servicer = startServer(os.path.join(root, "config.json"), apps)

while servicer.server:
    time.sleep(5)
