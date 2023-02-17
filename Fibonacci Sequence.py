num1 = 0
num2 = 1
nums = int(input("How many numbers in the fibonacci sequence would you like printed out?: "))
for i in range(nums):
    print(num1 + num2)
    if i % 2 == 0:
        num2 = num1 + num2
    else:
        num1 = num1 + num2
    
