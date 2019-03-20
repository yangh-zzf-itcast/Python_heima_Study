import threading
import time


def test1():
	for i in range(5):
		print("--------test1-------%d--------" % i)
		time.sleep(1)
		

def test2():
	for i in range(5):
		print("--------test2-------%d--------" % i)
		time.sleep(1)


# 主线程等所有的子线程结束之后才会结束
# 主线程结束就代表程序运行完毕
# 如果不小心主线程死了，那子线程也都直接结束
def main():
	t1 = threading.Thread(target=test1)
	t2 = threading.Thread(target=test2)
	
	# 子线程从线程对象调用start开始执行
	# 线程对应的函数执行结束，该线程结束
	t1.start()
	t2.start()
	
	while True:
		print(threading.enumerate())	# 查看当前线程数
		if len(threading.enumerate())<=1
			break
		time.sleep(1)


if __name__ == "__main__":
	main()	