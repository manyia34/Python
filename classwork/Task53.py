"""
Write a menu driven pyton program where the user can add items, remove items, view cart and exit
one is for exit mode
"""

print("<- - - - - - MENU - - - - - ->")
print("1. Add Items ")
print("2. Remove Items ")
print("3. View Cart ")
print("4. Exit ")
print("<- - - - - - - - - - - - - - ->")

cart = []
choice = int(input("Enter choice: "))
if choice == 1:
    item = input("Enter item to add: ")
    cart.append(item)
    print(f"{item} added to cart.")   
elif choice == 2:
    item = input("Enter item to remove: ")
    if item in cart:
        cart.remove(item)
        print(f"{item} removed from cart.")
    else:
        print(f"{item} not found in cart.")      
elif choice == 3:
    if len(cart) == 0:
        print("Cart is empty.")
    else:
        print("Items in cart: ")
        for i in range(len(cart)):
            print(cart[i])
elif choice == 4:
    print("Exit program")
    


