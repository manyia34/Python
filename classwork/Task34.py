"""
write a python program to input marks of 5 students
For each student the program should check whether the entered marks are valid or invalid 
marks are considered valid only if they are between 0 and 100 . If the marks are invalid 
the program should display "Invalid marked skipped" and move the next student without printing those marks 

if the marks are valid the program should display the marks are valid 
"""


for i in range(1,6):
    marks = int(input(f"Enter the marks of the {i} student: "))
    if marks >= 0 and marks <= 100:
        print("Marks are valid")
    else:
        print("Invalid marks skipped")