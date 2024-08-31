# Define a function to check if a given number is prime or not. 

def is_prime(number): # Defines a function called 'is_prime' that takes one argument 'number'.
    if number <= 1: # Checks if input is less or equal to 1 as such numbers are not prime by definition.
        return False 
    for i in range(2, int(number**0.5) + 1): # Creates a loop that iterates from 2 to the square root of the input number plus 1. 
        if number % i == 0: # Checks if the input number is divisible evenly by i. If it is, the function returns False. 
            return False
    return True

num_to_check = int(input("Enter a number to check if it's prime:"))
if is_prime(num_to_check):
    print(num_to_check, "is a prime number.")
else:
    print(num_to_check, "is not a prime number.")