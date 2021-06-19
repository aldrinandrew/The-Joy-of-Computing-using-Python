"""

If month is February and year is leap year then
Generate day randomly from to 1 to 29
If month is February and year is not a leap year then
Generate day randomly from 1 to 28
If month%2 == 0 and month<7 then //April and June
Generate day randomly from 1 to 30
If month%2 == 0 and month>7 then // August, October and December
Generate day randomly form 1 to 31
If month%2 != 0 and month<=7 then // January, March, May, July
Generate day randomly from 1 to 31
If month%2 != 0 and month>7 then // September and November
Generate day randomly from 1 to 30

"""

import random
import datetime

birthday = []
i = 0
while i < 50:
    year = random.randint(1895, 2020)
    # The oldest person ever lived was 122 years old
    if year % 4 == 0 and year % 100 == 0 or year % 400 == 0:
        leap = 1
    else:
        leap = 0
    month = random.randint(1, 12)
    if month == 2 and leap == 1:
        day = random.randint(1, 29)
    elif month == 0 and leap == 0:
        day = random.randint(1, 28)
    elif month == 7 or month == 8:
        day = random.randint(1, 31)
    elif month % 2 != 0 and month < 7:
        day = random.randint(1, 31)
    elif month % 2 == 0 and 7 < month < 12:
        day = random.randint(1, 31)
    else:
        day = random.randint(1, 30)
    dd = datetime.date(year, month, day)
    day_of_year = dd.timetuple().tm_yday  # Function that give day of year
    i = i + 1
    birthday.append(day_of_year)

birthday.sort()
i = 0
while i < 50:
    print(birthday[i])
    i = i + 1
