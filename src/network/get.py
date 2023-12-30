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
def get_img(url, cache):
    try:
        # 获取响应
        response = requests.get(url)
    except requests.exceptions:
        return 'Request api exceptions'
    # 获取状态码
    status = response.status_code
    image_data = response.content
    # 获取图片名称
    image_name = url.replaceAll("https:", "")
    image_name = image_name.replaceAll("http:", "")
    image_name = image_name.replaceAll("/", ".")
    # 如果启用了缓存
    if cache:
        if not os.path.exists("images/"+image_name):
            # 写入图片
            with open("images/"+image_name, "wb") as file:
                file.write(image_data)
    else:
        # 删除原来的图片
        if os.path.exists("images/"+image_name):
            os.remove("images/"+image_name)
        # 写入图片
        with open("images/"+image_name, "wb") as file:
            file.write(image_data)

    return image_name
