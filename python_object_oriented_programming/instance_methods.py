
# Instance methods operate on the instance attributed of the objects. 

class Dog:
    def __init__(self, name, age): 
        self.name = name
        self.age = age 
    
    # Defines an instance method named `bark`:
    def bark(self):
        # Prints a message that includes the dog's name and age:
        print(f"{self.name}, age {self.age}, is barking loudly!")

my_dog = Dog("Rex", 15)
# Calls the `bark` method on the `my_dog` object:
my_dog.bark()

