from django.conf.urls import url
from booktest import views

# index
# index2
# 在应用的urls文件中进行url配置时
# 1. 严格匹配开头与结尾


urlpatterns = [
    # 通过url函数来设置url路由配置项
    url(r'^index$', views.index),  # 建立/index和视图index之间的关系
    url(r'^index2$', views.index2),  # 建立/index2和视图index2之间的关系
    url(r'^books$', views.show_books),  # 显示图书信息
    url(r'^books/(\d+)$', views.detail),  # 显示英雄信息
]
