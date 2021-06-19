"""
datetime library

"""

import datetime

print(datetime.date.today())

print(datetime.date.today().strftime("%Y"))

print(datetime.date.today().strftime("%B"))

print(datetime.date.today().strftime("%d"))

print("Week number of the month", datetime.date.today().strftime("%W"))

print("Week day of the week", datetime.date.today().strftime("%w"))

print("Day of year", datetime.date.today().strftime("%j"))

print("Day of Week", datetime.date.today().strftime("%A"))

print(datetime.datetime.now())