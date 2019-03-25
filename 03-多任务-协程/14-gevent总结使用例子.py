import gevent
from gevent import monkey
import random
import time

# 有耗时操作时，将所有耗时操作的代码，换为gevent中自己实现的模块
monkey.patch_all()

def coroutine_work(coroutine_name):
    for i in range(10):
        print(coroutine_name, i)
        time.sleep(random.random())  # 休眠0-1随机


# 将协程对象统一放到一个列表里，等待，每一个线程完成统一结束
gevent.joinall([
    gevent.spawn(coroutine_work, "work1"),
    gevent.spawn(coroutine_work, "work2"),
    gevent.spawn(coroutine_work, "work3")
])
