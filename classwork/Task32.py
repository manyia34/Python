# Question:
# Write a Python program to simulate a digital lock system.
# The lock asks the user to enter a 4-digit PIN.
# If the PIN is not exactly 4 digits, display an error message.
# If the PIN is correct, the lock opens.
# Otherwise, ask the user to try again.

correct_pin = "1234"

pin = input("Enter 4-digit PIN: ")

if len(pin) != 4 or not pin.isdigit():
    print("Error: PIN must contain exactly 4 digits.")
else:
    if pin == correct_pin:
        print("Correct PIN. Lock opened!")
    else:
        print("Incorrect PIN. Please try again.")