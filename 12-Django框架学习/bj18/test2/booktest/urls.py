from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^index', views.index),  # 将view视图与图书信息页面对应        
    url(r'^create', views.create),  # 新增图书
    # 正则匹配的()的作用是匹配到会将其作为参数。传递给视图
    url(r'^delete/(\d+)$', views.delete),  # 删除图书
    url(r'^areas', views.areas),  # 自关联地区信息案例
]
