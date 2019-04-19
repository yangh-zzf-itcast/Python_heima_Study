from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse  # json返回ajax请求
from datetime import datetime, timedelta

# Create your views here.

# request就是HttpRequest类型的对象，包含了浏览器请求的信息
def index(request):
    """首页"""
    return render(request, 'booktest/index.html')


def show_arg(request, num):
    return HttpResponse(num)


def login(request):
    """显示登录页面"""
    # 访问前先判断用户是否登录
    if request.session.has_key('islogin'):
        # 用户已经登陆的话，就跳转到首页
        return redirect('/index')
    else:
        # 用户未登录
        # 获取cookie username
        if 'username' in request.COOKIES:
            # 获取记住的用户名和密码
            username = request.COOKIES['username']
        else:
            username = ''

        if 'password' in request.COOKIES:
            password = request.COOKIES['password']
        else:
            password = ''

        return render(request, 'booktest/login.html', {'username':username, 'password':password})

def login_check(request):
    """登录校验"""
    # request.POST  保存POST方式提交的参数, 类型是QueryDict，与字典的区别是一个键可以由多个值，可用[]和get()函数按键来取值, 用get比较好，找不到返回空，不会报错
    # request.GET  保存GET方式提交的参数，类型也是QueryDict
    # 1.获取提交的用户和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username+':'+password)
    
    # 获取是否保存用户名密码
    remember = request.POST.get('remember')
    print(remember)

    # 2.进行登录校验
    # 实际开发的时候，用户名和密码是保存在数据库中的，应该在数据库中查找是否有匹配项
    if username == 'yanghang' and password == 'zf951215':
        # 用户名和密码正确，跳转到首页
        response = redirect('/index')
        # 判断是否需要记住用户名, 让cookie的保存时间为一周
        if remember == 'on':
            response.set_cookie('username', username, max_age=7*24*3600)
            response.set_cookie('password', password, max_age=7*24*3600)

        # 设置用户登录状态
        # 只要session中有islogin，就认为用户已经登陆
        request.session['islogin'] = True
        return response 
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

def login_ajax(request):
    """ajax登录显示页面"""
    return render(request, 'booktest/login_ajax.html')


def login_ajax_check(request):
    """ajax登录校验"""
    # 1.获取用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')

    # 2.进行校验，返回json数据
    if username == 'yanghang' and password == 'zf951215':
        return JsonResponse({
            'res': 1
            })
    else:
        return JsonResponse({
            'res': 0
            })

def set_cookie(request):
    """设置cookie信息"""
    response = HttpResponse('设置cookie')
    # 设置一个cookie信息，名字为num，值为1, max_age设置cookie存活时间，单位s
    response.set_cookie('num', 1, max_age=14*24*3600)
    # response.set_cookie('num', 1, expires=datetime.now()+timedelta(days=14))
    
    # 返回response
    return response

def get_cookie(request):
    """获取cookie信息"""
    num = request.COOKIES['num']
    return HttpResponse(num)


# session 保存在服务器的django_session表中
def set_session(request):
    """设置session"""
    request.session['username'] = 'smart'
    request.session['age'] = '18'
    return HttpResponse('设置session')

def get_session(request):
    """获取session"""
    username = request.session['username']
    age = request.session['age']
    return HttpResponse(username+':' + str(age))

def clear_session(request):
    """清除session信息"""
    # 删除存储中值的部分
    request.session.clear()
    # 删除整条数据
    # request.session.flush()
    return HttpResponse('清除OK..')
