import socket

def server_program():
    # 获取主机名
    host = socket.gethostname()
    port = 5000  # 初始化端口号

    server_socket = socket.socket()  # 获取 socket 实例
    server_socket.bind((host, port))  # 绑定主机名和端口号

    server_socket.listen(2)
    conn, address = server_socket.accept()  # 接受新连接
    print("连接来自: " + str(address))
    while True:
        # 接收数据流。不要接收超过 1024 字节的数据
        data = conn.recv(1024).decode()
        if not data:
            # 如果没有数据，跳出循环
            break
        print("来自用户的消息: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # 发送数据到客户端

    conn.close()  # 关闭连接


if __name__ == '__main__':
    server_program()
import socket


def client_program():
    host = socket.gethostname()  # 获取本地主机名
    port = 5000  # 设置服务器端口号

    client_socket = socket.socket()  # 获取 socket 实例
    client_socket.connect((host, port))  # 连接到服务器

    message = input(" -> ")  # 获取用户输入

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # 发送消息
        data = client_socket.recv(1024).decode()  # 接收响应

        print('来自服务器的消息: ' + data)  # 显示响应

        message = input(" -> ")  # 再次获取用户输入

    client_socket.close()  # 关闭连接


if __name__ == '__main__':
    client_program()
