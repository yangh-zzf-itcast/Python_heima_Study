from django.shortcuts import render, redirect
from django.template import loader, RequestContext
from django.http import HttpResponse
from booktest.models import BookInfo

# 设置用户是否登录的权限设置
def login_required(view_func):
    """登录判断装饰器"""
    def wrapper(request, *view_args, **view_kwargs):
        # 进行用户是否登录的判断
        if request.session.has_key('islogin'):
            # 用户已登录，调用对应视图
            return view_func(request, *view_args, **view_kwargs)
        else:
            # 用户未登录，跳转到登陆页
            return redirect('/login')
    return wrapper
   

# Create your views here.

def my_render(request, templates_path, context={}):
    # 1.加载模板文件,获取一个模板对象
    temp = loader.get_template(templates_path)

    # 2.定义模板上下文，给模板文件传数据
    context = RequestContext(request, context)

    # 3.模板渲染，产生一个替换后的html内容
    res_html = temp.render(context)

    # 4.返回应答
    return HttpResponse(res_html)


def index(request):
    # return my_render(request, 'booktest/index.html')
    return render(request, 'booktest/index.html')

def index2(request):
    """模板文件的加载顺序"""
    return render(request, 'booktest/index2.html')

# 模板变量
# /temp_var
def temp_var(request):
    """模板变量"""
    my_dict = {
            'title':'字典键值'
            }
    my_list = [1, 2, 3]

    book = BookInfo.objects.get(id=1)

    # 定义模板上下文
    context = {
            'my_dict': my_dict,
            'my_list': my_list,
            'book': book
            }

    return render(request, 'booktest/temp_var.html', context)

# 模板标签
# /temp_tags
def temp_tags(request):
    """模板标签"""
    books = BookInfo.objects.all()
    return render(request, 'booktest/temp_tags.html',{
        'books':books
        })

# 模板过滤器
# /temp_filter
def temp_filter(request):
    """模板过滤器"""
    books = BookInfo.objects.all()
    return render(request, 'booktest/temp_filter.html',{
        'books':books
        })

# /temp_inherit
def temp_inherit(request):
    """模板继承"""
    return render(request, 'booktest/child.html')

# /html_escape
def html_escape(request):
    """html转义"""
    return render(request, 'booktest/html_escape.html', {
        'content':'<h1>hello</h1>'
        })

# /login
def login(request):
    """显示登录页面"""
    # 访问前先判断用户是否登录
    if request.session.has_key('islogin'):
        # 用户已经登陆的话，就跳转到修改密码页面
        return redirect('/change_pwd')
    else:
        # 用户未登录
        # 获取cookie username
        if 'username' in request.COOKIES:
            # 获取记住的用户名和密码
            username = request.COOKIES['username']
        else:
            username = ''

        return render(request, 'booktest/login.html', {'username':username})


def login_check(request):
    """登录校验"""
    # 1.获取提交的用户和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username+':'+password)
    
    # 获取是否保存用户名密码
    remember = request.POST.get('remember')
    print(remember)

    # 获取用户输入的图片验证码
    vcode = request.POST.get('vcode')
    # 获取session中的保存的验证码
    s_vcode = request.session.get('verifycode')

    # 首先进行验证码的校验
    if vcode != s_vcode:
        # 验证码错误，跳回登录页面
        return redirect('/login')

    # 2.进行登录校验
    if username == 'zzf' and password == '123':
        # 用户名和密码正确，跳转到修改新密码页面
        response = redirect('/change_pwd')
        # 判断是否需要记住用户名, 让cookie的保存时间为一周
        if remember == 'on':
            response.set_cookie('username', username, max_age=7*24*3600)

        # 设置用户登录状态
        # 只要session中有islogin，就认为用户已经登陆
        request.session['islogin'] = True
        # 服务器中记住登录的用户名
        request.session['username'] = username

        return response 
    else:
        # 用户名或密码错误，重新回到登录页面
        return redirect('/login')

# /change_pwd
@login_required
def change_pwd(request):
    """显示修改密码页面"""
    # # 进行用户是否登录的判断
    # if not request.session.has_key('islogin'):
    #     # 用户未登录，跳转到登陆页
    #     return redirect('/login')
    return render(request, 'booktest/change_pwd.html')

# /change_pwd_action
@login_required
def change_pwd_action(request):
    """模拟修改密码处理"""
    # # 进行用户是否登录的判断
    # if not request.session.has_key('islogin'):
    #     # 用户未登录，跳转到登陆页
    #     return redirect('/login')
     
    # 1.获取新密码
    password = request.POST.get('password')
    # 获取用户名
    username = request.session.get('username')

    # 2.实际开发中：修改对应的数据库中的内容
    # 3.返回一个应答
    return HttpResponse('%s修改密码为：%s' % (username, password))


# 给登录页面加上图片验证码, 防止暴力请求
# 要使用PIL 需要先pip3 pillow库
from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO

# /verify_code
def verify_code(request):
    # 1.引入随机函数模块
    import random
    # 2.定义颜色变量RGB
    bgcolor = (random.randrange(20, 100), random.randrange(20, 100), 255)
    width = 100
    height = 25
    # 3.创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 4.创建画笔对象
    draw = ImageDraw.Draw(im)
    # 5.调用画笔中的point函数 绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 6.定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 7.随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 8.构造字体对象
    font = ImageFont.truetype('FreeMono.ttf', 23)
    # 9.构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 10.绘制4个值
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)

    # 11.释放画笔
    del draw
    # 12.将验证码存入session，用于进一步验证
    request.session['verifycode'] = rand_str
    # 13.内存文件操作
    buf = BytesIO()
    # 14.将图片保存在内存中，类型为png
    im.save(buf, 'png')
    # 15.将内存中的图像数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')

# /url_reverse
def url_reverse(request):
    """#url反向解析"""
    return render(request, 'booktest/url_reverse.html')


def show_args(request, a, b):
    return HttpResponse(a+b)

def show_kwargs(request, c, d):
    return HttpResponse(c+d)

from django.core.urlresolvers import reverse
# /test_redirect
def test_redirect(request):
    # 重定向到/index
    # return redirect('/index')
    # url = reverse('booktest:index')
    # 带位置参数的url反向解析 /show_args/1/2
    # url = reverse('booktest:show_args', args=(1,2))
    # 带关键字参数的url反向解析 /show_kwargs/3/4
    url = reverse('booktest:show_kwargs', kwargs={'c':3,'d':4})
    
    return redirect(url)
