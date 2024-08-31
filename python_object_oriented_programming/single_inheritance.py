
# Single inheritance allows a class to inherit attributes and methods from a single parent class.

# Defines a parent class named Animal:
class Animal: 
    def __init__(self, name):
        self.name = name  # Instance attribute.
    
    # Defines a method that raises an exception if not overridden:
    def speak(self):
        raise NotImplementedError("Sublass must implement abstract method")
    
# Defines a subclass named `Cat` that inherits from `Animal`:  
class Cat(Animal):
    # Overrides the `speak` method to provide specific functionality:
    def speak(self):
        print(f"{self.name} the cat says meow!")

# Creates an instance of the `Cat` class with the name "Jasper":
cat = Cat("Jasper")
# Calls the `speak` method and prints the result:
cat.speak()
