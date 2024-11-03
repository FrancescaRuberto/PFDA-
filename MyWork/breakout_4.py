## Write a function (named number_days_between) that:
## Takes two arguments that are 8-digit integers of the form YYYYMMDD (actually a date), and
## Returns the number of days between the two dates.

import datetime

d1 = datetime.datetime(1996, 9, 1)
d2 = datetime.datetime(1992, 3, 5)

date_format = "%Y%m%d"

difference = d1 - d2

number_of_days = difference.days 

print(f"The number of days between {d1.date()} and {d2.date()} is {number_of_days} days.") 