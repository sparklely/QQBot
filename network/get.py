import requests
import os


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
    except requests.exceptions:
        return 'Request api exceptions'
    # 获取状态码
    status = response.status_code
    # 获取JSON
    json = response.json()
    return json, status


# 获取图片的方法
def get_img(url):
    try:
        # 获取响应
        response = requests.get(url)
    except requests.exceptions:
        return 'Request api exceptions'
    # 获取状态码
    status = response.status_code
    image_data = response.content
    # 如果原图片存在，则删除
    if os.path.exists("image_temp.png"):
        os.remove("image_temp.png")

    # 写入图片
    with open("image_temp.png", "wb") as file:
        file.write(image_data)
    return status
