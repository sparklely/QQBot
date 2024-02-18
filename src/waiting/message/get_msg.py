from waiting.command import user
from waiting.initialize.config import address
from waiting.initialize.config import command_prefix
from waiting.initialize.config import group
from waiting.message import send
from network import get


def execute(msg_id):
    # 获取消息
    heads = {"message_id": msg_id}
    data = get.heads_get_json(address + "/get_msg", heads)[0]["data"]
    # 判断是否为特定群消息
    if data["group"] and (data["group_id"] in group):
        msg_info = data["message"]
        if msg_info == "woc":
            woc()
        if msg_info[:len(command_prefix)] == command_prefix:
            cmd = msg_info[len(command_prefix):]  # len(command_prefix)用于获取字符串的长度
            user.execute(cmd, data)


def woc():
    send.group_msg("这里没有涩图哦", False)
