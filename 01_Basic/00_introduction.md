# *Introduction to Python*

Python is a high-level, interpreted, and object-oriented programming language. It was created in the 1990s by Guido van Rossum and has become one of the most popular and versatile languages in the world.

## Key features of Python:

* Easy to learn: Python has a simple and readable syntax, making it ideal for beginners and experts alike.
Object-oriented: Python supports object-oriented programming, allowing for the creation of modular and reusable programs.
* Interpreted: Python does not need to be compiled before execution, making it easier for rapid development and debugging.
* Extensive standard library: Python has a vast collection of libraries and modules that facilitate tasks such as file manipulation, networking, database management, and more.
* Active community: Python has a very active and growing community, which means there are many resources available to learn and troubleshoot.

## Common uses of Python:

* Web development: Python is used in frameworks like Django and Flask to create web applications.
* Data analysis: Python is very popular in data analysis and data science, thanks to libraries like NumPy, pandas, and scikit-learn.
Artificial intelligence and machine learning: Python is used in libraries like TensorFlow and Keras to create machine learning models.
* Automation: Python is used to automate tasks and processes in operating systems and applications.

### Python Syntax

A Python script can be written in Python interactive shell or in the code editor. A Python file has an extension .py.

### Comments

Comments are very important to make the code more readable and to leave remarks in our code. Python does not run comment parts of our code.
Any text starting with hash(#) in Python is a comment.

**Example: Single Line Comment**

```shell
# This is the first comment
# This is the second comment
# Python is eating the world
```

**Example: Multiline Comment**

Triple quote can be used for multiline comment if it is not assigned to a variable

```shell
"""This is multiline comment
multiline comment takes multiple lines.
python is eating the world
"""
```

### Data types

In Python there are several types of data types. Let us get started with the most common ones. Different data types will be covered in detail in other sections. For the time being, let us just go through the different data types and get familiar with them. You do not have to have a clear understanding now.

#### Number

- Integer: Integer(negative, zero and positive) numbers
    Example:
    ... -3, -2, -1, 0, 1, 2, 3 ...
- Float: Decimal number
    Example
    ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
- Complex
    Example
    1 + j, 2 + 4j

#### String

A collection of one or more characters under a single or double quote. If a string is more than one sentence then we use a triple quote.

**Example:**

```py
'Adam'
'Finland'
'Python'
'I love teaching'
'I hope you are enjoying the first day of 30DaysOfPython Challenge'
```

#### Booleans

A boolean data type is either a True or False value. T and F should be always uppercase.

**Example:**

```python
    True  #  Is the light on? If it is on, then the value is True
    False # Is the light on? If it is off, then the value is False
```

#### List

Python list is an ordered collection which allows to store different data type items. A list is similar to an array in JavaScript.

**Example:**

```py
[0, 1, 2, 3, 4, 5]  # All are the same data types - a list of numbers
['Banana', 'Orange', 'Mango', 'Avocado'] # All the same data types - a list of strings (fruits)
['Finland','Estonia', 'Sweden','Norway'] # All the same data types - a list of strings (countries)
['Banana', 10, False, 9.81] # Different data types in the list - string, integer, boolean and float
```

#### Dictionary

A Python dictionary object is an unordered collection of data in a key value pair format.

**Example:**

```py
{
'first_name':'Adam',
'last_name':'Yetayeh',
'country':'Finland', 
'age':250, 
'is_married':True,
'skills':['JS', 'React', 'Node', 'Python']
}
```

#### Tuple

A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created. They are immutable.

**Example:**

```py
('Adam', 'Pawel', 'Brook', 'Abraham', 'Lidiya') # Names
```

```py
('Earth', 'Jupiter', 'Neptune', 'Mars', 'Venus', 'Saturn', 'Uranus', 'Mercury') # Planets
```

#### Set

A set is a collection of data types similar to list and tuple. Unlike list and tuple, set is not an ordered collection of items. Like in Mathematics, set in Python stores only unique items.

In later sections, we will go in detail about each and every Python data type.

**Example:**

```py
{2, 4, 3, 5}
{3.14, 9.81, 2.7} # Order is not important in set
```