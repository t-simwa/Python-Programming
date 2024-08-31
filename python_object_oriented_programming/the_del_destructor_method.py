
# The `__del__` method is a special method that is called when an object is about to be destroyed. 
# It is useful for cleanup activities.

# Define a class named Person
class Person:
    # Defines the `__init__` constructor method:
    def __init__(self, name, age):
        # Assigns the `name` parameter to the instance attribute `name`:
        self.name = name
        # Assigns the `age` parameter to the instance attribute `age`.
        self.age = age

    # Method to display person's info:
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    # Defines the `__del__` constructor method:
    def __del__(self):
        print(f"Person object with the name {self.name} is about to be deleted.")

# Creates an instance of the `Person` class with the name "Ted" and age 26.
person1 = Person("Ted", 26)

# Calls the `display_info` method to print the person's information:
person1.display_info()   # Output: Name: Ted, Age: 26

# Deletes the `person1` object, triggering the `__del__` method.
del person1