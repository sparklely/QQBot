import threading

from command import console
from initialize.event import init_event

# ------------------------------------------------------初始化------------------------------------------------------
print("喵~开始初始化")

# 初始化sql
from initialize import sql
# 初始化doc
from initialize import doc


# ------------------------------------------------------监听事件-----------------------------------------------------
# 继承监听事件线程
event = init_event()
# 启动监听事件线程
event.start()
# TODO: 日志无法输出

# ------------------------------------------------------控制台-------------------------------------------------------
while True:
    # 获取命令
    Type = input("> ")
    # 执行命令
    # TODO: 修復stop命令
    if Type == "stop":
        event.stop()
        break
    try:
        console.execute(Type)
    except Exception as e:
        print(f"ERROR: 发生未知错误 {e}，尝试修复")
