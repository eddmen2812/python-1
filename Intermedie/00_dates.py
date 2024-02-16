#Dates
from datetime import datetime


now = datetime.now()


def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())
print_date(now)


year_2024 = datetime(2024,2,1)
print_date(year_2024)


from datetime import time
current_time = time(16,2,26)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date
current_date=date.today()
print(current_date.year)
print(current_date.month)
print(current_date.day)


current_date=date(2024,1,2)
print(current_date.year)
print(current_date.month)
print(current_date.day)
current_date=date(current_date.year,current_date.month + 1,current_date.day)
print(current_date.month)

diff = year_2024 -now
print(diff)
diff= year_2024.date() - current_date
print(diff)


from datetime import timedelta
start_timedelta = timedelta(200,100,156,weeks=10)
end_timedelta = timedelta(500,100,156,weeks=20)
print(end_timedelta-start_timedelta)
print(end_timedelta+start_timedelta)