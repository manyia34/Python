"""
Write a Python Program that asks the user to enter a username and password. Yhe user should 
get only 3 attempts. if the correct credientials are entered display "Login successful" and 
stop the loop.  If all attempts are used display "Account locked"
"""

credentials1 = "2024A1R057@MIETJAMMU.IN" 
credentials2 = "Manyia@123"
count = 3
while count > 0:
    email = input("Enter Email: ").upper()
    password = input("Enter Password: ")

    if email == credentials1 and password == credentials2:
        print("Login successful")
        break
    else:
        count -= 1
        if count > 0:
            print(f"Incorrect credentials. You have {count} attempts left.\n")
        else:
            print("Account Locked")                                                
            