import os
import pkgutil

from file import log
from waiting.command import console
from waiting.initialize import init_plugins, init_commands
from waiting.initialize.event import init_event
from API.register.plugin import plug


def init():
    # 遍历 plugins 包下的所有模块
    for module_info in pkgutil.walk_packages(['plugins']):
        # 导入模块
        module = module_info.module_finder.find_module(module_info.name).load_module()
        # 遍历模块中的成员
        for name, obj in module.__dict__.items():
            # 检查是否为类并且是否实现了 API.register.plugin.plug
            if (isinstance(obj, type) and issubclass(obj, plug) and
                    hasattr(obj, 'on_enable')):
                # 调用 on_enable 方法
                obj.on_enable()


# ------------------------------------------------------初始化------------------------------------------------------
log.info("喵~开始初始化", True)
init()
# 初始化数据库
# sql.start()
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
    try:
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
    except KeyboardInterrupt:
        # 无输入
        log.warning("未输入命令", True)
