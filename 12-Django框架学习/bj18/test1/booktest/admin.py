from django.contrib import admin
from booktest.models import BookInfo, HeroInfo

# 后台管理模块
# 自定义管理类
class BookInfoAdmin(admin.ModelAdmin):
    """图书模型管理类"""
    list_display = ['id', 'btitle', 'bpub_date']

class HeroInfoAdmin(admin.ModelAdmin):
    """英雄信息管理类"""
    list_display = ['id', 'hname', 'hgender', 'hage', 'hcomment']

# Register your models here.
# 注册模型类
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)

