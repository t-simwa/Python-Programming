
# Create a multi-directory package with `module1.py` in `package1` and `module2.py` in `package2`. 
# Demonstrate importing across these packages.

from package2.module2 import greeting_from_package2 

print(greeting_from_package2())

