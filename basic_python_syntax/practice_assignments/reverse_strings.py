# Write a Python program to reverse a given string. 

def reverse_string(input_string): 
    return input_string[::-1] # Uses Python's slicing notation to reverse the string. 

input_string = input("Enter a string to reverse:") 
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)