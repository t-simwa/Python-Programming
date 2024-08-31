
# Use `*` to unpack arguments from a list or tuple into function arguments.

def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

info = ("Ted, 26")
display_info(*info) # Output: Name: Ted, Age: 26
