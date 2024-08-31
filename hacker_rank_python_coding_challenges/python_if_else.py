
# Given an integer, perform the following conditional actions: 
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# Ifn is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 != 0:  # Odd number logic
        print('Weird')
    elif n % 2 == 0:   # Even number logic
        if 2 <= n <= 5:  # Set range between 2 to 5
            print("Not Weird")
        elif 6 <= n <= 20:  # set range between 6 to 20
            print("Weird")
        elif n > 20:  # n is greater than 20
            print("Not Weird")