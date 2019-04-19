# 利用参数实现对不同函数对象验证的权限不一样
# 缺点：一旦某个函数权限要修改，要修改之前所有的调用
# 改进：使用带有参数的装饰器


# 最外面一层set_level用来保存参数
# 里面的那层set_func用来保存函数引用
# 最里面的函数call_func去调用外一层的函数set_func去使用最外层的参数level_num

# 通用装饰器
def set_level(level_num):
    def set_func(func):
        def call_func(*args, **kwargs):
            if level_num == 1:
                print("权限级别1-验证")
            elif level_num == 2:
                print("权限级别2-验证")
            return func()
        return call_func
    return set_func

# 1.表示调用set_func并且将1 当做实参传递
# 2.用上一步的返回值 就是set_func闭包的引用 当做装饰器对test1函数进行装饰
@set_level(1)
# set_func进行装饰
def test1():
    print("---test1---")
    return "test1 OK"

@set_level(2)
def test2():
    print("---test2---")
    return "test2 OK"

test1()
test2()
