from django.db import models
# 进行与数据库相关的内容的编写
# Create your models here.
# 设计和表对应的类：模型类


# 一类
# 图书类
class BookInfo(models.Model):
    """图书模型类"""
    # 图书名称 对应字段名 CharField说明是一个字符串，max_length指定字符串最大长度
    btitle = models.CharField(max_length=20)
    # 图书出版日期，DateField说明是一个日期类型
    bpub_date = models.DateField()

    # 重写魔法方法，显示对象相关信息的字符串
    def __str__(self):
        # 返回书名
        return self.btitle


# 多类
# 英雄人物类
# 英雄名 hname
# 性别 hgender
# 年龄 hage
# 备注 hcomment
# 关系属性 hbook  建立图书类与英雄人物之间的一对多的关系
class HeroInfo(models.Model):
    """英雄人物模型类"""
    hname = models.CharField(max_length=20)
    # BooleanField说明是布尔类型，default是默认值，False代表男
    hgender = models.BooleanField(default=False)
    # PositiveSmallIntegerField 说明是 int unsigned 类型 
    hage = models.PositiveSmallIntegerField()
    hcomment = models.CharField(max_length=30)
    # 多类中定义关系属性，设置外键关系
    hbook = models.ForeignKey('BookInfo')

    def __str__(self):
        # 返回英雄名
        return self.hname


