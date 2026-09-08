# Question:
# Take roll number like 2024A1R057 and extract admission year,
# program code, and roll number digits using slicing.

roll_no = input("Enter roll number: ")

admission_year = roll_no[:4]
program_code = roll_no[4:7]
roll_number = roll_no[7:]

print("Admission Year:", admission_year)
print("Program Code:", program_code)
print("Roll Number Digits:", roll_number)