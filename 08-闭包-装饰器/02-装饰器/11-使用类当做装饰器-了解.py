class Test(object):
    def __init__(self, func):
        self.func = func  # 将传进来的函数引用保存起来作为实例对象用

    def __call__(self):
        print("这里是装饰器添加的功能....")
        return self.func()


@Test  # 相当于get_str = Test(get_str)
def get_str():
    return "haha"

print(get_str())  # 相当于调__call__()方法
