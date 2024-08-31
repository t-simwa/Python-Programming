
# Encapsulation restricts direct access to some of the object's components, which can prevent the accidental modification of data. 

# Define a class named BankAccount:
class BankAccount: 
    def __init__(self, owner, balance=0):
        self.owner = owner
        # Defines a private instance attribute named `__balance`:
        self.__balance = balance

    # Instance method to deposit money:
    def deposit(self, amount):
        if amount > 0: 
            # Adds the amount to `__balance` if it is greater than 0:
            self.__balance += amount
            return True
        return False
    
    # Instance Method to get the balance:
    def get_balance(self):
        # Returns the value of `__balance`.
        return self.__balance
    
# Creates an instance of the `BankAccount` class with an initial balance of 1000:
account = BankAccount("Ted", 1000)

# Calls the `deposit` method to add 500 to the balance:
account.deposit(500)

# Calls the `get_balance` method and prints the balance:
print(account.get_balance())   # Output: 1500


    