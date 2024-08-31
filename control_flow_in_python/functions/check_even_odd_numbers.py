
# Write a function to check if a number is even or odd. 

def is_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even(4))  # Output: Even
print(is_even(7))  # Output: Odd
