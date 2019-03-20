

num = 100
num2 = [11, 22]

# python中所有的变量本质都是对内存的引用

def test():
	# 在函数内部，需要对全局变量做修改，需要加global
	# 否则不能直接对其进行赋值修改
	global num
	
	num += 100


def test2():
	# 在函数内部，如果是可变变量
	# 可以通过可变变量的方法对其直接进行修改print(num)
	nums.append(33) 


print(num)
print(nums)

test()
test2()

print(num)
print(num2)
