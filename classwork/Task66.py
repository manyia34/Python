""" 
Create a class and object : student details 
problem: Create a student class to store a students name and roll number . create a object and display the details using an
instance method
"""

class Students: 
    def __init__(self,Name,No):
        self.name = Name
        self.roll_no = No
        
    def display(self):
        print(self.name)
        print(self.roll_no)


student = Students("Manyia Mahajan",57)
student.display()