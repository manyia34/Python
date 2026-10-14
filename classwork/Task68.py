"""
Create a Product class with the product name , price and quantity . Add an instance method to calculate the total cost
Take these values from the user and display the product name and total cost
"""

class Product: 
    def __init__(self,name,price,quantity):
        self.product_name = name
        self.product_price = price 
        self.product_quantity = quantity
        
    def calculate_cost(self):
        return self.product_price * self.product_quantity
    

pname = input("Enter Product name: ")
pprice = int(input("Enter Product price: "))
pquantity = int(input("Enter Price Quantity: "))

p = Product(pname,pprice,pquantity)
print("product name: ",p.product_name) 
print("Price: ",p.calculate_cost())       