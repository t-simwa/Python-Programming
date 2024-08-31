
# Create a multi-directory package with `module1.py` in `package1` and `module2.py` in `package2`. 
# Demonstrate importing across these packages.

from package1.module1 import greeting_from_package1

def greeting_from_package2():
    return greeting_from_package1() + "Hello from package2!"