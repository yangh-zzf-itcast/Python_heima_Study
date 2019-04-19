import socket


def service_client(tcp_client_socket):
    """为客户端服务"""

    # 1. 接收浏览器发送过来的 http 请求
    # GET / HTTP/1.1
    # ......
    # 
    # 请求数据内容
    request = tcp_client_socket.recv(1024)
    print(request)

    # 2. 返回http格式的应答数据 给浏览器
    # 2.1 发给浏览器的数据----header
    # 注意末尾换行一定要加上\r\n 表示换行                   
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"  # 在协议头和 请求的数据之间有一个空行

    # 2.2 发给浏览器的数据----body 
    response += "<h1>YangHang love ZhangZifan</h1>"
    
    # 发送
    tcp_client_socket.send(response.encode("utf-8"))
 
    # 关闭服务套接字
    tcp_client_socket.close()


def main():
    """完成服务器的整体控制"""
                                      
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    
    # 设定套接字选项
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. 绑定 
    server_ip = ""
    server_port = 7890
    tcp_server_socket.bind((server_ip, server_port))

    # 3. 监听
    tcp_server_socket.listen(128)
    
    while True:
        # 4. 等待新客户端的连接
        new_socket, client_addr = tcp_server_socket.accept()

        # 5. 为这个客户端服务
        service_client(new_socket)

    # 关闭监听套接字
    tcp_server_socket.close()

if __name__ == "__main__":
    main()
