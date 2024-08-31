
# Instance attributes are variables that are specific to each object created from a class.

class Dog:
    def __init__(self, name, age):
        # Assigns the `name` parameter to the instance attribute `name`:
        self.name = name      
        # Assigns the `age` parameter to the instance attribute `age`:
        self.age = age

# Creates an instance of the `Dog` class with the name `Rex` and age 15:
my_dog = Dog("Rex", 15)

# Prints the `name` attribute of the `my_dog` object.
print(my_dog.name)    # Output: Rex

# Prints the `age` attribute of the `my_dog` object.
print(my_dog.age)     # Output: 15

        