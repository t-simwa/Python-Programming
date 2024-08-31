
# Create a class `Account` with the following:
# Private instance attributes: `__account_number`, `__balance`.
# Methods: `deposit`, `withdraw`, and `get_balance` to encapsulate account operations.

class Account: 
    def __init__(self, account_number, balance=0): 
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount): 
        if amount > 0:
            self.__balance += amount
            return f"New balance after deposit: {self.__balance}."
        return "Invalid amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"New balance after withdrawal: {self.__balance}."
        return "Invalid amount"
    
    def get_balance(self):
        return f"Your account balance is: {self.__balance}."
    
account = Account("19S01ACS025", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())