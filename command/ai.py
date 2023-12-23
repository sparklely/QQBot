from message import send
from network import get
import os
from initialize.config import config


def ai_img(prompt):
    send.group_msg("开始画图...", False)
    # 获取API
    api = config["ai"]["img"]["api"]
    api = api.replace("%prompt%", prompt)
    # 获取图片文件
    get.get_img(api)
    # 获取绝对路径
    current_directory = os.getcwd()
    file_uri = "file://" + current_directory + "/../image_temp.png"
    # 发送图片
    send.group_msg("[CQ:image,file="+file_uri+",id=40000]", "false")
