"""
Write a python program to store repeated values in a tuple and count how many times a given value
appear
"""
my_tuple = (1,2,3,1,2,3,4,5,2)
value = int(input("Enter a value: "))
count = 0
for i in my_tuple:
    if(value == my_tuple[i]):
        count += 1
        
print("Frequency: ",count)
        
