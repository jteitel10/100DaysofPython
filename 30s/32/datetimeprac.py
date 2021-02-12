import datetime as dt

# date time object for right now 
now = dt.datetime.now()
year = now.year

if year == 2020:
    print("Wear a face mask")
else:
    print("Be careful")

# set date time object to specific date
date_of_birth = dt.datetime(year=1993, month=2, day=1)
