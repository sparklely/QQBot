import socket
import json
import re
import threading
from initialize.config import go_config
from events import msg

# 通过继承创建监听事件线程
class init_event(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.status=True

    def stop(self):
        self.status=False

    def event(self,data):
        # 定义正则表达式
        json_data = None
        pattern = r'{.*}'

        # 使用正则表达式提取 JSON 数据部分
        match = re.search(pattern, data)

        if match:
            # 解析 JSON 字符串
            data = match.group()
            json_data = json.loads(str(data))

        # 解析post_type
        post_type = json_data["post_type"]
        if post_type == "message" or post_type == "message_sent":
            msg.execute(json_data)

    def run(self):
        # 创建一个 TCP socket 对象
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = go_config["servers"][0]["http"]["post"][0]["url"].replace("http://127.0.0.1:", "")
        port = port.replace("/", "")
        # 绑定 IP 地址和端口号
        server_address = ('127.0.0.1', int(port))
        server_socket.bind(server_address)

        # 监听连接
        server_socket.listen(1)
        print("成功注册监听事件")
        while True:
            # 接受客户端连接
            client_socket, client_address = server_socket.accept()

            # 接收请求数据
            request_data = client_socket.recv(1024).decode('utf-8')

            init_event.event(None,request_data)
            # 处理请求
            response = 'HTTP/1.1 200 OK\r\nContent-Type: text/plain; charset=utf-8\r\n\r\nHello, World!'
            client_socket.sendall(response.encode('utf-8'))

            # 关闭连接
            client_socket.close()

            # 退出循环
            if self.status==False:
                break
