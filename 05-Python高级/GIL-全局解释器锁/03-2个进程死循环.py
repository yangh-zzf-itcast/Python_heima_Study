import multiprocessing

# 子线程死循环
def test():
    while True:
        pass

t1 = multiprocessing.Process(target=test)
t1.start()

# 主线程死循环
while True:
    pass
