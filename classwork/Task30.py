# Question:
# Take a password and check length, presence of @,
# and whether first and last characters are different.

password = input("Enter password: ")

length_check = len(password) >= 8
at_check = "@" in password
different_check = password[0] != password[-1]

print("Length is at least 8:", length_check)
print("Contains @:", at_check)
print("First and last characters are different:", different_check)

if length_check and at_check and different_check:
    print("Password is Valid")
else:
    print("Password is Invalid")