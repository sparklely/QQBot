from network import get
from initialize.config import group
from initialize.config import address
from message import send
from command import user
import os


def execute(msg_id):
    # 获取消息
    heads = {"message_id": msg_id}
    data = get.heads_get_json(address + "/get_msg", heads)[0]["data"]
    # 判断是否为特定群消息
    if data["group"] and data["group_id"] == group:
        msg_info = data["message"]
        if msg_info == "woc":
            woc()
        if msg_info[:len("#")] == "#":
            cmd = msg_info[1:]
            user.execute(cmd)


def woc():
    send.group_msg("这里没有涩图哦", False)

