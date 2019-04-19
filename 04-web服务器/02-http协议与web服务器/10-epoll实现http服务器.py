import socket
import re
import select


def service_client(tcp_client_socket, request):
    """为客户端服务"""

    # 1. 接收浏览器发送过来的 http 请求
    # GET /index.html HTTP/1.1
    # ......
    # 
    # 请求数据内容，对数据内容进行解码
    # request = tcp_client_socket.recv(1024).decode("utf-8")

    print(request)

    # 对接收到的请求协议字符串进行按行切割
    # 返回的是由每一行组成的一个列表
    request_lines = request.splitlines()

    # 第一行就是http请求头，其中有浏览器需要访问的文件名
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    # 获取文件名 /index.html
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"
    else:
        pass
    
    try:
        f = open("./html" + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "------file not found------"
        tcp_client_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        # 2. 返回http格式的应答数据 给浏览器
        # 2.1 发给浏览器的数据----header
        # 注意末尾换行一定要加上\r\n 表示换行               

        response_body = html_content

        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"  # 在协议头和 请求的数据之间有一个空行

        response = response_header.encode("utf-8") + response_body
        
        # 发送客户端 http请求头 + 请求的内容
        tcp_client_socket.send(response)   
    
    # 长连接，不关闭套接字
    # 关闭服务套接字
    # tcp_client_socket.close()


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
    tcp_server_socket.setblocking(False)  # 将套接字变为非堵塞

    # 创建一个epoll对象, 创建一个共享内存
    epl = select.epoll()

    # 将监听套接字对应的文件描述符fd 注册到epoll中,监听读事件
    epl.register(tcp_server_socket.fileno(), select.EPOLLIN)

    # 接收到的客户端套接字与文件描述符对应 字典
    # 后面客户端监听到事件后，要recv数据时使用
    fd_event_dict = dict()

    while True:
       # 返回值是一个元组列表 [(fd, event), ()..]包含文件描述符和监听事件 
        fd_event_list = epl.poll()  # 默认堵塞，知道 os检测到数据到来，通过事件通知告诉程序，此时才会解堵塞
        for fd, event in fd_event_list:
            # 服务器的监听套接字发生事件，说明有客户端连接到来
            if fd == tcp_server_socket.fileno():
                # 4. 等待新客户端的连接
                new_socket, client_addr = tcp_server_socket.accept()
                # 将监听fd 监听到的客户端的fd 注册到epoll中，监听读事件
                epl.register(new_socket.fileno(), select.EPOLLIN)
                fd_event_dict[new_socket.fileno()] = new_socket
            # 说明客户端的套接字有读事件发生
            elif event == select.EPOLLIN:
                # 判断客户是否有数据发过来
                recv_data = fd_event_dict[fd].recv(1024).decode("utf-8")
                if recv_data:
                    service_client(fd_event_dict[fd], recv_data)
                else:
                    fd_event_dict[fd].close()
                    # 将关闭了的客户端套接字从epoll内存映射区中移除
                    epl.unregister(fd)
                    del fd_event_dict[fd]

    # 关闭监听套接字
    tcp_server_socket.close()

if __name__ == "__main__":
    main()
