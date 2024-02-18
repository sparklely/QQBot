from API.data.global_vars import registries as r
from file.config import config
from enum import Enum


def reg(cmd, cla, cate):
    """
   注册命令

   Args:
    cmd (str) : 命令主体
    cla (class) : 类
    cate (str) : 类型，传入枚举category
   """
    # 构建字典
    dic = {'class': cla, 'cate': cate}
    # 保存到全局变量
    r.commands.update({cmd: dic})


def reg_help(cmd, des, cate):
    """
    添加命令帮助
    Args:
     cmd (str) : 命令主体
     des (str) : 命令描述
     cate (str) :  类型，传入枚举category
    """
    # 读取命令前缀
    p = config["command"]["prefix"]
    if cate == category.USER:
        r.user_help = r.user_help + f'{p}{cmd}   <{des}>\n'
    else:
        r.console_help = r.console_help + f'\033[92m {cmd}  \033[94m {des}\033[0m\n'


class category(Enum):
    """
    命令的类型

    USER: 用户命令

    CONSOLE: 控制台命令

    BOTH: 两者
    """
    USER = 1
    CONSOLE = 2
    BOTH = 3
