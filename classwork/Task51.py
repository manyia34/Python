"""
Write a python program to take input numbers in a list and create a two seperate list for even and
odd numbers
"""
n = int(input("Enter the number of element: "))
list = []
for i in range(1,n+1):
    e = int(input(f"Enter element {i}: "))
    list.append(e)
    
odd = []
even = []
for i in range(0,n):
    if list[i] % 2 == 0:
        even.append(list[i])
    else:
        odd.append(list[i])
    
print("Odd list: ")
for i in range(len(odd)):
    print(odd[i],end=" ")
   
print("Even list: ") 
for i in range(len(even)):
    print(even[i],end=" ")
    
