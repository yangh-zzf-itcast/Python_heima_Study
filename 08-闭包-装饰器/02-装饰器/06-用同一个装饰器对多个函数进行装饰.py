# 定义一个闭包
def set_func(func):
    def call_func(num):  # 这个形参num是传给func(num)的，也就是test1(num)的形参
        print("----权限验证1----")
        print("----权限验证2----")
        func(num)   # 传给test1(num)
    return call_func

# 装饰器的作用就是在不修改原函数代码的情况下，修改对函数的调用结果
# 这样符合开放封闭原则，对扩展开放，对修改源代码封闭
@set_func  # 等价于 test1 = set_func(test1) ,将函数名的引用指向发生了改变
def test1(num):
    print("----------test1------------%d" % num)

# 装饰器的原理实现
# ret = set_func(test1)
# ret()

@set_func
def test2(num):
    print("------------test2----------%d" % num)

test1(100)  # 100表示实参，是传给call_func(num)的形参num
test2(200)
