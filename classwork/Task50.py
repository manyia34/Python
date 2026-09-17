"""
write a python program to input numbers in a list and find the second largest number
"""

n = int(input("Enter the number of element: "))       
list = []
for i in range(0,n):
    element = int(input(f"Enter element {i}: "))
    list.append(element)
    
list.sort()
print(f"The second largest element is: ",list[-2])