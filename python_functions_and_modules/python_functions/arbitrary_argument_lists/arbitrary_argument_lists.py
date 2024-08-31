
# Use `* args` to pass a variable number of positional arguments. 

def print_number(*args): # The `*` symbol enable the function to accept any mumber of arguments for its parameters.
    for number in args: 
        print(number)

print_number(1, 2, 3, 4)  # Output: 1 2 3 4
