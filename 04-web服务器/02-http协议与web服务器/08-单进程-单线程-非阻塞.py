import socket
import time

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_server_socket.bind(("", 7890))
tcp_server_socket.listen(128)

# 设置套接字为非阻塞的方式
tcp_server_socket.setblocking(False)

# 定义客户端socket列表，接收到的新客户端放入列表中
client_socket_list = list()

while True:
    time.sleep(1)

    try:
        # 由于tcp的socket设置为非堵塞，这边不会堵塞
        new_client_socket, new_addr = tcp_server_socket.accept()
    except Exception as ret:
        print("---没有新的客户端到来---")
    else:
        print("---接收到一个新的客户端---")
        
        # 将接收到的客户端套接字设为非堵塞，将来recv的时候不会堵塞
        new_client_socket.setblocking(False)
        # 接到到的客户端套接字添加到列表中
        client_socket_list.append(new_client_socket)

    # 单进程 循环并发实现多任务
    for client_socket in client_socket_list:
        try:
            recv_data = clinet_socket.recv(1024)
        except Exception as ret:
            print("---发生异常：%s---" % ret)
            print("---客户端没有发送数据过来---")
        else:
            print("---没有异常---")
            print(recv_data)
            # 对方发送过来数据，要判断数据是否为空
            if recv_data:
                print("---客户端发送过来数据---")
            else:
                # 对方调用了close 导致了 recv返回 空
                client_socket.close()
                # 客户端关闭后移除客户端套接字，否则每次都要循环，影响效率
                client_socket_list.remove(client_socket)
                print("---客户端已经关闭---")
