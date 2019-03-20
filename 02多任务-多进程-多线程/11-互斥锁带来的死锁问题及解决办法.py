import threading
import time

# 创建两个互斥锁
mutexA = threading.Lock()
mutexB = threading.Lock()

# 当一个线程要占用多个共享资源时，系统资源的竞争或县城运行顺序不合适，可能会发生死锁现象
# 解决方法：1.给锁加时限，超过一定时间访问不到就跳过
# 2.银行家算法，事先银行家算法通过对进程需求、占有和系统拥有资源的实时统计，
# 确保系统在分配给进程资源不会造成死锁才会给与分配。

class MyThread1(threading.Thread):
	def run(self):
		# 对mutexA上锁
		mutexA.acquire()
		
		# 对mutexA上锁后，延时1s，等待另外那个线程，把mutexB上锁
		print(self.name+'----------do1-------up------')
		time.sleep(1)
		
		# 此时会在这里堵塞，因为mutexB已经被另外一个线程抢先上锁
		mutexB.acquire()
		print(self.name+'----------do1-------down------')
		
		mutexB.release()
		
		# 对mutexA解锁
		mutexA.release()
		
		
class MyThread2(threading.Thread):
	def run(self):
		# 对mutexB上锁
		mutexB.acquire()
		
		# 对mutexB上锁后，延时1s，等待另外那个线程，把mutexA上锁
		print(self.name+'----------do2-------up------')
		time.sleep(1)
		
		# 此时会在这里堵塞，因为mutexA已经被另外一个线程抢先上锁
		mutexA.acquire()
		print(self.name+'----------do2-------down------')
		
		mutexA.release()
		
		# 对mutexB解锁
		mutexB.release()
	
	
def main():
	t1 = MyThread1()
	t2 = MyThread2()
	
	t1.start()
	t2.start()
	
if __name__ == "__main__":
	main()