import time
from greenlet import greenlet

# 在两个函数里面来回切换，自动实现了while Ture循环多任务
def task_1():
    while True:
        print("---1---")
        time.sleep(0.5)
        gr2.switch()


def task_2():
    while True:
        print("---2---")
        time.sleep(0.5)
        gr1.switch()

# 生成器greenlet对象
gr1 = greenlet(task_1)
gr2 = greenlet(task_2)

def main():
    # 切换到gr1中运行
    gr1.switch()

if __name__ == "__main__":
    main()
