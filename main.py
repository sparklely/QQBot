import threading
from event.event import start
from command import console

# ------------------------------------------------------初始化------------------------------------------------------
print("喵~开始初始化")


# send.group_msg("启动!", False)

# ------------------------------------------------------控制台-------------------------------------------------------
#通过继承创建监听事件线程
class event_start(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        start()
#继承监听事件线程
event=event_start()
#启动监听事件线程
event.start()
#下方代码正常运行
while True:
    # 获取命令
    Type = input("> ")
    # 执行命令
    if Type == "stop":
        # 输入了stop，结束运行
        break
    console.execute(Type)
