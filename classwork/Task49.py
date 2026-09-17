"""
write a python program to input marks of 10 student store only valid marks between 0 and 100 in 
list. Skip invalid marks
"""
student = []
count = 0
for i in range(1,11):
    marks = int(input("Enter marks: "))
    if marks >= 0 and marks <= 100:
        count = count + 1
        student.append(marks)
    
for i in range(count):
    print(student[i])