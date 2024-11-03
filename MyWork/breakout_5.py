## On July 16, 1969, the huge, 363-feet tall Saturn V rocket launches on the Apollo 11 mission from Pad A, Launch Complex 39, Kennedy Space Center, at 9:32 a.m. EDT. Write a Python program the computes (from now) the number of:

#Years
#Months
#Days
#Hours
#Minutes
#Seconds
#since the launch.

#https://stackoverflow.com/questions/1345827/how-do-i-find-the-time-difference-between-two-datetime-objects-in-python

import datetime

current_date = datetime.datetime.now()
launch_date = datetime.datetime(1969, 7, 16)

duration = current_date - launch_date
duration_in_s = duration.total_seconds()
years = divmod(duration_in_s, 31536000)[0]  # Seconds in a year=365*24*60*60 = 31536000
days  = divmod(duration_in_s, 86400)[0]     # Seconds in a day = 86400
hours = divmod(duration_in_s, 3600)[0]      # Seconds in an hour = 3600
minutes = divmod(duration_in_s, 60)[0]      # Seconds in a minute = 60

print(f"Number of Years:   {years}")
print(f"Number of Weeks:   {days/7}")
print(f"Number of Days:    {days}")
print(f"Number of Hours:   {hours}")
print(f"Number of Minutes: {minutes}")
print(f"Number of Seconds: {duration_in_s}")
