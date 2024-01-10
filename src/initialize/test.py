from API import command
from message import send


# 这个类仅用于测试
def start():
    print("注册命令成功")
    command.reg('test', test_cmd, 'user')


class test_cmd:
    @staticmethod
    def user_execute(c_type):
        send.group_msg(str(c_type), True)
