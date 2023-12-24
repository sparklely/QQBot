import requests
from message import send


def yy():
    msg = requests.get("https://api.cenguigui.cn/api/yiyan/", {"code": "json"}).json()
    msg = msg["msg"]
    send.group_msg(msg, False)
