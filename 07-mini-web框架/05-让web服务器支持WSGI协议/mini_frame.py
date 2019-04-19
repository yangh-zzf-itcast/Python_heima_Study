def application(environ, start_response):
    # 设定http响应头信息，发回给浏览器的格式以及字符编码
    # 只写跟框架有关的响应头信息，不写服务器的
    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])
    return 'Hello World 我爱你'
