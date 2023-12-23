from message import send
from command import console
from event import start
import multiprocessing

# ------------------------------------------------------初始化------------------------------------------------------
print("喵~开始初始化")

# send.group_msg("启动!", False)

# 启动监听事件
process = multiprocessing.Process(target=start.start())
process.start()

# ------------------------------------------------------控制台-------------------------------------------------------
while True:
    # 获取命令
    Type = input("> ")
    # 执行命令
    if Type == "stop":
        # 输入了stop，结束运行
        send.group_msg("bey!", False)
        break
    console.execute(Type)
