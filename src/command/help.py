from message import send
from initialize.g_vars import commands


def execute(arr_type):
    print(commands.console_help)


def user_execute(arr_type,msg_data):
    send.group_msg(commands.user_help, False)
