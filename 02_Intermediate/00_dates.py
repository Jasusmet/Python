### Dates ###

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

current_time = time(21, 6, 0) # De esta manera establecemos una hora fija

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date(2024, 6, 22) # De esta manera establecemos una fecha fija

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date.today() # De esta manera definimos la fecha actual

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day) # Esta es una forma sencilla de modificar una fecha ya establecida

print(current_date.month)

diff = year_2025 - now # Así podemos ver la diferencia temporal entre dos fechas, los dos parámetros deben de ser del mismo tipo
print(diff)
diff = year_2025.date() - current_date
print(diff)

from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks = 10) # Con "timedelta" trabajamos con franjas de fechas y nos permite definir valores absolutos
end_timedelta = timedelta(300, 100, 100, weeks = 13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)