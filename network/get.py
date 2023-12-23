import requests


# 所有方法都是返回响应内容,状态码
# 方法命名为 _返回值

# 最基础的get方法，需要传入url
def heads_get_text(url, heads: dict):
    # 获取响应
    response = requests.get(url, heads)
    # 获取状态码
    status = response.status_code
    # 获取返回文本
    text = response.text
    return text, status


def get_text(url):
    # 获取响应
    response = requests.get(url)
    # 获取状态码
    status = response.status_code
    # 获取返回文本
    text = response.text
    return text, status


# 获取Json的get方法
def get_json(url):
    # 获取响应
    response = requests.get(url)
    # 获取状态码
    status = response.status_code
    # 获取JSON
    json = response.json()
    return json, status
