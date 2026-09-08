# Question:
# Take name, branch, and year.
# Generate a code name using string concatenation, slicing, and repetition.

name = input("Enter name: ")
branch = input("Enter branch: ")
year = input("Enter year: ")

code_name = name[:3].upper() + branch[:2].upper() + year[-2:] + "X" * 2

print("Code Name:", code_name)