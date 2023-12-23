from network import get
from initialize.config import group
from initialize.config import address
from message import send


def execute(msg_id):
    # 获取消息
    heads = {"message_id": msg_id}
    data = get.heads_get_json(address + "/get_msg", heads)[0]["data"]
    # 判断是否为特定群消息
    if data["group"] and data["group_id"] == group:  # data["group_id"] == group:
        msg_info = data["message"]
        if msg_info == "woc":
            woc()


def woc():
    send.group_msg("此处无色图", False)
