import random
import os
from message import send
from initialize import config
from network import get


def random_img():
    # 获取API
    api = config.random_agc_api
    # 生成随机数
    num = random.randint(config.random_agc_min, config.random_agc_max)
    api = api.replace("%num%", str(num))
    # 获取图片文件
    get.get_img(api)
    # 获取绝对路径
    current_directory = os.getcwd()
    file_uri = "file://" + current_directory + "/image_temp.png"
    # 发送图片
    send.group_msg("[CQ:image,file=" + file_uri + ",id=40000]", "false")