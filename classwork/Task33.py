"""
Write a python program to calculate the final bill amount after applying a discount. The 
program should take the total bill amount as input from the user and apply the discount according to the 
following rules. After calculating the discount the program should display the discount amount 
and the fina bill amount payable by the customer.

Bill Amount                      Discount 
Above 5000                       20 percent 
3000 to 5000                     10 percent 
below 3000                       No discount
"""

bill_amount = int(input("Enter total bill Amount: "))
if bill_amount > 5000: 
    discount = 0.20 * bill_amount
    result_amount = bill_amount - discount
elif bill_amount > 3000 and bill_amount <= 5000:
    discount = 0.10 * bill_amount
    result_amount = bill_amount - discount
else:
    result_amount = bill_amount

print("Discount: ",discount)
print("Final bill need to pay: ",result_amount)

