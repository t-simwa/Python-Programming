
# Magic methods allow you to define how objects of your class behave with built-in Python operations:

# Define a class named Vector: 
class Vector: 
    def __init__(self, x, y):
        self.x = x 
        self.y = y 

# Defines the behavior of the `+` operator for `Vector` objects:
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

# Defines the string representation of `Vector` objects:
    def __str__(self): 
        return f"Vector({self.x}, {self.y})"
    
# Creates an instance of the `Vector` class with coordinates (5, 10):
v1 = Vector(5, 10)
# Creates an instance of the `Vector` class with coordinates (4, 8):
v2 = Vector(4, 8)

# Adds the two vectors using the overloaded `+` operator:
v3 = v1 + v2 

# Prints the result using the overloaded `__str__` method:
print(v3)  # Output: Vector(9, 18)