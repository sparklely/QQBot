from message import send as send_msg
from file import upload
from file import log


def execute(arr_type):
    if arr_type[1] == "msg":
        # 发送消息
        send_msg.group_msg(arr_type[2], False)
    elif arr_type[1] == "file":
        # 发送文件
        if len(arr_type) == 4:
            upload.group_file(arr_type[2], arr_type[3], arr_type[4])
        else:
            upload.group_file(arr_type[2], arr_type[2], "/")
    else:
        # 没有参数，直接发送消息
        send_msg.group_msg(arr_type[1], False)
    log.info("\033[92m 发送成功\033[0m", True)
