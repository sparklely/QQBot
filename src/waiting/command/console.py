from waiting.command import help
from waiting.initialize.g_vars import commands as cmd


def execute(c_type):
    # 转换为数组
    arr_type = c_type.split()
    if arr_type[0] == "help":
        help.execute(arr_type)
    # 如果输入的命令存在于字典中且cate为console
    if arr_type[0] in cmd.commands and cmd.commands[arr_type[0]]['cate'] == 'console':
        # 获取命令的类
        cmd_class = cmd.commands[arr_type[0]]['class']()
        # 执行命令
        cmd_class.console_execute(arr_type)
    else:
        print("无效的命令")
