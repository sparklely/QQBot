import threading

from command import console
from initialize.event import start

# ------------------------------------------------------初始化------------------------------------------------------
print("喵~开始初始化")

# 初始化sql
from initialize import sql


# ------------------------------------------------------监听事件-----------------------------------------------------
# 通过继承创建监听事件线程
class event_start(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        start()


# 继承监听事件线程
event = event_start()
# 启动监听事件线程
event.start()

# TODO: 检查data-doc完整性 (initialize.doc)

# ------------------------------------------------------控制台-------------------------------------------------------
while True:
    # 获取命令
    Type = input("> ")
    # 执行命令
    # TODO: 修復stop命令
    if Type == "stop":
        # 输入了stop，结束运行
        break
    try:
        console.execute(Type)
    except Exception as e:
        print(f"ERROR: 发生未知错误 {e}，尝试修复")
