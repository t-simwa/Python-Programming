
# A function combining positional-or-keyword, positional-only, and keyword-only parameters.

def mixed_function(a, b, /, c, d, *, e, f):
    return a + b + c + d + e + f 

print(mixed_function(1, 2, 3, 4, e=5, f=6)) # Output: 21

