
# Import the Car class from the defining_a_class file:
from defining_a_class import Car

# Create an instance of the `Car` class with the brand "Mercedes" and model "Benz":
my_car = Car("Mercedes", "Benz")

# Prints the `brand` attribute of the `my_car` object:

print(my_car.brand) # Output: Mercedes

# Prints the `model` attribute of the `my_car` object:

print(my_car.model) # Output: Benz

# Calls the `display_info` method to print the car's information:
my_car.display_info()