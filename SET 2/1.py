#A program that models a bank account, with classes for the account , the customer, and the bank.


class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")
    
    def get_balance(self):
        return self.balance
    
class Customer:
    def __init__(self, name, account):
        self.name = name
        self.account = account
    
    def deposit_to_account(self, amount):
        self.account.deposit(amount)
    
    def withdraw_from_account(self, amount):
        self.account.withdraw(amount)
    
    def check_balance(self):
        return self.account.get_balance()
    
    def __str__(self):
        return f"Customer {self.name} with Account {self.account.account_number}"


class Bank:
     def __init__(self, name):
        self.name = name
        self.customers = {}
    
     def add_customer(self, customer):
        self.customers[customer.name] = customer
        print(f"Customer {customer.name} added to the bank.")
    
     def get_customer(self, customer_name):
        return self.customers.get(customer_name, None)
    
     def __str__(self):
        return f"Bank: {self.name}, Total Customers: {len(self.customers)}"
# Create a bank instance
my_bank = Bank("My Great Bank")

# Create bank accounts for customers
account1 = BankAccount(account_number="12345", balance=1000)
account2 = BankAccount(account_number="67890", balance=500)

# Create customers and associate them with accounts
customer1 = Customer(name="John Doe", account=account1)
customer2 = Customer(name="Jane Smith", account=account2)

# Add customers to the bank
my_bank.add_customer(customer1)
my_bank.add_customer(customer2)

# Interact with customer accounts
customer1.deposit_to_account(200)
customer2.withdraw_from_account(100)

# Check balance
print(f"{customer1.name}'s balance: {customer1.check_balance()}")
print(f"{customer2.name}'s balance: {customer2.check_balance()}")

# Display the bank's details
print(my_bank)

