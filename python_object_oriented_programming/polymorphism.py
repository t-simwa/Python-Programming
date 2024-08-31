
# Polymorphism allows methods to do different things based on the object it is acting upon.

# Define a parent class named `Animal`:
class Animal: 
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method.")
    
# Defines a subclass named `Dog` that inherits from `Animal`:    
class Dog: 
    # Overrides the `speak` method to provide specific functionality for dogs:
    def speak(self):
        return "Dog says Woof."
    
# Defines a subclass named `Cat` that inherits from `Animal`:
class Cat: 
    # Overrides the `speak` method to provide specific functionality for cats:
    def speak(self):
        return "Cat says Meow."

#  Defines a function that takes an `Animal` object and calls the `speak` method.`    
def animal_sound(animal):
    print(animal.speak())

# Create objects of Dog, Cat and Animal classes:
dog = Dog()
cat = Cat()
animal = Animal()

# Calls the `animal_sound` function with a `Dog` object and prints the result:
animal_sound(dog)     # Output: Dog says Woof.
# Calls the `animal_sound` function with a `Cat` object and prints the result:
animal_sound(cat)     # Output: Cat says Meow.
