
# Positional-only parameters are parameters that must be specified positionally

def subtract(x, y, /): # The `/` operator ensures all parameters before it are specified positionally.
    return x - y 

print(subtract(10, 5)) # Output 5 (Positional parameters)