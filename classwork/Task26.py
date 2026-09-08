# Question:
# Take student full name and roll number.
# Generate email using first 3 letters of first name,
# first 3 letters of last name, and last 3 characters of roll number.

name = input("Enter full name: ")
roll_no = input("Enter roll number: ")

parts = name.split()

first_name = parts[0]
last_name = parts[-1]

email = first_name[:3].lower() + last_name[:3].lower() + roll_no[-3:] + "@college.com"

print("Generated Email:", email)