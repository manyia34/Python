a = int(input("Enter first number: "))
b = int(input("Enter Second number: "))
num1,num2 = a,b
while b != 0:
    remainder = a % b
    a = b
    b = remainder
    
print(f"The GCD of {num1} and {num2} is {a}")