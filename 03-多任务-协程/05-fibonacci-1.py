nums = list()

num1 = 0
num2 = 1
count = 1

while count <= 10:
    nums.append(num1)
    num1, num2 = num2, num1 + num2
    count += 1

for num in nums:
    print(num)
