def index():
    
    # 前段人员负责，我们只需要调用前段写好的css/js/html页面即可
    # 复杂的页面，利用这种方式进行展示

    # with open("html页面路径") as f:
    #    content = f.read()
    # return content

    return "这是主页"

def login():
    return "这是登录页"

def application(env, start_response):
    # 设定http响应头信息，发回给浏览器的格式以及字符编码
    # 只写跟框架有关的响应头信息，不写服务器的
    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])

    # 从传入的环境变量字典参数中 获取浏览器请求的文件名
    file_name = env['PATH_INFO']
    if file_name == "/index.py":
        return index()
    elif file_name == "/login.py":
        return login()
    else:
        return 'Hello World 我爱你'
