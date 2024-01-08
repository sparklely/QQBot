import json
import os
from urllib.parse import urlparse

import requests
from httplib2.socks import ProxyError
from requests import RequestException

from file import log


# 所有方法都是返回响应内容,状态码
# 方法命名为 _返回值

# 最基础的get方法，需要传入url
def heads_get_text(url, heads: dict):
    try:
        # 获取响应
        response = requests.get(url, heads)
    except requests.exceptions:
        return 'Request api exceptions'
    # 获取状态码
    status = response.status_code
    # 获取返回文本
    text = response.text
    log.debug(f'向{url}发送了一条get请求', False)
    return text, status


def heads_get_json(url, heads: dict):
    try:
        # 获取响应
        response = requests.get(url, heads)
    except requests.exceptions:
        return 'Request api exceptions'
    # 获取状态码
    status = response.status_code
    # 获取返回文本
    text = response.json()
    log.debug(f'向{url}发送了一条get请求', False)
    return text, status


def get_text(url):
    try:
        # 获取响应
        response = requests.get(url)
    except requests.exceptions:
        return 'Request api exceptions'
    # 获取状态码
    status = response.status_code
    # 获取返回文本
    text = response.text
    log.debug(f'向{url}发送了一条get请求', False)
    return text, status


# 获取Json的get方法
def get_json(url):
    try:
        # 获取响应
        response = requests.get(url)
        # 获取状态码
        status = response.status_code
        # 获取JSON
        try:
            json_data = response.json()
            log.debug(f'向{url}发送了一条get请求', False)
            return json_data
        except json.decoder.JSONDecodeError as e:
            log.warning(str(e), True)
            return None, status
    except requests.exceptions.RequestException as e:
        log.error(f'无法向{url}发送get请求: {str(e)}', True)
        return 'Request api exceptions', None


# 获取图片的方法
def get_img(url, cache):
    try:
        # 获取响应
        response = requests.get(url)
        response.raise_for_status()  # 检查响应是否出错
    except ProxyError as e:
        log.error(f'代理异常: {str(e)}', True)
        return None
    except ConnectionError as e:
        log.error(f'连接异常: {str(e)}', True)
        return None
    except RequestException as e:
        log.error(f'响应异常: {str(e)}', True)
        return None
    except Exception as e:
        log.error(f'未知异常: {str(e)}', True)
        return None
    # 获取图片内容
    image_data = response.content
    # 解析URL
    parsed_url = urlparse(url)
    # 获取路径部分
    path = parsed_url.path
    # 获取文件名，不存在则默认为 default.png
    image_name = path.split("/")[-1] if path.split("/")[-1] else "default.png"

    # 创建目录
    os.makedirs("temp/images", exist_ok=True)
    # 如果启用了缓存
    if cache:
        if image_name == "default.png" and os.path.exists("temp/images/" + image_name):
            os.remove("temp/images/" + image_name)
        if not os.path.exists("temp/images/" + image_name):
            # 写入图片
            with open("temp/images/" + image_name, "wb") as file:
                file.write(image_data)
    else:
        # 删除原来的图片
        if os.path.exists("temp/images/" + image_name):
            os.remove("temp/images/" + image_name)
        # 写入图片
        with open("temp/images/" + image_name, "wb") as file:
            file.write(image_data)
    log.info(f'从 {url} 获取了一张图片', False)
    return image_name
