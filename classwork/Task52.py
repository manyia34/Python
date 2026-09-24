"""
write a python program to rotate a list one position to the right
"""

n = int(input("Enter the number of element: "))
list = []
for i in range(0,n):
    element = int(input(f"Enter element {i}: "))
    list.append(element)
    
# Rotate the list one position to the right
if n > 0:
    last_element = list[-1]
    for i in range(n-1, 0, -1):
        list[i] = list[i-1]
    list[0] = last_element

print("List after rotating one position to the right:")
for i in range(n):
    print(list[i], end=" ")