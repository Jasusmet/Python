### Higher Order Functions ###

"""
In Python functions are treated as first class citizens, allowing you to perform the following operations on functions:

-   A function can take one or more functions as parameters
-   A function can be returned as a result of another function
-   A function can be modified
-   A function can be assigned to a variable
"""

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_value(5, 2, sum_one)) # Output: 8
print(sum_two_values_and_add_value(5, 2, sum_five)) # Output: 12

### Closures ###

"""
Python allows a nested function to access the outer scope of the enclosing function.
This is is known as a Closure. Let us have a look at how closures work in Python.
In Python, closure is created by nesting a function inside another encapsulating function and then returning the inner function.
"""

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add


add_closure = sum_ten(1)
print(add_closure(5)) # Output: 16
print((sum_ten(5))(1)) # Output: 16

### Built-in Higher Order Functions ###

"""
Some of the built-in higher order functions that we cover in this part are map(), filter, and reduce.
Lambda function can be passed as a parameter and the best use case of lambda functions is in functions like map, filter and reduce.
"""

numbers = [2, 5, 10, 21, 3, 30]

# Map (The map() function is a built-in function that takes a function and iterable as parameters)

def multiply_two(number):
    return number * 2 

print(list(map(multiply_two, numbers))) # Output: [4, 10, 20, 42, 6, 60]
print(list(map(lambda number: number * 2, numbers))) # Output: [4, 10, 20, 42, 60]

# Filter (The filter() function calls the specified function which returns boolean for each item of the specified iterable (list). It filters the items that satisfy the filtering criteria)

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers))) # Output: [21, 30]
print(list(filter(lambda number: number > 10, numbers))) # Output: [21, 30]

# Reduce (The reduce() function is defined in the functools module and we should import it from this module. Like map and filter it takes two parameters, a function and an iterable. However, it does not return another iterable, instead it returns a single value)

from functools import reduce

def sum_two_values(first_value, second_value):
    return first_value + second_value 

print(reduce(sum_two_values, numbers)) # Output: 71