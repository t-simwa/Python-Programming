
# Defining a class named `car`.
class Car: 
    # A class attribute that is shared by all instances of a class.
    wheels = 4

    # The constructor method initializes the instance attribute.
    def __init__(self, brand, model):
        self.brand = brand  # Assigns the `brand` parameter to the instance attribute `brand`.
        self.model = model  # Assigns the `model` parameter to the instance attribute `model`.
    
    # Defines an instance method that prints the car's brand and model.
    def display_info(self, cls):
        print(f"Car brand: {self.brand}, Model: {self.model}")

    