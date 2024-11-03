## Create a date object where year is 2023 and the day is 5.

import datetime
import random 

## datetime.time(day=5, year=2023) does not work, as datetime.time is only used to create time objects and does not recognize day and month

## Since month was not specified I imported random so I can add a random month
# Genrate a casual month from 1 to 12
random_month = random.randint(1, 12)

## I create the date object 
date = datetime.datetime(day=5, month=random_month, year=2023)
print(date)
