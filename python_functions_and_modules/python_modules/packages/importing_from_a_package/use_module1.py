
#  Packages are a way to structure Python modules into a hierarchy of directories. 
#  A package is a directory that contains a special `__init__.py` file and other module files


#  Create a package `my_package` with a module `module1.py` that contains a function `say_hello`. 
#  Import and use this function in a script.

from my_package.module1 import say_hello
print(say_hello()) # Output: Hello from module!


