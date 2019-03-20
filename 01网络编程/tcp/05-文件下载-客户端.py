import socket

# 发送文件内容
def send_file_2_client(new_client_socket, new_client_addr):
    
    # 5.接收客户端要下载的文件
    file_name = new_client_socket.recv(1024).decode("utf-8")
    print("客户端(%s)要下载的文件是：%s " % (str(new_client_addr), file_name))

    file_content = None
    # 需要判断读文件的时候是不是打得开这个文件，用try捕获异常，不用with
    try:
        f = open(file_name, "rb")
        file_content = f.read()
    except Exception as ret:
        print("没有要下载的文件(%s)" % file_name)

    if file_content:
        # 6.发送文件的内容给客户端
        # new_client_socket.send("您好!".encode("gbk"))
        new_client_socket.send(file_content)
    

def main():
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2.绑定服务端地址
    tcp_server_socket.bind(("", 7890))

    # 3.监听，将默认的套接字由主动变为被动
    # 最大允许同时连接的客户端
    tcp_server_socket.listen(128)

    while True:
        # 4.等待客户端的链接
        # 返回一个为客户端服务的新的套接字 与 客户端的地址(元组)ip/port
        # 新的套接字负责为这个客户端收发数据，与客户端通信作用
        # 老的套接字 tcp_server_socket 负责继续监听另外的客户端
        new_client_socket, new_client_addr = tcp_server_socket.accept()
        print(new_client_addr)
       
        # 发送文件函数，为客户端服务
        send_file_2_client(new_client_socket, new_client_addr)

        # 关闭完成服务的客户端套接字
        new_client_socket.close()
    
    # 关闭服务器套接字
    tcp_server_socket.close()



if __name__ == "__main__":
    main()
