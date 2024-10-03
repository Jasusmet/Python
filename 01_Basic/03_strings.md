# _Strings_

A string is a fundamental data type in computer science that represents a sequence of characters, such as letters, words, or sentences. It's a way to store and manipulate human-readable data in a program. Strings can be thought of as a collection of characters that are stored in contiguous memory locations, terminated by a special character called the null character.

## Index

- [Creating a string](#creating-a-string)
- [String concatenation](#string-concatenation)
- [Escape sequences in strings](#escape-sequences-in-strings)
- [String formatting](#string-formatting)
  - [Old style string formatting (% Operator)](#old-style-string-formatting--operator)
  - [New style string formatting (str.format)](#new-style-string-formatting-strformat)
  - [String interpolation (f-Strings)](#string-interpolation-f-strings)
- [Strings as sequences of characters](#strings-as-sequences-of-characters)
  - [Unpacking characters](#unpacking-characters)
  - [Accessing characters in strings by index](#accessing-characters-in-strings-by-index)
  - [Slicing strings](#slicing-strings)
  - [Reversing a string](#reversing-a-string)
  - [Skipping characters while slicing](#skipping-characters-while-slicing)
- [String methods](#string-methods)

### Creating a string

```py
letter = 'P' # A string could be a single character or a bunch of texts
print(letter) # P
print(len(letter)) # 1
greeting = 'Hello, World!' # String could be made using a single or double quote,"Hello, World!"
print(greeting) # Hello, World!
print(len(greeting)) # 13
sentence = "I hope you are enjoying the course"
print(sentence)
```

Multiline string is created by using triple single (''') or triple double quotes ("""). See the example below.

```py
multiline_string = '''I'm a developer and enjoy programming.
That's why I'm doing this.'''
print(multiline_string)

# Another way of doing the same thing
multiline_string = """I'm a developer and enjoy programming.
That's why I'm doing this."""
print(multiline_string)
```

### String concatenation

We can connect strings together, merging or connecting strings is called concatenation. See the example below:

```py
first_name = 'Jesús'
last_name = 'Clemente'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Jesús Clemente
# Checking the length of a string using len() built-in function
print(len(first_name)) # 5
print(len(last_name)) # 8
print(len(first_name) > len(last_name)) # False
print(len(full_name)) # 14
```

### Escape sequences in strings

In Python and other programming languages \ followed by a character is an escape sequence. Let us see the most common escape characters:

- \n: new line
- \t: Tab means(8 spaces)
- \\\\: Back slash
- \\': Single quote (')
- \\": Double quote (")

Now, let's see the use of the above escape sequences with examples.

```py
print('I hope everyone is enjoying the course.\nAre you ?') # Line break
print('Days\tTopics\tExercises') # Adding tab space or 4 spaces
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # To write a double quote inside a single quote

# Output
I hope every one is enjoying the course.
Are you ?
Days	Topics	Exercises
Day 1	5	    5
Day 2	6	    20
Day 3	5	    23
Day 4	1	    35
This is a backslash  symbol (\)
In every programming language it starts with "Hello, World!"
```

### String formatting

String formatting is a powerful feature in programming that allows you to create formatted strings by inserting variables, expressions, or values into a string template. This technique is essential in various programming languages, including Python, Java, C++, and many others.

#### Old style string formatting (% Operator)

The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s", "%d", "%f", "%.<small>number of digits</small>f".

- %s - String (or any object with a string representation, like numbers)
- %d - Integers
- %f - Floating point numbers
- "%.<small>number of digits</small>f" - Floating point numbers with fixed precision

```py
# Strings only
first_name = 'Jesús'
last_name = 'Clemente'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string) # I am Jesús Clemente. I teach Python

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"
```

#### New style string formatting (str.format)

This formatting is introduced in Python version 3

```py
first_name = 'Jesús'
last_name = 'Clemente'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # Limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# Output
4 + 3 = 7
4 - 3 = 1
4 * 3 = 12
4 / 3 = 1.33
4 % 3 = 1
4 // 3 = 1
4 ** 3 = 64

# Strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)
```

#### String interpolation (f-Strings)

This formatting is introduced in Python version 3.6+

Another new string formatting is string interpolation, f-strings. Strings start with f and we can inject the data in their corresponding positions.

```py
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
```

### Strings as sequences of characters

Python strings are sequences of characters, and share their basic methods of access with other Python ordered sequences of objects – lists and tuples. The simplest way of extracting single characters from strings (and individual members from any sequence) is to unpack them into corresponding variables.

#### Unpacking characters

```py
language = 'Python'
a,b,c,d,e,f = language # Unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n
```

#### Accessing characters in strings by index

In programming counting starts from zero. Therefore the first letter of a string is at zero index and the last letter of a string is the length of a string minus one.

```py
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n
```

If we want to start from right end we can use negative indexing, -1 is the last index.

```py
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o
```

#### Slicing strings

We can slice strings into substrings.

```py
language = 'Python'
first_three = language[0:3] # Starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon
```

#### Reversing a string

We can easily reverse strings.

```py
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH
```

#### Skipping characters while slicing

It is possible to skip characters while slicing bty passing step argument to slice method.

```py
language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto
```

### String methods

There are many string methods which allow us to format strings. See some of the string methods in the following example:

- capitalize(): Converts the first character of the string to capital letter

```py
var = 'python course'
print(var.capitalize()) # 'Python course'
```

- count(): Returns occurrences of substring in string, count(substring, start=.., end=..). The start is a starting indexing for counting and end is the last index to count.

```py
var = 'python course'
print(var.count('y')) # 1
print(var.count('y', 3, 10)) # 0 
print(var.count('th')) # 1
```

- endswith(): Checks if a string ends with a specified ending

```py
var = 'python course'
print(var.endswith('se')) # True
print(var.endswith('thon')) # False
```

- expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument

```py
var = 'python\tcourse'
print(var.expandtabs()) # python  course
print(var.expandtabs(10)) # python    course
```

- find(): Returns the index of the first occurrence of a substring, if not found returns -1

```py
var = 'python course'
print(var.find('y')) # 1
print(var.find('th')) # 2
```

- rfind(): Returns the index of the last occurrence of a substring, if not found returns -1

```py
var = 'python course'
print(var.rfind('y')) # 1
print(var.rfind('th')) # 2
```

- format(): Formats string into a nicer output

```py
first_name = 'Jesús'
last_name = 'Clemente'
job = 'developer'
age = 25
country = 'Spain'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, job, age, country)
print(sentence) # I am Jesús Clemente. I am a developer. I am 25 years old. I live in Spain.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314
```

- index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError. 

```py
var = 'python course'
sub_string = 'co'
print(var.index(sub_string)) # 7
print(var.index(sub_string, 9)) # Error
```

- rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)

```py
var = 'python course'
sub_string = 'co'
print(var.rindex(sub_string))  # 7
print(var.rindex(sub_string, 9)) # Error
```

- isalnum(): Checks alphanumeric character

```py
var = '25'
print(var.isalnum()) # True

var = 'Monday'
print(var.isalnum()) # True

var = 'python course'
print(var.isalnum()) # False, space is not an alphanumeric character

var = 'python course 2024'
print(var.isalnum()) # False
```

- isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)

```py
var = 'python course'
print(var.isalpha()) # False, space is once again excluded
var = 'Monday'
print(var.isalpha()) # True
num = '123'
print(num.isalpha()) # False
```

- isdecimal(): Checks if all characters in a string are decimal (0-9)

```py
var = 'python course'
print(var.isdecimal()) # False
var = '123'
print(var.isdecimal()) # True
var = '\u00B2'
print(var.isdigit()) # True
var = '12 3'
print(var.isdecimal()) # False, space not allowed
```

- isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)

```py
var = 'Thirty'
print(var.isdigit()) # False
var = '30'
print(var.isdigit()) # True
var = '\u00B2'
print(var.isdigit()) # True
```

- isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)

```py
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False
```

- isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name

```py
var = '25years'
print(var.isidentifier()) # False, because it starts with a number
var = 'python_course'
print(var.isidentifier()) # True
```

- islower(): Checks if all alphabet characters in the string are lowercase

```py
var = 'python course'
print(var.islower()) # True
var = 'Python course'
print(var.islower()) # False
```

- isupper(): Checks if all alphabet characters in the string are uppercase

```py
var = 'python course'
print(var.isupper()) #  False
var = 'PYTHON COURSE'
print(var.isupper()) # True
```

- join(): Returns a concatenated string

```py
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'
```

```py
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'
```

- strip(): Removes all given characters starting from the beginning and end of the string

```py
var = 'I love Python'
print(var.strip('noth')) # 'I love Py
```

- replace(): Replaces substring with a given string

```py
var = 'python course'
print(var.replace('python', 'coding')) # 'coding course'
```

- split(): Splits the string, using given string or space as a separator

```py
var = 'python course'
print(var.split()) # ['python', 'course']
var = 'I, love, python'
print(var.split(', ')) # ['I', 'love', 'python']
```

- title(): Returns a title cased string

```py
var = 'python course'
print(var.title()) # Python Course
```

- swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters

```py
var = 'python course'
print(var.swapcase()) # PYTHON COURSE
var = 'PYTHON COURSE'
print(var.swapcase()) # python course
```

- startswith(): Checks if string starts with the specified string

```py
var = 'python course'
print(var.startswith('py')) # True

var = 'Monday'
print(var.startswith('py')) # False
```