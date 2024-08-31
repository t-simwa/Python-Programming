
# Given a year, determine whether it is a leap year. 
# If it is a leap year, return the Boolean True, otherwise return False.

def is_leap(year):
    if year % 4 == 0: # Checks if year is divisible by 4
        if year % 100 == 0: # Checks if year is divisible by 100
            if year % 400 == 0: # Checks if year is divisble by 400
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = int(input())
