
# Within the package `my_package`, use relative imports to call `say_hello` from `module1.py` in `module2.py` and create a script to test it.

from .module1 import say_hello

def greet(): 
    return say_hello() + "Greetings from module2!"