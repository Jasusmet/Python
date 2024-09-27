### List Comprehension ###

"""
List comprehension in Python is a compact way of creating a list from a sequence.
It is a short way to create a new list.
List comprehension is considerably faster than processing a list using the for loop.
"""

my_original_list = [35, 24, 62, 52, 30, 30, 17]
print(my_original_list) # Output: [35, 24, 62, 52, 30, 30, 17]

my_list = [i for i in my_original_list] # We transform a list into another list
print(my_list) # Output: [35, 24, 62, 52, 30, 30, 17]

my_list = [i for i in range(7)] # We can iterate over a range of numbers
print(my_list) # Output: [0, 1, 2, 3, 4, 5, 6]

my_list = [i + 1 for i in range(8)] # We can do the same thing but adding 1 to the initial value
print(my_list) # Output: [1, 2, 3, 4, 5, 6, 7, 8]

my_list = [i * 2 for i in range(8)] # We can do it only with even numbers
print(my_list) # Output: [0, 2, 4, 6, 8, 10, 12, 14]

my_list = [i * i for i in range(8)] # Or even by multiplying its value by itself as it iterates
print(my_list) # Output:  [0, 1, 4, 9, 16, 25, 36, 49]

def sum_five(number): # We define a value using a function
    return number + 5

my_list = [sum_five(i) for i in range(8)] # We can make the index have a default value thanks to a function
print(my_list) # Output: [5, 6, 7, 8, 9, 10, 11, 12]

#* Exercises

#* Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

negative_and_zero_numbers = [i for i in numbers if i <= 0]
print(negative_and_zero_numbers) # Output: [-4, -3, -2, -1, 0]