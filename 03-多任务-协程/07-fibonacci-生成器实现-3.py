# 生成器是一类特殊的迭代器
# 可以调用iter ，next函数


def Fibonacci(all_num):
    print("---1---")
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        print("---2---")
        # 如果一个函数中任意地方有yield语句，那么这个就不再是函数，而是一个生成器模板类
        yield a
        print("---3---")
        a, b = b, a + b
        current_num += 1
        print("---4---")
    
    return "---ok--"


# 如果在调用的时候，发现函数中有yield，那么此时不再是调用函数，而是创建一个生成器对象
fibo = Fibonacci(10)

fibo = Fibonacci(2)  # 可以创建多个生成器对象，彼此之间互不影响

result = next(fibo)
print(result)

result = next(fibo)
print(result)

# for num in fibo:
#    print(num)
