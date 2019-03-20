import threading
import time

# 线程获取CPU时间片来执行

# 多线程共享全局变量会有一个问题：同时对一个变量进行操作时，发生资源竞争
# 通过线程同步来解决，原子性/原子操作
# 同步就是协同步调，按预定的先后次序
# 互斥锁

# 定义一个全局变量
g_num = 0


# 主线程和子线程之间是共享全局变量的
def test1(num):
	global g_num
	for i in range(num):
		g_num += 1
	print("------------in test1 g_num = %d -----------" % g_num)


def test2(num):
	global g_num
	for i in range(num):
		g_num += 1
	print("------------in test2 g_num = %d -----------" % g_num)

def main():
	# target 指定将来 该县城去哪个函数执行 
	# args 指定传入线程参数，要元组类型
	t1 = threading.Thread(target=test1, args=(100, )) 
	t2 = threading.Thread(target=test2, args=(100, ))
	
	t1.start()
	

	
	t2.start()
	
	time.sleep(5)
	
	# 由于资源竞争，g_num的值最终不是希望的结果
	print("------------in main g_num = %d -----------" % g_num)
	

if __name__ == "__main__":
	main()