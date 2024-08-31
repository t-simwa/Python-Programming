
# Class methods are methods that are bound to the class and not the instance of the class. 
# Static methods do not have access to `self` or `cls`.

# Define a class method named MathOperations:
class MathOperations: 
    # A decorator that defines a class method:
    @classmethod
    # Defines a class method that adds two numbers:
    def add(cls, a, b):
        return a + b 
    
    # A decorator that defines a static method:
    @staticmethod
    # Defines a static method that multiplies two numbers:
    def multiply(a, b):
        return a * b 

# Calls the `add` class method and prints the result:   
print(MathOperations.add(5, 3))       # Output: 8
# Calls the `multiply` static method and prints the result:
print(MathOperations.multiply(5, 3))  # Output: 15 