from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^static_test$', views.static_test),  # 显示图片        
    
    url(r'^index$', views.index),  # 首页
    
    url(r'^show_upload$', views.show_upload),  # 显示上传图片页面

    url(r'^upload_handle$', views.upload_handle),  # 处理获取到的图片
    
    url(r'^show_area(?P<pindex>\d*)$', views.show_area),  # 分页显示

    url(r'^areas$', views.areas),  # 省市县选择案例    

    url(r'^prov$', views.prov),  # 返回省级地区信息

    url(r'city(\d+)$', views.city),  # 获取省下面的市的信息
    
    url(r'dis(\d+)$', views.city),  # 获取市下面的县区的信息,逻辑一样，对应相同的视图函数即可
]
