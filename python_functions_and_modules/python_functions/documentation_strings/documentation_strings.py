
# Documentation strings, or docstrings, provide a convenient way to associate documentation with functions, classes, and modules. 
# They are defined using triple quotes and can be accessed using the `.__doc__` attribute.

def greet(name):
    """
    Greet the person with the provided name.
    """
    return f"Hello, {name}"

print(greet.__doc__) # Output: Greet the person with the provided name. 

