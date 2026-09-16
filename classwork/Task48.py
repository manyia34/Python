"""
Write a python program to input marks of n student in a list Display the highest marks, lowest marks,
Average marks and number of student who passed
"""

n = int(input("Enter the number student: "))
student = []
for i in range(0,n):
    marks = int(input(f"Enter marks of {i} Student: "))
    student.append(marks)

total_student = len(student)

# Highest marks
high = student[0]
for i in total_student: