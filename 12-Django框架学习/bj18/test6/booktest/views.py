from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from booktest.models import PicTest, AreaInfo

# Create your views here.

EXCLUDE_IPS = ['127.0.0.2']
# 禁止受限制的ip访问 权限装饰器
def blocked_ips(view_func):
    def wrapper(request, *view_args, **view_kwargs):
        # 获取浏览器端的ip地址
        user_ip = request.META['REMOTE_ADDR']
        print(user_ip)
        # 判断访问浏览器的ip是否在禁止访问首页的列表中！
        if user_ip in EXCLUDE_IPS:
            return HttpResponse('<h1>Forbidden</h1>')
        return view_func(request, *view_args, **view_kwargs)
    return wrapper


# /static_test.html
def static_test(request):
    print(settings.STATICFILES_FINDERS)
    # ('django.contrib.staticfiles.finders.FileSystemFinder', 'django.contrib.staticfiles.finders.AppDirectoriesFinder')
    return render(request, 'booktest/static.html')

# @blocked_ips
def index(request):
    """首页"""
    print('------index-------')
    # num = 'a' + 1
    return render(request, 'booktest/index.html')

# /show_upload
def show_upload(request):
    """显示上传图片页面"""
    return render(request, 'booktest/upload_pic.html')

# /upload_handle
def upload_handle(request):
    """上传图片处理"""
    # 1.获取上传图片的 处理对象
    pic = request.FILES['pic']
    # print(type(pic))
    # 根据上传文件大小，返回的图片处理对象不一样，不大于2.5M文件放在内存中，返回的是第一个
    # <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
    # 上传文件大于2.5M，文件内容放在临时的一个文件中
    # <class 'django.core.files.uploadedfile.TemporaryUploadedFile'>
    
    # 处理对象有个属性name，用户上传文件的名字, 还可以获取文件大小，文件类型
    # print(pic.name, pic.size, pic.content_type)

    # 处理对象有个方法 chunks(),返回的是一个生成器，可通过遍历读取文件的内容
    # pic.chunks()

    # 2.保存到路径 /static/media/booktest
    # 2.1 创建文件
    save_path = '%s/booktest/%s' % (settings.MEDIA_ROOT, pic.name)
    with open(save_path, 'wb') as f:
        # 2.2 获取上传文件的内容并写入
        for content in pic.chunks():
            f.write(content)

    # 3.在数据库中保存上传记录,使用create方法；也可以创建对象使用save方法
    PicTest.objects.create(goods_pic='booktest/%s' % pic.name)

    # 4.返回应答
    return HttpResponse('ok')


from django.core.paginator import Paginator  # 导入分页类
# /show_area(\d+)
# 前端访问的时候需要传递页码
def show_area(request, pindex):
    """分页"""
    # 1.查询出所有省级地区的信息
    areas = AreaInfo.objects.filter(aParent__atitle='中国')
    
    # 对查询集进行分页，每页显示10条
    paginator = Paginator(areas, 8)
    print(paginator.num_pages)
    print(paginator.page_range)

    # 获取第一页的内容
    # page是Page类的实例对象
    if pindex == '':
        # 默认取第一页内容
        pindex = 1
    else:
        pindex = int(pindex)
    page = paginator.page(pindex)
    print(page.number)

    # 2.使用模板
    # return render(request, 'booktest/show_area.html', {'areas':areas})
    return render(request, 'booktest/show_area.html', {'page':page})

# /areas
def areas(request):
    """省市县选择案例"""
    return render(request, 'booktest/areas.html')

# /prov
def prov(request):
    """获取所有省级地区的信息"""
    # 1.获取地区信息
    areas = AreaInfo.objects.filter(aParent__atitle='中国')
    
    # 查询出来的areas查询集不能直接转换为Json数据格式，直接使用返回会报错
    # 使用变量areas拼接出Json数据：标题atitle，id
    areas_list = []
    for area in areas:
        areas_list.append((area.id, area.atitle))

    # 2.返回数据
    return JsonResponse({
        'data':areas_list
        })

# /city(\d+)
def city(request, pid):
    """获取pid省的下级市的信息"""
    # 1.获取pid对应的省的信息，然后使用一查多的方式查询
    # area = AreaInfo.objects.get(id=pid)
    # area.areainfo_set.all()
    areas = AreaInfo.objects.filter(aParent__id=pid)

    areas_list = []
    for area in areas:
        areas_list.append((area.id, area.atitle))

    # 2.返回数据
    return JsonResponse({
        'data':areas_list
        })


