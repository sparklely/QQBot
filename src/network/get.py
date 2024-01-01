import json

import requests
import os
from file import log
from urllib.parse import urlparse


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
            return json_data, status
        except json.decoder.JSONDecodeError as e:
            log.warning(e, True)
            return None, status
    except requests.exceptions.RequestException:
        return 'Request api exceptions', None


# 获取图片的方法
def get_img(url, cache):
    try:
        # 获取响应
        response = requests.get(url)
    except requests.exceptions:
        return 'Request api exceptions'
    # 获取图片内容
    image_data = response.content

    # 解析URL
    parsed_url = urlparse(url)
    # 获取路径部分
    path = parsed_url.path
    # 从路径中提取文件名
    image_name = path.split("/")[-1]

    # 创建目录
    os.makedirs("images", exist_ok=True)
    # 如果启用了缓存
    if cache:
        if not os.path.exists("images/" + image_name):
            # 写入图片
            with open("images/" + image_name, "wb") as file:
                file.write(image_data)
    else:
        # 删除原来的图片
        if os.path.exists("images/" + image_name):
            os.remove("images/" + image_name)
        # 写入图片
        with open("images/" + image_name, "wb") as file:
            file.write(image_data)
    log.info(f'从 {url} 获取了一张图片', False)
    return image_name
