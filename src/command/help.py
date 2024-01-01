from message import send
from initialize.config import command_prefix as p
from initialize import config


def execute(arr_type):
    print("\033[92m help  \033[94m 获取帮助")
    print("\033[92m send msg <消息内容>  \033[94m 发送消息")
    print("\033[92m send file <文件路径> <文件名> <文件存储目录>  \033[94m 发送文件\033[0m")


def user_execute(arr_type):
    msg = ""
    # AI画图启用
    if config.ai_img_enable:
        msg = msg + f'{p}ai img 提示词   <AI画图>\n'
    # AI聊天启用
    if config.ai_chat_enable:
        msg = msg + f'{p}ai chat 内容   <AI聊天>\n'
    # 一言启用
    if config.yiyan_enable:
        msg = msg + f'{p}一言   <获取一言>\n'
    # 随机二次元启动
    if config.random_agc_enable:
        msg = msg + f'{p}二次元   <获取随机二次元>'

    send.group_msg(msg, False)
