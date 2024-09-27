### Dates ###

"""
The datetime module in Python provides classes for manipulating dates and times. It allows you to:

-   Create objects representing specific dates and times
-   Perform arithmetic operations on dates and times (e.g., add or subtract days, hours, minutes, etc.)
-   Format dates and times in different formats
-   Extract information from dates and times (e.g., day of the week, month, year, etc.)

DateTime Classes

The datetime module provides several classes:

-  date: represents a date without time
-  time: represents a time without date
-  datetime: represents a date and time
-  timedelta: represents a time interval (e.g., a day, hour, minute, etc.)
-  tzinfo: represents time zone information
"""

from datetime import datetime

now = datetime.now()

timestamp = now.timestamp()

print(timestamp)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

year_2025 = datetime(2025, 1, 1)

print(year_2025)

from datetime import time

current_time = time(21, 6, 0) # In this way we establish a fixed time

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date(2024, 6, 22) # In this way we establish a fixed date

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date.today() # In this way we define the current date

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day) # This is a simple way to modify an already established date

print(current_date.month)

diff = year_2025 - now # So we can see the time difference between two dates, the two parameters must be of the same type
print(diff)
diff = year_2025.date() - current_date
print(diff)

from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks = 10) # With 'timedelta' we work with date ranges and allow us to define absolute values
end_timedelta = timedelta(300, 100, 100, weeks = 13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)

print("\n EXERCISES \n")

print("1. Print the current date and time information\n")

from datetime import datetime

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
print(f"Timestamp: {timestamp}\n")

print("2. Format the current date using this format: '%m/%d/%Y/,%H:%M:%S'\n")

from datetime import datetime

# Get the current date and time
now = datetime.now()

# Using 'strftime' function to format the time and date into a string according to a specified format
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print("The current date and time is:", time_one)

print("3. Today is 5 December, 2019. Change this time string to time\n")

from datetime import datetime

# Using 'strptime' function to parse a string representing a time or date
date_string = "5 December, 2019"
print("date_string = ")