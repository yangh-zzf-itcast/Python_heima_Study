import socket


def main():
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2.绑定服务端地址
    tcp_server_socket.bind(("", 7890))

    # 3.监听，将默认的套接字由主动变为被动
    # 最大允许同时连接的客户端
    tcp_server_socket.listen(128)

    # 让服务器循环监听
    while True:
        print("等待一个新的客户端到来......")
        # 4.等待客户端的链接
        # 返回一个为客户端服务的新的套接字 与 客户端的地址(元组)ip/port
        # 新的套接字负责为这个客户端收发数据，与客户端通信作用
        # 老的套接字 tcp_server_socket 负责继续监听另外的客户端
        new_client_socket, new_client_addr = tcp_server_socket.accept()
        print("新客户端%s已经连接....." % str(new_client_addr))

        # 循环为一个客户端进行服务，直接客户端不再发送数据为止
        while True:
            # 5.接收/发送数据
            recv_data = new_client_socket.recv(1024)
            print("客户端发送的请求是：%s" % recv_data.decode("gbk"))
            
            # 如果recv解阻塞：1.客户端发送过来数据 2.客户端close关闭连接
            # 关闭连接之后，recv_data为None
            if recv_data:
                new_client_socket.send("您好!".encode("gbk"))
            else:
                break

        print("客户端%s连接结束....." % str(new_client_addr))
        # 6.关闭客户端套接字
        new_client_socket.close()
    
    # 7.关闭服务器套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
