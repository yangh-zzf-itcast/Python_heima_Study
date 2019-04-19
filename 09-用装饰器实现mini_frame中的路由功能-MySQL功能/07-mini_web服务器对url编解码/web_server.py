import socket
import re
import multiprocessing
# import dynamic.mini_frame  # 逻辑处理代码模块
import sys

class WSGIServer(object):
    """WSGI服务器类"""
    def __init__(self, port, app, static_path):

        # 框架函数传参
        self.application = app

        # 静态网页路径传参
        self.static_path = static_path

        # 1. 创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 设定套接字选项, 可以重复使用地址
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 2. 绑定 
        self.tcp_server_socket.bind(("", port))

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
                file_name = "/index.html"
                pass

        except IndexError:
            file_name = "/index.html"

        # 2.返回http格式的数据给浏览器
        # 如果请求的资源不是以.html为结尾，那么就认为是静态资源（html/css/js/png，jpg等）
        if not file_name.endswith(".html"):
            try:
                # 静态页面路径
                # f = open("./static" + file_name, "rb")
                f = open(self.static_path + file_name, "rb")
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
           
            # body = "hhhh"
            # if file_name == "/login.py":
            #     body = mini_frame.login()
            # 实现解耦, 在简单框架内进行逻辑处理
            
            #WSGI协议
            env = dict()  # 字典存储浏览器要访问的信息
            env['PATH_INFO'] = file_name

            # body = dynamic.mini_frame.application(env, self.set_response_header)
            
            body = self.application(env, self.set_response_header)
            
            header = "HTTP/1.1 %s\r\n" % self.status
            # 遍历响应头的元组
            for temp in self.headers:
                header +="%s:%s\r\n" % (temp[0], temp[1])
            
            header += "\r\n"

            response = header + body
            tcp_client_socket.send(response.encode("utf-8"))
           
        # 关闭服务套接字
        tcp_client_socket.close()

    # WSGI协议函数
    # 将函数引用传入框架的application函数，获得响应头信息，然后存入实例属性中
    def set_response_header(self, status, headers):
        self.status = status
        # 与服务器相关的信息，在服务器的函数内添加，与框架的信息区分开
        self.headers = [('server:','mini_web v1.0')]
        # 服务器信息与框架信息合并
        self.headers += headers

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
    if len(sys.argv) == 3:
        try:
            port = int(sys.argv[1])
            frame_app_name = sys.argv[2]  # mini_frame:application
        except Exception as ret:
            print("端口输入有误......")
            return
    else:
        print("请按以下方式运行：")
        print("python3 xxx.py 7890 mini_frame:application")
        return
 
    ret = re.match("([^:]+):(.*)", frame_app_name)
    if ret:
        frame_name = ret.group(1)  # 框架名 mini_frame
        app_name = ret.group(2)  # 框架内的函数名 application
    else:
        print("请按以下方式运行：")
        print("python3 xxx.py 7890 mini_frame:application")
        return
    
    # 读取web_server配置文件信息，并读取转为字典
    with open("./web_server.conf") as f:
        conf_info = eval(f.read())

    # ---------关键步骤------------

    # import frame_name ----> 找不到，frame_name.py
    # 将./dynamic 添加到程序找得到的路径列表中
    # 动态页面路径
    # sys.path.append("./dynamic")
    sys.path.append(conf_info['dynamic_path'])

    frame = __import__(frame_name)  # __import__ 可以以变量的形式导入包，返回值标志着 导入的这个模块
    app = getattr(frame, app_name)  # 在这个模块中找app_name这个变量存的函数名对应的属性，返回值app就指向了mini_frame中application这个函数
 
    wsgi_server = WSGIServer(port, app, conf_info['static_path'])
    wsgi_server.run_forever()


if __name__ == "__main__":
    main()
