# Create a dictionary representing a person with keys for name, age and city. 
# Print each key-value pair. 

person = {"Name": "Ted Simwa", "Age": 26, "City": "Nairobi"} # Creates a dictionary called 'person' with three key-value pairs.
for key, value in person.items(): # Creates a loop that iterates through each key-value pair in the dictionary. The item() method returns a view object that displays a list of the dictionary's key-value tuple pairs. 
    print(key + ":", value)