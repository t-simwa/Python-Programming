
# Positional paraemeters are parameters that are passed in the order they are defined.
# Keyword parameters are parameters that are specified by name in any order. 

def calculate_area(length, width):
    return length * width

print(calculate_area(10, 5))                # Output: 50 (Positional Arguments)
print(calculate_area(length=10, width=5))   # Output: 50 (Keyword Arguments)



