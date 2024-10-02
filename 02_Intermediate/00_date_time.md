# _Date Time_

The datetime module in Python provides classes for manipulating dates and times. It allows you to:

- Create objects representing specific dates and times
- Perform arithmetic operations on dates and times (e.g., add or subtract days, hours, minutes, etc.)
- Format dates and times in different formats
- Extract information from dates and times (e.g., day of the week, month, year, etc.)

## Index

* [_Date Time_](#Date-Time)
  - [Getting _datetime_ information](#getting-datetime-information)
  - [Formatting date output using _strftime_](#formatting-date-output-using-strftime)
  - [String to time using _strptime_](#string-to-time-using-strptime)
  - [Using _date_ from _datetime_](#using-date-from-datetime)
  - [Time objects to represent time](#time-objects-to-represent-time)
  - [Difference between two points in time using _date_](#difference-between-two-points-in-time-using-date)
  - [Difference between two points in Time using _timedelta_](#difference-between-two-points-in-time-using-timedelta)

### DateTime Classes

The datetime modulo provides several classes:

- date: Represents a date whithout time
- time: Represents a time without date
- datetime: Represents a date and time
- timedelta: Represents a time interval (e.g., a day, hour, minute, etc.)
- tzinfo: Represents time zone information

```py
import datetime
print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
```

With dir or help built-in commands it is possible to know the available functions in a certain module. As you can see, in the datetime module there are many functions, but we will focus on _date_, _datetime_, _time_ and _timedelta_. Let's see them one by one.

### Getting _datetime_ information

```py
from datetime import datetime
now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')
```

Timestamp or Unix timestamp is the number of seconds elapsed from 1st of January 1970 UTC.

### Formatting date output using _strftime_

```py
from datetime import datetime
new_year = datetime(2020, 1, 1)
print(new_year)      # 2020-01-01 00:00:00
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute) #1 1 2020 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 1/1/2020, 0:0
```

```py
from datetime import datetime
# Current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)
```

```sh
time: 15:05:01
time one: 10/01/2024, 15:05:01
time two: 01/10/2024, 15:05:01
```

Here are all the _strftime_ symbols we use to format time. An example of all the formats for this module.

![strftime](../00_Images/strftime.png)

### String to time using _strptime_

```py
from datetime import datetime
date_string = "1 October, 2024"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
```

```sh
date_string = 1 October, 2024
date_object = 2024-10-01 00:00:00
```

### Using _date_ from _datetime_

```py
from datetime import date
d = date(2024, 10, 1)
print(d)
print('Current date:', d.today())    # 2024-10-01
# Date object of today's date
today = date.today()
print("Current year:", today.year)   # 2024
print("Current month:", today.month) # 10
print("Current day:", today.day)     # 1
```

### Time objects to represent time

```py
from datetime import time
# Time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a) # 00:00:00
# Time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b) # 10:30:50
# Time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c) # 10:30:50
# Time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d) # 10:30:50.200555
```

### Difference between two points in time using _date_

```py
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00
```

### Difference between two points in time using _timedelta_

```py
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
```

```sh
    date_string = 5 December, 2019
    date_object = 2019-12-05 00:00:00
    t3 = 86 days, 22:56:50
```

## Exercises

1. Print the current date and time information

```py
# Get the current date and time
now = datetime.now()

# Get the current day, month, year, hour, minute and timestamp
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()

print(f"Day: {day}")
print(f"Month: {month}")
print(f"Year: {year}")
print(f"Hour: {hour}")
print(f"Minute: {minute}")
print(f"Timestamp: {timestamp}")
```

2. Format the current date using this format: '%m/%d/%Y/,%H:%M:%S'

```py
from datetime import datetime

# Get the current date and time
now = datetime.now()

# Using 'strftime' function to format the time and date into a string according to a specified format
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print("The current date and time is:", time_one)
```

3. Today is 5 December, 2019. Change this time string to time

```py
from datetime import datetime

# Using 'strptime' function to parse a string representing a time or date
date_string = "5 December, 2019"
print("date_string =", date_string) # date_string = 5 December, 2019
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object) # date_object = 2019-12-05 00:00:00
```

4. Calculate the time difference between now and new year

```py
from datetime import datetime

today = date(year=2024, month=9, day=27)
new_year = date(year=2025, month=1, day=1)
time_left_for_new_year = new_year - today
print("Time left for new year: ", time_left_for_new_year)
```

5. Calculate the time difference between 1 January 1970 and now

```py
from datetime import datetime

def calculate_time_diff(year1, month1, day1, year2, month2, day2):
    date1 = date(year1, month1, day1)
    date2 = date(year2, month2, day2)

    time_diff = date2 - date1

    days = time_diff.days
    years = days // 365
    remaining_days = days % 365
    months = remaining_days // 30
    remaining_days = remaining_days % 30

    return years, months, remaining_days

today = date(year=2024, month=9, day=27)
past_time = date(year=1970, month=1, day=1)

years, months, days = calculate_time_diff(1970, 1, 1, 2024, 9, 27)

print("The time difference is : {} years, {} months and {} days".format(years, months, days))
```
