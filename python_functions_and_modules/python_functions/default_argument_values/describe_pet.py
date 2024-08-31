
# Create a function `describe_pet` that takes two arguments: `pet_name` and `animal_type`. 
# Provide a default value of "dog" for `animal_type`

def describe_pet(pet_name, animal_type="dog"):
    return(f"I have a {animal_type} named {pet_name}.")

print(describe_pet("Rex"))               # Output: I have a dog named Rex. (uses the default animal_type value of "dog")
print(describe_pet("Whiskers, cat"))     # Output: I have a cat named Whiskers. (uses the animal_type value of "cat")


