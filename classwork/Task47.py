"""
Write a python program to print a hallow Square using stars
"""
n = int(input("Enter the size of the square: "))
for i in range(n):   # Rows
    for j in range(n):  # Columns
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()