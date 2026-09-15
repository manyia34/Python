decimal_num = int(input("Enter a decimal number: "))
if decimal_num == 0:
    binary_str = "0"
else:
    binary_str = ""
    temp_num = decimal_num
    while temp_num > 0:
        remainder = temp_num % 2
        binary_str = str(remainder) + binary_str
        temp_num //= 2
print(f"The binary representation is: {binary_str}")
