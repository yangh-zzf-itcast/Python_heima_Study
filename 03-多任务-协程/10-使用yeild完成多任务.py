import time

def task_1():
    while True:
        print("---1---")
        time.sleep(0.5)
        yield


def task_2():
    while True:
        print("---2---")
        time.sleep(0.5)
        yield


def main():
    # 生成器对象
    t1 = task_1()
    t2 = task_2()
    while True:
        # 并发 多任务（交替执行，假的多任务）
        # 先让t1运行一会，遇到yield暂停
        # 然后执行t2，遇到yield暂停
        # 最终t1/t2/t1/...交替运行，实行多任务
        next(t1)
        next(t2)


if __name__ == "__main__":
    main()
