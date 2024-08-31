
# The `super()` function is used to call a method from the parent class:

# # Define a base class named Animal:
class Animal: 
    def __init__(self, name):
        self.name = name

    def speak(self): 
        return f"{self.name} makes a sound."
    
# Define a subclass named Dog that uses super():
class Dog(Animal): 
    def __init__(self, name, breed):
        # Calls the constructor of the parent class `Animal`:
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name}, the {self.breed}, says woof!"
    
# Creates an instance of the `Dog` class with the name "Rex" and breed "German Shepherd":
dog = Dog("Rex", "German Shepherd")
animal = Animal("Every animal")

# Calls the `speak` methods and prints the results:
print(dog.speak())     # Output: Rex, the German Shepherd, says woof!
print(animal.speak())  # Output: Every animal makes a sound. 
