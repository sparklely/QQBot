import socket
import json
import re
import threading
from waiting.initialize.config import go_config
from waiting.initialize.config import config
from waiting.events import msg
from file import log


# 通过继承创建监听事件线程
class init_event(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.status = True

    def stop(self):
        self.status = False

    @staticmethod
    def event(data):
        # 定义正则表达式
        json_data = None
        pattern = r'{.*}'

        # 使用正则表达式提取 JSON 数据部分
        match = re.search(pattern, data)
        
        try:
            if match:
                # 解析 JSON 字符串
                data = match.group()
                json_data = json.loads(str(data))
            # 解析post_type
            post_type = json_data["post_type"]
            if post_type == "message" or post_type == "message_sent":
                msg.execute(json_data)
        except KeyError:
            # 如果json_data中没有post_type字段
            log.warning("JSON数据中缺少post_type字段(可忽略)", True)
        except TypeError:
            # 如果json_data为空
            log.warning("JSON数据为空(可忽略)", True)
        except json.decoder.JSONDecodeError:
            # 如果json_data未终止字符串错误
            log.warning("JSON未终止字符串错误(可忽略)", True)

    def run(self):
        # 创建一个 TCP socket 对象
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = go_config["servers"][int(config['event']['address'])]["http"]["post"][0]["url"].replace("http://127.0.0.1:", "")
        port = port.replace("/", "")
        # 绑定 IP 地址和端口号
        server_address = ('127.0.0.1', int(port))
        server_socket.bind(server_address)

        # 监听连接
        server_socket.listen(1)
        log.info("成功注册监听事件", True)
        while True:
            # 接受客户端连接
            client_socket, client_address = server_socket.accept()

            try:
                # 接收请求数据
                request_data = client_socket.recv(1024).decode('utf-8')
            except UnicodeDecodeError:
                # 如果JSON数据无法读取
                log.warning("JSON数据无法读取(可忽略)", True)

            init_event.event(request_data)
            # 处理请求
            response = 'HTTP/1.1 200 OK\r\nContent-Type: text/plain; charset=utf-8\r\n\r\nHello, World!'
            client_socket.sendall(response.encode('utf-8'))

            # 关闭连接
            client_socket.close()

            # 退出循环
            if not self.status:
                break
