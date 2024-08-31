
# Class attributes and methods are shared among all instances of a class.

class Dog: 

    # Defines a class attribute named `species`
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age 

    # A decorator that defines a class method.
    @classmethod
    # Defines a class method named `species_info`.
    def species_info(cls):
        # Returns a string that includes the class attribute `species`.
        return f"All dogs are of species: {cls.species}"

# Calls the class method `species_info` and prints the result.   
print(Dog.species_info())