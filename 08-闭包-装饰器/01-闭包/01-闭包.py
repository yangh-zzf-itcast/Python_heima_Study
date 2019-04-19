# 二元函数，计算值

# 方式1
# k = 1
# b = 2
# y = k*x+b
# 缺点：如果需要计算多次，就需要写多次表达式

# 方式2
def line_2(k,b,x):
    print(k*x+b)

line_2(1, 2, 0)
line_2(1, 2, 1)
line_2(1, 2, 2)
# 缺点：如果想要计算多次这条线上的y值，需要多次传递k，b的值，麻烦

print("-" * 50)

# 方式3 全局变量
k = 1
b = 2
def line_3(x):
    print(k*x+b)

line_3(0)
line_3(1)
line_3(2)
k = 11
b = 22
line_3(0)
line_3(1)
line_3(2)
# 缺点：计算多条线上的y值，那么需要每次对全局变量进行修改，代码会增多

print("-" * 50)

# 方式4 函数缺省参数
def line_4(x, k=1, b=2):
    print(k*x+b)

line_4(0)
line_4(1)
line_4(2)

line_4(0, k=11, b=22)
line_4(1, k=11, b=22)
line_4(2, k=11, b=22)

# 优点：比全局变量的方式好在，k，b是line_4函数的一部分，有一定的封装，不会被其他函数修改
# 缺点：如果要计算多条线上，那么需要每次调用的时候传递参数，麻烦

print("-" * 50)

# 方式5 实例对象
class Line5(object):
    def __init__(self, k, b):
        self.k = k
        self.b = b

    def __call__(self, x):
        print(self.k*x+self.b)

line_5_1 = Line5(1, 2)
line_5_1(0)
line_5_1(1)
line_5_1(2)
line_5_2 = Line5(11, 22)
line_5_2(0)
line_5_2(1)
line_5_2(2)
# 缺点：为了计算多条线，所以需要保存多个k，b的值，因此创建了多个实例对象，浪费资源，占用空间

print("-" * 50)

# 方式6  闭包
def line_6(k, b):
    def create_y(x):
        print(k*x+b)
    return create_y  # 返回一个函数对象，创建了一个小空间

line_6_1 = line_6(1, 2)  #创建一个k=1，b=2，还有print(k*x+b)语句的 小空间 
line_6_1(0)
line_6_1(1)
line_6_1(2)
line_6_2 = line_6(11, 22)
line_6_2(0)
line_6_2(1)
line_6_2(2)

# 优点：虽然也需要创建空间，但是比实例对象的空间小很多
# 缺点：只能处理一些简单的代码
