# 定义元类
class ModelMetaclass(type):
    # 通过__new__方法修改类的属性
    # name 元类修改的类名
    # bases 元类修改的类的基类
    # attrs 元类修改的类的属性
    def __new__(cls, name, bases, attrs):
        mappings = dict()
        # 判断是否需要保存
        for k, v in attrs.items():
            # 判断是否是指定的StingField或者IntergerField的实例对象
            # 将原来类的属性与值的键值对提取出来存在一个新的mapping中
            if isinstance(v, tuple):
                print('Found mapping:%s ==> %s' % (k,v))
                mappings[k] = v

        # 删除这些已经存在于字典中的属性
        for k in mappings.keys():
            attrs.pop(k)

        # 将之前的uid/name/email/password以及对应的对象引用...类名字
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name         # 假设表名和类名一直
        # 将元类修改之后的类对象进行返回
        return type.__new__(cls, name, bases, attrs)

class User(metaclass=ModelMetaclass):
    uid = ('uid', "int unsigned")
    name = ('username', "varchar(30)")
    email = ('email', "varchar(30)")
    password = ('password', "varchar(30)")
    # 当指定元类之后，以上的类属性将不在类中，而是在__mappings__属性指定的字典中存储
    # 经过元类之后，形成新的键值对
    # 以上User类中有
    # __mappiings__ = {
    #         "uid": ('uid', "int unsigned")
    #         "name": ('username', "varchar(30)")
    #         "email": ('email', "varchar(30)")
    #         "password": ('password', "varchar(30)")
    #         }
    # __table__ = "user"
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            # 使用setattr函数设置元类修改后返回的对象的属性与值
            # 不能使用self. 来赋值，这样属性名一直是name
            setattr(self, name, value)

    def save(self):
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            # 将字段-属性名uid/username/email/password依次存入fields列表
            fields.append(v[0])
            # 将原字段uid/name/username/email/password传入的对应的值存入列表中
            args.append(getattr(self, k, None))

        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join([str(i) for i in args]))
        print('SQL: %s' % sql)

        # TODO import pymysql
        # 连接数据库--->execute执行语句------>commit提交----->关闭连接
        

def main():
    u = User(uid=123456, name='yanghang', email='2459846416@qq.com', password='123456pwd')
   
    # print(u.__dict__)
    u.save()

if __name__ == "__main__":
    main()
