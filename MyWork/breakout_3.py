## Create an artbitrary date object and add five weeks, Print the new dates. 

import datetime

initial_date = datetime.date(2024, 11, 3)
new_date = initial_date + datetime.timedelta(weeks=5)

print('Arbitrary date: ', initial_date)
print('New date (+ 5 weeks): ', new_date)

