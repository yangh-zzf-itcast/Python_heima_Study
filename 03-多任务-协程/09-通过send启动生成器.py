# 生成器是一类特殊的迭代器
# 可以调用iter ，next函数


def Fibonacci(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        # 如果一个函数中任意地方有yield语句，那么这个就不再是函数，而是一个生成器模板类
        ret = yield a
        print(">>ret>>", ret)
        a, b = b, a + b
        current_num += 1
    
    return "---ok---"

# 如果在调用的时候，发现函数中有yield，那么此时不再是调用函数，而是创建一个生成器对象
fibo = Fibonacci(25)

# 调用生成器的两种方式
ret = next(fibo)
print(ret)

# 用生成器对象调用send函数也可以获得结果
# send可以传递参数
# 获取到的参数可以影响生成器的状态
ret = fibo.send(2)
print(ret)
