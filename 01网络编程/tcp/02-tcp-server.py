import socket


def main():
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2.绑定服务端地址
    tcp_server_socket.bind(("", 7890))

    # 3.监听，将默认的套接字由主动变为被动
    # 最大允许同时连接的客户端
    tcp_server_socket.listen(128)

    # 4.等待客户端的链接
    # 返回一个为客户端服务的新的套接字 与 客户端的地址(元组)ip/port
    # 新的套接字负责为这个客户端收发数据，与客户端通信作用
    # 老的套接字 tcp_server_socket 负责继续监听另外的客户端
    new_client_socket, new_client_addr = tcp_server_socket.accept()
    print(new_client_addr)

    # 5.接收/发送数据
    recv_data = new_client_socket.recv(1024)
    print(recv_data)

    new_client_socket.send("您好!".encode("gbk"))

    # 6.关闭套接字
    new_client_socket.close()
    tcp_server_socket.close()



if __name__ == "__main__":
    main()
