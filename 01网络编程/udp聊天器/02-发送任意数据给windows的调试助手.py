import socket

# 使用udp发送数据
def main():
    # 创建一个udp关键字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 从键盘获取数据
    send_data = input("请输入您要发送的任意数据：")
    
    # 使用套接字可以收发数据 
    # udp_socket.sendto(b"hello", ("192.168.159.31", 8080))
    # 之前只能发送byte类型数据，现在可以发送将数据的编码设置为utf-8模式，可以发送所有语言
    udp_socket.sendto(send_data.encode("utf-8"), ("192.168.159.31", 8080))

    # 关闭套接字
    udp_socket.close

# 测试代码段
if __name__ == "__main__":
    main()
