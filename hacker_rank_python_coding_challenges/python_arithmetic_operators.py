
# The provided code stub reads two integers from STDIN, a and b. 
# Add code to print three lines where:
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
def add(a, b): 
    return a + b # Returns the sum of a and b

def subtract(a, b):
    return a - b # Returns the difference between a and b

def multiply(a, b):
    return a * b # Returns the product of a and b
    
    
print(add(a, b))
print(subtract(a, b))
print(multiply(a, b))

