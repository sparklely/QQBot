import requests


# 所有方法都是返回响应内容,状态码
# 方法命名规范 发送_返回

# 最基础的post方法，传入url和data
# data 示例: {"key1": "value1", "key2": "value2"}
def data_text(url, data):
    # 发送post请求
    response = requests.post(url, data)
    # 获取状态码
    status = response.status_code
    # 获取返回文本
    text = response.text
    return text, status


# 返回json的post请求，传入与 data_text(url,data)相同
def data_json(url, data):
    # 发送post请求
    response = requests.post(url, data)
    # 获取状态码
    status = response.status_code
    # 获取返回文本
    text = response.text
    return text, status

# 返回json的post请求,使用json传输数据,支持头
def json_headers(url,headers,data):
    headers['Content-Type']="application/json; charset=UTF-8"
    response =requests.post(url,headers=headers,json=data)
    return response