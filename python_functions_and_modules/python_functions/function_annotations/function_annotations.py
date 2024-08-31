
# Function annotations provide a way to attach metadata to function arguments and return values.
# Annotations are optional and do not affect the function's behavior.

def add(x: int, y: int) -> int:
    return x + y

print(add(5, 3))       # Output: 8 
print(add.__annotations__)   # Output: {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}