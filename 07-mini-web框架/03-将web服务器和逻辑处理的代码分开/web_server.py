import socket
import re
import multiprocessing
import mini_frame  # 逻辑处理代码模块


class WSGIServer(object):
    """WSGI服务器类"""
    def __init__(self):
        # 1. 创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 设定套接字选项, 可以重复使用地址
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 2. 绑定 
        self.tcp_server_socket.bind(("", 7890))

        # 3. 监听
        self.tcp_server_socket.listen(128)
       
    
    def service_client(self, tcp_client_socket):
        """为客户端服务"""

        # 1. 接收浏览器发送过来的 http 请求
        # GET /index.html HTTP/1.1
        # ......
        # 
        # 请求数据内容，对数据内容进行解码
        request = tcp_client_socket.recv(1024).decode("utf-8")
        print(request)

        try:
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
        
        except IndexError:
            pass

        # 2.返回http格式的数据给浏览器
        # 如果请求的资源不是以.py为结尾，那么就认为是静态资源（html/css/js/png，jpg等）
        if not file_name.endswith(".py"):
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
                # 2.1 发给浏览器的数据----header
                # 注意末尾换行一定要加上\r\n 表示换行                   
                response = "HTTP/1.1 200 OK\r\n"
                response += "\r\n"  # 在协议头和 请求的数据之间有一个空行

                # 2.2 发给浏览器的数据----body 
                # response += "<h1>YangHang love ZhangZifan</h1>"
                
                # 发送回应头
                tcp_client_socket.send(response.encode("utf-8"))
                # 发送客户端请求的内容
                tcp_client_socket.send(html_content)
        else:
            # 如果是以.py结尾，那么就认为是动态资源请求
            header = "HTTP/1.1 200 OK\r\n"
            header += "\r\n"

            # body = "hhhh"
            body = mini_frame.login()

            response = header + body
            tcp_client_socket.send(response.encode("utf-8"))
           
        # 关闭服务套接字
        tcp_client_socket.close()

    def run_forever(self):
        """完成服务器的整体控制，无限循环运行"""                     
        while True:
            # 4. 等待新客户端的连接
            new_socket, client_addr = self.tcp_server_socket.accept()

            # 5. 创建一个子进程为这个客户端服务
            p = multiprocessing.Process(target=self.service_client, args=(new_socket, ))
            p.start()    
            
            # 关闭父进程中的 new_socket 
            new_socket.close()

        # 关闭监听套接字
        self.tcp_server_socket.close()

def main():
    """控制整体，创建一个web服务器对象，然后调用这个对象的run_forever方法运行"""
    wsgi_server = WSGIServer()
    wsgi_server.run_forever()


if __name__ == "__main__":
    main()
