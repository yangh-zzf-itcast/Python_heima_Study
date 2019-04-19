#定义一个闭包
def set_func_one(func):
    print("---开始装饰权限1的功能---")
    def call_func(*args, **kwargs):  
        print("----权限验证1----")
        return func(*args, **kwargs)   
    return call_func


#定义一个闭包
def set_func_two(func):
    print("---开始装饰权限2的功能---")
    def call_func(*args, **kwargs):  
        print("----权限验证2----")
        return func(*args, **kwargs)   
    return call_func

# 多个装饰器进行装饰时，装饰的顺序从下向上封装闭包，调用的顺序从上向下，层层向内
@set_func_one
@set_func_two
def test1(num, *args, **kwargs):
    print("----------test1------------%d" % num)
    print("----------test1------------", args)
    print("----------test1------------", kwargs)
    return "OK"

# 装饰器的原理实现
# ret = set_func(test1)
# ret()


ret = test1(100)  # 100表示实参，是传给call_func(num)的形参num
print(ret)

