
# Print the list of integers from through as a string, without spaces.

if __name__ == '__main__':
    n = int(input()) # Reads the input from STDIN, strips any extra whitespace, and converts it to an integer n.
    
for number in range(1, n + 1): # This loop iterates through numbers from 1 to n (inclusive).
    print(number, end='') # Prints each number i without adding a newline, achieved using end=''. 
    
    