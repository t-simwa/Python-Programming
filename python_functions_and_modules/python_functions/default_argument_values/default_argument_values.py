
# Default argument values allow you to define default values for function parameters.
# If the caller doesn't provide a value for a parameter, the default value is used. 

def power(base, exponent=2):
    return base ** exponent

print(power(5))      # Output: 25 (uses the default exponent of 2)
print(power(5, 3))   # Output: 125 (uses exponent of 3)