import socket


def main():
    # 1.创建tcp套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
    # 2.连接服务器
    # tcp_socket.connect(("127.0.0.1", 9000))
    server_ip = input("请输入要连接的服务器ip:")
    server_port = int(input("请输入要连接的服务器的端口:"))
    server_addr = (server_ip, server_port)
    tcp_socket.connect(server_addr)
                           
    # 3.发送给服务器要下载的文件名
    download_filename = input("请输入要下载的文件名：")
    tcp_socket.send(download_filename.encode("gbk"))

    # 4.接收文件中数据
    recv_data = tcp_socket.recv(1024)

    # 5.保存文件数据到新的文件中
    # 使用 with ... as ...语句来打开读写文件，可以防止打开文件正常，而在读写操作时发生的异常，使用try..except..语句太复杂，with语句更简洁，发生异常会自动关闭文件
    if recv_data:
        with open("[新]" + download_filename, "wb") as f:
            f.write(recv_data)

    # 6.关闭套接字
    tcp_socket.close()                      
       
       
if __name__ == "__main__":
    main()
