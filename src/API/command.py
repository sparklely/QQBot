from initialize.g_vars import commands as c
from initialize.config import command_prefix as p


def reg(cmd, cla, cate):
    """
   注册命令

   Args:
    cmd (str) : 命令主体
    cla (class) : 类
    cate (str) : 类型，填写user或console
   """
    # 构建字典
    dic = {'class': cla, 'cate': cate}
    # 保存到全局变量
    c.commands.update({cmd: dic})


def reg_help(cmd, des, cate):
    """
    添加命令帮助
    Args:
     cmd (str) : 命令主体
     des (str) : 命令描述
     cate (str) :  类型，填写user或console
    """
    if cate == 'user':
        c.user_help = c.user_help + f'{p}{cmd}   <{des}>\n'
    else:
        c.console_help = c.console_help + f'\033[92m {cmd}  \033[94m {des}\033[0m\n'
