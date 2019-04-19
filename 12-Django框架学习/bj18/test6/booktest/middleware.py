from django.http import HttpResponse


# 要使用需要在项目的settings.py文件中，注册中间件类
class BlockedIPSMiddleware(object):
    """中间件类"""
    EXCLUDE_IPS = ['127.0.0.2']

    # 中间件函数的定义
    def process_view(self, request, view_func, *view_args, **view_kwargs):
        """在视图函数调用之前，会调用中间件函数"""
        # 获取浏览器端的ip地址                                                
        user_ip = request.META['REMOTE_ADDR']
        print(user_ip)
        # 判断访问浏览器的ip是否在禁止访问首页的列表中！
        if user_ip in BlockedIPSMiddleware.EXCLUDE_IPS:
            return HttpResponse('<h1>Forbidden</h1>')

class TestMiddleware(object):
    """中间件类"""
    def __init__(self):
        """服务器重启之后，接收第一个请求时调用, 刷新网页不再调用"""
        print('-----init-----')

    def process_request(self, request):
        """产生request对象之后，url匹配之前调用"""
        print('-----process_request-----')

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        """url匹配之后，视图函数匹配之前调用，因此有request，视图函数，视图函数参数这些参数"""
        print('-----process_view-----')

    def process_response(self, request, response):
        """在视图函数调用之后，内容返回浏览器之前调用。response是视图函数调用之后的返回值"""
        print('-----process_response-----')
        return response

class ExceptionTest1Middleware(object):
    def process_exception(self, request, exception):
        """视图函数 发生异常时调用"""
        print('-----process_exception1-----')
        print(exception)

class ExceptionTest2Middleware(object):
    def process_exception(self, request, exception):
        """视图函数 发生异常时调用"""
        print('-----process_exception2-----')
        print(exception)
