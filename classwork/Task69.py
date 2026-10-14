class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        
    def deposit(self,amount):
        self.balance = self.balance + amount
        
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Widhdrawl Successful")
        else:
            print("Insufficient balance")
            
    def show_balance(self):
        print("Account holder: ",self.name)
        print("Balance: ",self.balance)
        
        
name = input("Enter Account holder name: ")
balance = float(input("Enter opening balance: "))

account = BankAccount(name,balance)

deposit_amount = float(input("Enter amount to deposit: "))
account.deposit(deposit_amount)

withdrawl_amount = float(input("Enter amount to withdrawl: "))
account.withdraw(withdrawl_amount)

account.show_balance()
