# Question:
# Write a Python program to determine whether a student is eligible for a scholarship.
# Condition:
# a) CGPA >= 8.5 and attendance >= 85
# b) OR student has won a national-level competition.

cgpa = float(input("Enter CGPA: "))
attendance = float(input("Enter attendance percentage: "))
competition = input("Won national-level competition? (yes/no): ")

if (cgpa >= 8.5 and attendance >= 85) or competition == "yes":
    print("Student is eligible for the scholarship.")
else:
    print("Student is not eligible for the scholarship.")