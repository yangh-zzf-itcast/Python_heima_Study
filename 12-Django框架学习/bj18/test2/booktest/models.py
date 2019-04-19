from django.db import models

class BookInfoManager(models.Manager):
    """图书模型管理类"""
    # 应用1.改变查询的结果集
    def all(self):
        # 1.调用父类的all方法，获取所有数据集Queryset
        books = super().all()
        # 2.对数据进行过滤
        books = books.filter(bisDelete=False)
        # 3.返回过滤后的数据集
        return books

    # 应用2.封装函数：操作模型类对应数据表的（增删改查）
    def create_book(self, btitle, bpub_date):
        # 1.创建一个图书对象
        # book = BookInfo()
        # model属性可以获取self所属的模型类，这样就可以避免模型类名修改的时候对这里造成的影响
        model_class = self.model
        book = model_class()
        # 2.保存进数据库
        book.btitle = btitle
        book.bpub_date = bpub_date
        book.save()
        # 3.返回图书对象
        return book


# 一类对多类的关系

# 一类
# Create your models here.
# 建立模型类
class BookInfo(models.Model):
    """图书模型类"""
    # 图书名称
    btitle = models.CharField(max_length=20)
    # 可以指定唯一，还可以设置索引,可以指定字段名
    # btitle = models.CharField(max_length=20, unique=True, db_index=True, db_column='title')
    # 图书价格, 最大位数为10，小数位数为2
    # bprice = models.DecimalField(max_digits=10, decimal_places=2)
    # 出版日期
    # DateTimeField() 包含年月日-时分秒
    # bpub_date = models.DateField()
    # 自动赋值创建时间
    # bpub_date = models.DateField(auto_now_add=True)
    # 自动复制最后一次修改时间
    bpub_date = models.DateField(auto_now=True)
    # 图书阅读量
    bread = models.IntegerField(default=0)
    # 评论量
    bcomment = models.IntegerField(default=0)
    # 逻辑删除（假的删除,作为一个标记）
    bisDelete = models.BooleanField(default=False)

    # BookInfo.objects.all() ---> BookInfo.book.all()
    # book = models.Manager()  # 自定义一个Manager管理器类对象
    # 这样数据库中的类名不会依赖于应用名
    objects = BookInfoManager()  # 自定义管理器对象

    def __str__(self):
        return self.btitle

    # 定义一个类方法
    @classmethod
    def create_book(cls, btitle, bpub_date):
        # 1.创建一个图书对象
        book = cls()
        # 2.保存进数据库
        book.btitle = btitle
        book.bpub_date = bpub_date
        book.save()
        # 3.返回图书对象
        return book

    class Meta:
        db_table = 'bookinfo'  # 通过元选项指定模型类对应的表名

# 多类
class HeroInfo(models.Model):
    """英雄信息类"""
    # 英雄名
    hname = models.CharField(max_length=20)
    # 性别, 默认男
    hgender = models.BooleanField(default=False)
    # 年龄
    hage = models.PositiveSmallIntegerField(default=30)
    # 英雄备注, 并允许为空，允许为空白
    hcomment = models.CharField(max_length=30, null=True, blank=True)
    # 多类中定义关系属性，设置外键关系
    hbook = models.ForeignKey('BookInfo')
    # 逻辑删除（假的删除,作为一个标记）
    hisDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.hname

# 多类对多类的关系

# 新闻类型类
class NewsType(models.Model):
    """新闻类型"""
    type_name = models.CharField(max_length=20)

# 新闻类
class NewsInfo(models.Model):
    """新闻"""
    title = models.CharField(max_length=128)
    # 发布时间
    pub_date = models.DateTimeField(auto_now_add=True)
    # 信息内容
    content = models.TextField()
    # 多类对多类关联属性，定义在哪个类都可以
    news_type = models.ManyToManyField('NewsType')


# 一类对一类的关系
# 员工基本信息类
class EmployeeBasicInfo(models.Model):
    # 姓名
    name = models.CharField(max_length=20)
    # 性别
    gender = models.BooleanField(default=False)
    # 年龄
    age = models.PositiveSmallIntegerField()

# 员工详细信息类
class EmployeeDetailInfo(models.Model):
    # 详细地址
    addr = models.CharField(max_length=256)
    # 电话号码
    tel = models.CharField(max_length=13)
    # 一类对一类的关系属性，定义在哪个类都可以
    employee_basic = models.OneToOneField('EmployeeBasicInfo')


# 自关联

# 地区模型类
class AreaInfo(models.Model):
    """地区，省市县"""
    # 地区名称
    atitle = models.CharField(max_length=20)
    # 关系属性，代表当前地区的父级地区
    aParent = models.ForeignKey('self', null=True, blank=True)
