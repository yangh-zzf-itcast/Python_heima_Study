from django.db import models

# Create your models here.

class AreaInfo(models.Model):
    """地区模型类"""
    # 地区名称, verbose_name 指定列名
    atitle = models.CharField(verbose_name="地区", max_length=20)
    # 自关联属性
    aParent = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.atitle

    def title(self):
       return self.atitle
    # 让方法对应的列也能进行排序
    title.admin_order_field = 'atitle'
    # 指定方法对应的列名
    title.short_description = '地区名称'

    def parent(self):
        if self.aParent is None:
            return '中国'
        return self.aParent.atitle

    parent.short_description = '父级地区名称'


class PicTest(models.Model):
    """上传图片"""
    goods_pic = models.ImageField(upload_to='booktest')


