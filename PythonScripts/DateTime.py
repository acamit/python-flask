import datetime as dt

now = dt.datetime.now()
year = now.year
weekday = now.weekday()
print(now)
print(year)
print(weekday)


dob = dt.datetime(year=1995, month=10, day =8, hour=10)
print(dob)
