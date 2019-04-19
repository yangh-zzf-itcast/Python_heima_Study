from django.shortcuts import render
from django.http import HttpResponse
from booktest.models import BookInfo
from django.template import loader, RequestContext


# 可以自定义渲染函数
def my_render(request, template_path, context_dict={}):
    """使用模板文件"""
     # 使用模板文件
    # 1.加载模板文件
    temp = loader.get_template(template_path)
    # 2.定义模板上下文：给模板文件传递数据,放在字典中
    context = RequestContext(request, context_dict)
    # 3.模板渲染，产生标准的html内容
    res_html = temp.render(context)

    return HttpResponse(res_html)


# Create your views here.
# 1.定义视图函数 HttpRequest
# 2.进行url配置，建立url地址和视图的对应关系
# http://127.0.0.1:8000/index
def index(request):
    """进行处理、和M模板类与T模板之间进行交互"""
    # return HttpResponse('yangh love zzf')
    # return my_render(request, './booktest/index.html')
   
    # Django已经封装好了
    return render(request, './booktest/index.html', {'content':'hello world', 'list':list(range(1, 10))})

   
# http://127.0.0.1:8000/index2
def index2(request):
    return HttpResponse('hello python')


def show_books(request):
    """显示图书的信息"""
    # 1.通过M查找图书表中的数据
    books = BookInfo.objects.all()
    # 2.使用模板
    return render(request, 'booktest/show_books.html', {'books':books})

def detail(request, bid):
    """查询图书关联英雄信息"""
    # 1.根据bid查询图书信息
    book = BookInfo.objects.get(id=bid)
    # 2.查询与book关联的英雄信息，一查多
    heros = book.heroinfo_set.all()
    # 3.使用模板
    return render(request, 'booktest/detail.html', {'book':book, 'heros':heros})


