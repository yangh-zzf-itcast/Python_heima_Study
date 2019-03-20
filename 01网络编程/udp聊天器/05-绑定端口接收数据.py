# 发送数据可以不绑定端口
# 接收数据必须绑定端口，给发送者一个目标，否则接收不到
import socket

def main():
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.绑定接收端本地信息，IP和端口
    local_addr = ("", 7788)
    udp_socket.bind(local_addr)

    # 3.接收数据
    # 1024表示接受的最大数据长度
    recv_data = udp_socket.recvfrom(1024)

    # 4.打印接收到的数据
    
    print(recv_data)

    # 5.关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()
    
