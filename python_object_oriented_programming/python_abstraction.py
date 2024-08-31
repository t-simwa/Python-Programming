
# Abstraction means exposing only the relevant parts of an object while hiding the unnecessary details.

# Defines a class called Computer:
class Computer: 
    def __init__(self, cpu, ram):
        # Defines a private instance attribute named `__cpu`.
        self.__cpu = cpu
        # Defines a private instance attribute named `__ram`.
        self.__ram = ram  
    
    # Defines a method named `perform_calculation`.
    def perform_calculation(self):
        # Returns a string indicating that a calculation is being performed.
        return "Calculating..."
    
# Creates an instance of the `Computer` class with specific CPU and RAM.   
my_computer = Computer("Intel", "16GB")

# Calls the `perform_calculation` method and prints the result.
print(my_computer.perform_calculation())
