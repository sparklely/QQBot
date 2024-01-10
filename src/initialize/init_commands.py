from API import command
from command import acg
from command import ai


def start():
    command.reg('二次元', acg.acg_class, 'user')
    command.reg_help('二次元', '获取随机二次元', 'user')
