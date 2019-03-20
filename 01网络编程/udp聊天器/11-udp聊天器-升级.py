import socket


def send_msg(udp_socket):
    """发送消息"""
    # 获取要发送的内容
    dest_ip = input("请输入对方的ip:")
    dest_port = int(input("请输入对方的端口:"))      
    send_data = input("请输入您要发送的消息")
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def recv_msg(udp_socket):
    """接收数据"""    
    recv_data = udp_socket.recvfrom(1024)
    recv_msg, recv_addr = recv_data
    print("%s:%s" % (recv_addr, recv_msg.decode("utf-8")))


def main():

    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 循环处理聊天
    udp_socket.bind(("", 7788))

    while True:
        print("------udp聊天器-------")
        print("1:发送消息")
        print("2:接收消息")
        print("0:退出系统")
        op = int(input("请输入操作："))

        if op == 1:
            # 发送消息
            send_msg(udp_socket)
        elif op == 2:
            # 接收消息
            recv_msg(udp_socket)
        elif op == 0:
            # 3.可以退出聊天室 
            break

    # 关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()
