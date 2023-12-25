import requests
from message import send
from initialize.config import yiyan_api


def yy():
    msg = requests.get(yiyan_api, {"code": "json"}).json()
    msg = msg["msg"]
    send.group_msg(msg, False)
