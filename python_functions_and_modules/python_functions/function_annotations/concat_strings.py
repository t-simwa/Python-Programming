
# Define a function `concat_strings` with type annotations for its parameters and return type. It should concatenate two strings.

def concat_strings(a: str, b: str) -> str:
    """
    Concatenate two strings
    """
    return a + b

print(concat_strings("Hello, ", "World!"))     # Output: Hello, World!
print(concat_strings.__annotations__)      # Output: {'a': <class: 'str'>, 'b': <class: 'str'>, 'return': <class: 'str'>}

