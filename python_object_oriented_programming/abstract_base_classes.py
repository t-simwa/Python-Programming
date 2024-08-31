
# Abstract Base Classes (ABCs) are classes that cannot be instantiated and are meant to be subclassed.

# Imports the necessary components for creating abstract base classes.
from abc import ABC, abstractmethod

# Defines an abstract base class named `Animal`:
class Animal(ABC):
    # A decorator that defines an abstract method:
    @abstractmethod
    # Defines an abstract method named `speak`: 
    def speak(self):
        pass

# Defines a subclass named `Cat` that inherits from `Animal`:
class Cat(Animal): 
    # Provides a specific implementation for the `speak` method:
    def speak(self):
        return "Meow"

# Creates an instance of the `Cat` class: 
cat = Cat()

# Calls the `speak` method and prints the result:
print(cat.speak())   # Output: Meow