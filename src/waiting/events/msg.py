from waiting.message import get_msg


def execute(data):
    msg_id = data["message_id"]
    # 执行得到消息后应该做的
    get_msg.execute(msg_id)
