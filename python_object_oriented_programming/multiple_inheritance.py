
# Multiple inheritance allows a class to inherit attributes and methods from more than one parent class.

# Define a parent class named Animal:
class Animal: 
    def __init__(self, name):
        self.name = name 

# Define a parent class named Owner:
class Owner: 
    def __init__(self, owner):
        self.owner = owner

# Define a subclass named Cat that inherits from both Animal and Owner:
class Cat(Animal, Owner):
    def __init__(self, name, owner):
        # Initializes the `Animal` part of the `Cat` class:
        Animal.__init__(self, name)
        # Initializes the `Owner` part of the `Cat` class.
        Owner.__init__(self, owner)

    # Instance method to make the cat speak:
    def speak(self):
        return f"{self.name} the cat who is owned by {self.owner} says meow!"
    
# Creates an instance of the `Cat` class with the name "Jasper" and the owner "Ted":
cat = Cat("Jasper", "Ted")

# Prints the cat's name and owner:
print(f"Cat's name:{cat.name}, Cat's owner:{cat.owner}")
# Calls the 'speak' method and prints the results. 
print(cat.speak())