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
    file_uri = "file://" + current_directory + "/image_temp.png"
    # 发送图片
    send.group_msg("[CQ:image,file=" + file_uri + ",id=40000]", "false")


def ai_chat(text):
    # 获取API
    api = config["ai"]["chat"]["api"]
    # 获取提示词
    prompt = config["ai"]["chat"]["prompt"]
    api = api.replace("%text%", text)
    # 构建链接
    api = api.replace("%prompt%", prompt)
    # 从链接获取json
    response, status = get.get_json(api)
    # 解析json
    msg = response["response"]
    # 发生消息
    send.group_msg(msg, False)
