import os
import importlib

from core.server.server import startServer

root = os.path.dirname(os.path.abspath(__file__))

apps = map(
    lambda x: (x, importlib.import_module(f"apps.py.{x}")),
    map(lambda x: x.replace(".py", ""), os.listdir(os.path.join(root, "apps", "py")))
)

server = startServer(os.path.join(root, "config.json"), apps)
print("Python server start")
server.wait_for_termination()
print("Python server stop")
