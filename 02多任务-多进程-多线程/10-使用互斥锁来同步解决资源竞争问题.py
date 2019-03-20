import threading
import time

# 线程获取CPU时间片来执行

# 多线程共享全局变量会有一个问题：同时对一个变量进行操作时，发生资源竞争
# 通过线程同步来解决，原子性/原子操作
# 同步就是协同步调，按预定的先后次序
# 互斥锁

# 定义一个全局变量
g_num = 0

# 创建一个互斥锁，默认是没有上锁的
mutex = threading.Lock()

# 主线程和子线程之间是共享全局变量的
def test1(num):
	global g_num
	
	# 上锁，如果之前没上锁，那么此时上锁成功
	# 如果上锁之前已经被其他线程上锁了，那么会堵塞在这里，直到 这个锁被解开位置
	
	for i in range(num):
		# 重要！！！
		# 加互斥的锁的原则：原子性，保证在锁内的步骤最少
		# 对共享全局变量要操作之前加锁，操作一结束马上解锁！
		mutex.acquire()
		g_num += 1
		# 解锁
		mutex.release()
	
	print("------------in test1 g_num = %d -----------" % g_num)


def test2(num):
	global g_num
	
	for i in range(num):
		mutex.acquire()
		g_num += 1
		mutex.release()
		
	print("------------in test2 g_num = %d -----------" % g_num)

def main():
	# target 指定将来 该县城去哪个函数执行 
	# args 指定传入线程参数，要元组类型
	t1 = threading.Thread(target=test1, args=(1000000, )) 
	t2 = threading.Thread(target=test2, args=(1000000, ))
	
	t1.start()
	

	
	t2.start()
	
	time.sleep(5)
	
	# 由于资源竞争，g_num的值最终不是希望的结果
	print("------------in main g_num = %d -----------" % g_num)
	

if __name__ == "__main__":
	main()
