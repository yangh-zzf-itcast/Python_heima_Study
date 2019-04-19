# 利用参数实现对不同函数对象验证的权限不一样
# 缺点：一旦某个函数权限要修改，要修改之前所有的调用

# 通用装饰器
def set_func(func):
    def call_func(*args, **kwargs):
        level = args[0]
        if level == 1:
            print("权限级别1-验证")
        elif level == 2:
            print("权限级别2-验证")
        return func()
    return call_func

@set_func
def test1():
    print("---test1---")
    return "test1 OK"

@set_func
def test2():
    print("---test2---")
    return "test2 OK"

test1(1)
test2(2)
