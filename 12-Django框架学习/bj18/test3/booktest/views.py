from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse  # json返回ajax请求

# Create your views here.

# request就是HttpRequest类型的对象，包含了浏览器请求的信息
def index(request):
    """首页"""
    return render(request, 'booktest/index.html')


def show_arg(request, num):
    return HttpResponse(num)


def login(request):
    """显示登录页面"""
    return render(request, 'booktest/login.html')

def login_check(request):
    """登录校验"""
    # request.POST  保存POST方式提交的参数, 类型是QueryDict，与字典的区别是一个键可以由多个值，可用[]和get()函数按键来取值, 用get比较好，找不到返回空，不会报错
    # request.GET  保存GET方式提交的参数，类型也是QueryDict
    # 1.获取提交的用户和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username+':'+password)
    # 2.进行登录校验
    # 实际开发的时候，用户名和密码是保存在数据库中的，应该在数据库中查找是否有匹配项
    if username == 'yanghang' and password == 'zf951215':
        # 用户名和密码正确，跳转到首页
        return redirect('/index')  
    else:
        # 用户名或密码错误，重新回到登录页面
        return redirect('/login')

    # 3.返回应答
    # return HttpResponse('OK')


def ajax_test(request):
    """显示ajax页面"""
    return render(request, 'booktest/test_ajax.html')

def ajax_handle(request):
    """ajax请求处理"""
    # 返回的json数据
    return JsonResponse({
        'res':1
        })
