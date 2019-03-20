import socket

# 使用udp发送数据
def main():
    # 创建一个udp关键字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 使用套接字可以收发数据
    # 在字符串前 加'b' 为将字符串转换为byte类型
    udp_socket.sendto(b"hello", ("192.168.159.31", 8080))

    # 关闭套接字
    udp_socket.close

# 测试代码段
if __name__ == "__main__":
    main()
