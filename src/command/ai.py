from message import send
from network import get
import os
from initialize.config import config
from file import log


class ai_class:
    plugin = "bot"
    permission = "command.acg"

    @staticmethod
    def user_execute(arr_type):
        if len(arr_type) >= 3:
            if arr_type[1] == "img" and config.ai_img_enable:
                ai_class.ai_img(arr_type[2])
            if arr_type[1] == "chat" and config.ai_chat_enable:
                ai_class.ai_chat(arr_type[2])

    @staticmethod
    def ai_img(prompt):
        send.group_msg("开始画图...", False)
        # 获取API
        api = config["ai"]["img"]["api"]
        api = api.replace("%prompt%", prompt)
        # 获取图片文件
        image_name = get.get_img(api, False)
        if image_name is None:
            # 获取图片出错
            send.group_msg("获取图片出错", True)
            return
        # 获取绝对路径
        current_directory = os.getcwd()
        file_uri = f'file://{current_directory}/temp/images/{image_name}'
        # 发送图片
        send.group_msg("[CQ:image,file=" + file_uri + ",id=40000]", "false")

    @staticmethod
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
        # 发送消息
        send.group_msg(msg, False)
        log.info(f'ai聊天 提示词:{prompt} ;消息:{msg}', False)
