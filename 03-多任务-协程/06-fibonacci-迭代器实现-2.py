class Fibonacci(object):
    def __init__(self, all_num):
        self.all_nums = all_num
        self.count = 0
        self.a = 0
        self.b = 1


    def __iter__(self):
        return self

    
    def __next__(self):
        if self.count < self.all_nums:
            ret = self.a
            self.count += 1
            self.a, self.b = self.b, self.a + self.b
            return ret
        else:
            raise StopIteration

fibo = Fibonacci(10)

for num in fibo:
    print(num)
