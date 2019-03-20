# 同一个套接字，同时既可以发数据也可以收数据，全双工
import socket

# 使用udp发送数据
# 不指定端口，系统会动态分配默认端口
def main():
    # 创建一个udp关键字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 获取对方的ip/port
    dest_ip = input("请输入对方的ip:")
    dest_port = int(input("请输入对方的port:"))

    # 从键盘获取数据
    send_data = input("请输入您要发送的任意数据：")
        

    # 使用套接字可以收发数据 
    # udp_socket.sendto(b"hello", ("192.168.159.31", 8080))
    # 之前只能发送byte类型数据，现在可以发送将数据的编码设置为utf-8模式，可以发送所有语言,在这里受网络调试助手软件的影响，选用gbk编码或gbk2312
    udp_socket.sendto(send_data.encode("gbk"), (dest_ip, dest_port))

    # 接收数据,接收阻塞在此
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data)

    # 关闭套接字
    udp_socket.close

# 测试代码段
if __name__ == "__main__":
    main()
