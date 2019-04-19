from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^index$', views.index),  # 首页 
    # url(r'^showarg(\d+)$', views.show_arg),  # 利用正则匹配捕获url参数,位子参数
   
    # 关键字参数的组名，这里是num 要与视图中的参数的名字保持一致，否则报错
    url(r'^showarg(?P<num>\d+)$', views.show_arg),  # 利用正则匹配捕获url参数,关键字参数

    url(r'^login$', views.login),  # 显示登录页面    
     
    url(r'^login_check$', views.login_check),  # 用户登录校验   

    url(r'^test_ajax$', views.ajax_test),  # 显示ajax页面    

    url(r'^ajax_handle$', views.ajax_handle),  # ajax处理
]
