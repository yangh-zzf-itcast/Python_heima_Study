import time
from collections import Iterable  # 导入可迭代类
from collections import Iterator  # 导入迭代器类

# 有__iter__的类是可迭代类
# 同时有__iter__ 和 __next__ 函数的类是迭代器类

# 定义一个可迭代类兼 迭代器类
class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    # 定义一个__iter__方法，并返回一个带__iter__和__next__方法的迭代器对象的引用
    # 让这个类成为可以迭代的类
    # 可以使用for,会自己调用这个方法
    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            # 迭代完成，抛出异常 停止迭代
            raise StopIteration

classmate = Classmate()

classmate.add("老王")
classmate.add("老张")
classmate.add("老杨")

# print("判断classmate是否是可以迭代的对象：", isinstance(classmate, Iterable))

# 调用iter函数，返回一个迭代器对象
# classmate_iterator = iter(classmate)
# print("判断classmate_iterator是否是迭代器：", isinstance(classmate_iterator, Iterator))
# 调用迭代器的next函数 取返回值
# print(next(classmate_iterator))

# 普通类 不是 可迭代类，执行会报错
for name in classmate:
    print(name)
    time.sleep(1)
