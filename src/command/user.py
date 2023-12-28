from command import help, yiyan, ai
from initialize import config


def execute(c_type):
    # 转换为数组
    if c_type == "":
        return
    arr_type = c_type.split()
    if arr_type[0] == "help":
        help.user_execute(arr_type)
    if arr_type[0] == "ai":
        if len(arr_type) >= 3:
            if arr_type[1] == "img" and config.ai_img_enable:
                ai.ai_img(arr_type[2])
            if arr_type[1] == "chat" and config.ai_chat_enable:
                ai.ai_chat(arr_type[2])
    if arr_type[0] == "一言" and config.yiyan_enable:
        yiyan.yy()


