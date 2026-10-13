rows = int(input("Enter the number of rows:"))
columns = int(input("Enter the number of columns: "))
matrix = []
for i in range(rows):
    row = []
    for j in range(columns):
        value = int(input(f"Enter value for row {i + 1}, column {j + 1}: "))
        row.append(value)
    matrix.append(row)
    
k = int(input("Enter the value to search for: "))
if k <= 0:
    print("Invalid input")
else:
    for i in range(k-1,rows,k):
        matrix[i].reverse()
    print("Updated matrix:")
    for row in matrix:
        print(row)
    