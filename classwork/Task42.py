"""
Write a python program to repeatedly calculate the sum of digits of a number untill the result 
become a single digit
Example : 9875 -> 9 + 8 + 7 + 5 = 29 -> 2 + 9 = 11 -> 1 + 1 = 2
"""

def get_single_digit_sum(number):
    number = abs(number)
    while number >= 10:
        digit_sum = 0
        while number > 0:
            digit_sum += number % 10  
            number //= 10            
        number = digit_sum            
    return number

try:
    user_input = int(input("Enter an integer: "))
    result = get_single_digit_sum(user_input)
    print(f"The final single-digit sum is: {result}")
except ValueError:
    print("Please enter a valid integer.")


