import gevent
import time
from gevent import monkey

# 将程序中所有耗时操作的代码换位gevent中自己实现的代码
monkey.patch_all()  


def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)  # 这种延时无法实现gevent多任务
        # gevent.sleep(0.5)

def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)
        # gevent.sleep(0.5)


def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)
        # gevent.sleep(0.5)

# 创建gevent对象
print("---1---")
g1 = gevent.spawn(f1, 5)
print("---2---")
g2 = gevent.spawn(f2, 5)
print("---3---")
g3 = gevent.spawn(f3, 5)
print("---4---")

g1.join()  # 等待g1执行完
g2.join()
g3.join()
