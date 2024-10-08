### Error Types ###

"""
When we write code it is common that we make a typo or some other common error.
If our code fails to run, the Python interpreter will display a message,
containing feedback with information on where the problem occurs and the type of an error.
It will also sometimes gives us suggestions on a possible fix.
Understanding different types of errors in programming languages will help us to debug our code quickly and also it makes us better at what we do.
"""

# SyntaxError
#print "Hi!" # Error
print ("Hi!")

# NameError
language = "English" # Comment for Error
print(language)

# IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
#print(my_list[5]) # Uncomment for Error

# ModuleNotFoundError
# import maths # Uncomment for Error
import math

# AttributeError
#print(math.PI) # Uncomment for Error
print(math.pi)

# KeyError
my_dict = {"Name":"Jesús", "Surname":"Clemente", "Age":"25", 1:"Python"}
print(my_dict["Age"])
#print(my_dict["Afe"]) # Uncomment for Error

# TypeError
#print(my_list["Name"]) # Uncomment for Error
print(my_list[0])

# ImportError
#from math import PI # Uncomment for Error
from math import pi
print(pi)

# ValueError
#my_int = int("10 Years") # Uncomment for Error
#print(type(my_int)) # Uncomment for Error

# ZeroDivisionError
#print(4/0) # Uncomment for Error