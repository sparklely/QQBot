import socket
from initialize.config import go_config


def start():
    # 创建一个 TCP socket 对象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = go_config["servers"][0]["http"]["post"][0]["url"].replace("http://127.0.0.1:", "")
    port = port.replace("/", "")
    # 绑定 IP 地址和端口号
    server_address = ('127.0.0.1', int(port))
    server_socket.bind(server_address)

    # 监听连接
    server_socket.listen(1)
    print('服务器已启动，等待连接...')

    while True:
        # 接受客户端连接
        client_socket, client_address = server_socket.accept()
        # print(f'与客户端 {client_address} 建立连接')

        # 接收请求数据
        request_data = client_socket.recv(1024).decode('utf-8')


        # 处理请求
        response = 'HTTP/1.1 200 OK\r\nContent-Type: text/plain; charset=utf-8\r\n\r\nHello, World!'
        client_socket.sendall(response.encode('utf-8'))

        # 关闭连接
        client_socket.close()

