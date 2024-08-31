
# Within the package `my_package`, use relative imports to call `say_hello` from `module1.py` in `module2.py` and create a script to test it.

from my_package.module2 import greet
print(greet())