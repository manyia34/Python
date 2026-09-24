"""
Write a python program to count how many times a particular element appears in the list
"""

n = int(input("Enter the number of element: "))
list = []
for i in range(1,n+1):
    e = int(input("Enter the element: "))
    list.append(e)
    
count = 0
search = int(input("Enter the element want to search: "))
for num in list:
    if num == search:
        count = count + 1
        
print("Frequency: ",count)