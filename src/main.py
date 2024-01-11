from file import log
from command import console
from initialize.event import init_event
from initialize import init_commands
import os
from initialize import sql
from initialize import init_plugins


# ------------------------------------------------------初始化------------------------------------------------------
log.info("喵~开始初始化", True)
# 初始化数据库
sql.start()
# 加载插件
init_plugins.start()
# ------------------------------------------------------监听事件-----------------------------------------------------
# 注册命令
init_commands.start()
# 继承监听事件线程
event = init_event()
# 启动监听事件线程
event.start()

# ------------------------------------------------------控制台-------------------------------------------------------
if os.name == 'posix':
    import readline

    # 将左箭头键与"left"字符串绑定
    readline.parse_and_bind("\033[D: left")
    # 将右箭头键与"right"字符串绑定
    readline.parse_and_bind("\033[C: right")
    # 将上箭头键与"up"字符串绑定
    readline.parse_and_bind("\033[A: up")
    # 将下箭头键与"down"字符串绑定
    readline.parse_and_bind("\033[B: down")
while True:
    # 获取命令
    Type = input("> ")
    # 执行命令
    if Type == "stop":
        event.stop()
        log.info("成功关闭程序", True)
        break
    try:
        console.execute(Type)
    except Exception as e:
        log.error(f"发生未知错误 {e}，尝试修复", True)
