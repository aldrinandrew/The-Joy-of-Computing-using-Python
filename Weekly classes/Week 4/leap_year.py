"""
Leap year or not_ program

My method

import random
year = random.randint(1993,2021)
print(year)
if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a leap year")

"""

# Easy solution


import random

year = random.randint(1990, 2021)
print(year)
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("The given year is a leap year")
else:
    print("The given year is not a leap year")
