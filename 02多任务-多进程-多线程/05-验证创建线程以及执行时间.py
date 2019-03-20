import threading
import time


def test1():
	for i in range(5):
		print("--------test1-------%d--------" % i)
		time.sleep(1)
		

def main():

	print(threading.enumerate())
	
	# 线程指定目标为一个函数比较方便
	# 当目标比较复杂时，线程也可以直接指定为一个类，继承于threading.thread类
	# 然后直接创建该类对象，然后可以调用父类的start方法，然后自动先调用该类的run方法
	# 注意一定是run方法，其他方法可以在run方法中调用来实现调用该类中的其他方法
	# 1. t = MyThread()
	# 2. t.start()
	t1 = threading.Thread(target=test1)
	
	print(threading.enumerate())
	t1.start()
	
	print(threading.enumerate())	# 查看当前线程数



if __name__ == "__main__":
	main()	