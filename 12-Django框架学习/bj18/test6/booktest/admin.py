from django.contrib import admin
from booktest.models import AreaInfo, PicTest

# 关联关系的显示
class AreaStackedInline(admin.StackedInline):
    # 写多类的名字
    model = AreaInfo

    extra = 2  # 额外的空白行


class AreaTabularInline(admin.TabularInline):
    model = AreaInfo
    extra = 2

class AreaInfoAdmin(admin.ModelAdmin):
    """地区模型管理类"""
    list_per_page = 10  # 指定每一页显示10条数据
    list_display = ['id', 'atitle', 'title', 'parent']
    actions_on_bottom = True  # 底部也有一个下拉框
    actions_on_top = False  # 上部也有一个下拉框隐藏掉
    list_filter = ['atitle']  # 列表页右侧过滤栏
    search_fields = ['atitle']  # 列表页上方搜索框

    # fields = ['aParent', 'atitle']  # 指定字段显示的顺序
    fieldsets = (
            ('基本',{'fields':['atitle']}),
            ('高级',{'fields':['aParent']}),
            )

    # inlines = [AreaStackedInline]
    inlines = [AreaTabularInline]

# Register your models here.
admin.site.register(AreaInfo, AreaInfoAdmin)
admin.site.register(PicTest)
