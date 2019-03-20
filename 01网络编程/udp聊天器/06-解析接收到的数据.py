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
    # 接收到的是一个元组，包含 (接收到的数据，(发送方的ip，port))
    recv_data = udp_socket.recvfrom(1024)
    recv_msg = recv_data[0]  # 存储的数据
    send_addr = recv_data[1]  # 发送方的地址信息

    # 4.打印接收到的数据
    # 对接收到的数据解码 decode 与发送时的 encode对应
    # print(recv_data)
    print("%s: %s" % (str(send_addr), recv_msg.decode("gbk")))

    # 5.关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()
    
