''''
Exp 7 : Write a Python program to create n students. Store each student records as a dictionary containing roll number, name, branch, and marks.
Store all records in a list and search for a student using roll number.(Condition : Roll numbers must be unique.)
''' 
students = {}
n = int(input("Enter number of students: "))

for i in range(n):
    roll = input("Roll number: ")
    name = input("Name: ")
    branch = input("Branch: ")
    marks = float(input("Marks: "))

    if roll not in students:
        students[roll] = [name, branch, marks]

roll = input("Enter roll number to search: ")

if roll in students:
    print(students[roll])
else:
    print("Student not found")