# 定义一个闭包
def set_func(func):
    def call_func():
        print("----权限验证1----")
        print("----权限验证2----")
        func()
    return call_func

# 装饰器的作用就是在不修改原函数代码的情况下，修改对函数的调用结果
# 这样符合开放封闭原则，对扩展开放，对修改源代码封闭
@set_func  # 等价于 test1 = set_func(test1) ,将函数名的引用指向发生了改变
def test1():
    print("----------test1------------")

# 装饰器的原理实现
# ret = set_func(test1)
# ret()

test1()
