import requests
from waiting.message import send
from waiting.initialize.config import yiyan_api


class yy_class:
    plugin = 'bot'
    permission = "command.yy"

    @staticmethod
    def user_execute(args,msg_data):
        yy_class.yy()

    @staticmethod
    def yy():
        msg = requests.get(yiyan_api, {"code": "json"}).json()
        msg = msg["msg"]
        send.group_msg(msg, False)
