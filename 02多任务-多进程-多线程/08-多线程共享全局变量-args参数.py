import threading
import time

# 多线程共享全局变量会有一个问题：同时对一个变量进行操作时，发生资源竞争

# 定义一个全局变量
g_nums = [11, 22]


# 主线程和子线程之间是共享全局变量的
def test1(temp):
	temp.append(33)
	print("------------in test1 g_nums = %s -----------" % str(temp))


def test2(temp):
	print("------------in test1 g_nums = %s -----------" % str(temp))

def main():
	# target 指定将来 该县城去哪个函数执行 
	# args 指定传入线程参数，要元组类型
	t1 = threading.Thread(target=test1, args=(g_nums, )) 
	t2 = threading.Thread(target=test2)
	
	t1.start()
	
	time.sleep(1)
	
	t2.start()
	
	time.sleep(1)
	
	print("------------in main g_nums = %d -----------" % str(g_nums))
	

if __name__ == "__main__":
	main()