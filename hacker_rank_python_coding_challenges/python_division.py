
# The provided code stub reads two integers, a and b ,from STDIN.
# Add logic to print two lines. 
# The first line should contain the result of integer division, a // b. 
# The second line should contain the result of float division, a / b. 


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
def integer_division(a, b): 
    return a // b  # Returns the result of integer division.

def float_division(a, b):
    return a / b   # Returns the results of float division.

print(integer_division(a, b))
print(float_division(a, b))

