# Write a Python program to implement a class named BankAccount with the following  requrenments :
'''
# The class should contain two instace variables :
    # Name (Account holder name)
    # Amount (Account balance)
# The class should contain one class varible :
    # ROT(Rate of Interest), initialized to 10.5
# Define a constructor (__init__) that accepts Name and initial Amouunt
# Implement the following instace methods:
    # Display() - displays account holder name and current balance
    # Deposit() - accepts an amount from the user and adds it to balance
    # Withdraw() - accepts an amount from the user and subtracts it from balance
    (Ensure withdrawal is allowed only if sufficient balance exists)
# Create multiple objects and demonstrate all methods.
'''

class BankAccount:
    # Class variable
    ROI = 10.5   # Rate of Interest

    # Constructor
    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    # Display account details
    def Display(self):
        print("Account Holder Name :", self.Name)
        print("Current Balance    :", self.Amount)

    # Deposit money
    def Deposit(self):
        deposit_amount = float(input("Enter amount to deposit: "))
        if deposit_amount > 0:
            self.Amount += deposit_amount
            print("Amount deposited successfully.")
        else:
            print("Invalid deposit amount.")

    # Withdraw money
    def Withdraw(self):
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount <= 0:
            print("Invalid withdrawal amount.")
        elif withdraw_amount > self.Amount:
            print("Insufficient balance.")
        else:
            self.Amount -= withdraw_amount
            print("Amount withdrawn successfully.")


# Creating multiple objects
acc1 = BankAccount("Gaurav", 5000)
acc2 = BankAccount("Rahul", 3000)

# Demonstrating methods for first account
acc1.Display()
acc1.Deposit()
acc1.Withdraw()
acc1.Display()
print("----------------------------")

# Demonstrating methods for second account
acc2.Display()
acc2.Deposit()
acc2.Withdraw()
acc2.Display()
