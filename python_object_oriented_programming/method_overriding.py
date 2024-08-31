
# Method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass.

# Define a parent class named `Animal`:
class Animal: 
    def __init__(self, name):
        self.name = name

    # Method to make the animal speak:
    def speak(self):
        return f"{self.name} makes a sound."
    
# Define a subclass named Dog that overrides the speak method  
class Cat(Animal):
    def speak(self): 
        return f"{self.name} says meow!"

# Creates an instance of the `Animal` class with the name "Every Animal":  
animal = Animal("Every animal")
# Creates an instance of the `Cat` class with the name "Jasper":
cat = Cat("Jasper")

# Calls the `speak` method on the `animal` object and prints the result:
print(animal.speak())  # Output: Every animal makes a sound.
# Calls the `speak` method on the `cat` object and prints the result.
print(cat.speak())     # Output: Jasper says meow!