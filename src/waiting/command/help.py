from waiting.message import send
from waiting.initialize.g_vars import commands


def execute(arr_type):
    print(commands.console_help)


def user_execute(arr_type):
    send.group_msg(commands.user_help, False)
