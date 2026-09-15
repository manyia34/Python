"""
write a python program to check whether the given number is a perfect number.A number is a 
perfect if the sum of its proper divisor is equal to the number itself
"""
num = int(input("Enter a number: "))
divisor_sum = 0
for i in range(1, num):
    if num % i == 0:
        divisor_sum = divisor_sum + i

if divisor_sum == num:
    print(num, "is a perfect number.")
else:
    print(num, "is not a perfect number.")
