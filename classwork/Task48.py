"""
Write a python program to input marks of n student in a list Display the highest marks, lowest marks,
Average marks and number of student who passed
"""

n = int(input("Enter the number student: "))
student = []
for i in range(1,n+1):
    marks = int(input(f"Enter marks of {i} Student: "))
    student.append(marks)

# Highest marks
high = student[0]
for i in range(len(student)):
    if student[i] > high:
        high = student[i]
print(f"Highest marks: ",high)

# Lowest marks 
low = student[0]
for i in range(len(student)):
    if student[i] < low:
        low = student[i]
print(f"lowest marks: ",low)

# Average marks
average_marks = 0
for i in range(len(student)):
    average_marks += student[i]

print(f"Average marks: ",average_marks / len(student))     
        
# Total number of student passed 
count = 0
for i in range(len(student)):
    if student[i] >= 33:
        count += 1
    
print(f"Total number of student who passed: ",count)