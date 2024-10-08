# _Variables_

Variables store data in a computer memory. Mnemonic variables are recommended to use in many programming languages. A mnemonic variable is a variable name that can be easily remembered and associated. A variable refers to a memory address in which data is stored. Number at the beginning, special character, hyphen are not allowed when naming a variable. A variable can have a short name (like x, y, z), but a more descriptive name (firstname, lastname, age, country) is highly recommended.

## Index

  - [Declaring multiple variables in a line](#declaring-multiple-variables-in-a-line)
  - [Data types](#data-types)
  - [Checking data types and casting](#checking-data-types-and-casting)
  - [Numbers](#numbers)

Python variable name rules

- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (a-z, 0-9, and \_ )
- Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME)

Here are some example of valid variable names:

```shell
firstname
lastname
age
country
city
first_name
last_name
capital_city
_if # If we want to use reserved word as a variable
year_2021
year2021
current_year_2021
birth_year
num1
num2
```

Invalid variables names:

```shell
first-name
first@name
first$name
num-1
1num
```

We will use standard Python variable naming style which has been adopted by many Python developers. Python developers use snake case(snake_case) variable naming convention. We use underscore character after each word for a variable containing more than one word(eg. first_name, last_name, engine_rotation_speed). The example below is an example of standard naming of variables, underscore is required when the variable name is more than one word.

When we assign a certain data type to a variable, it is called variable declaration. For instance in the example below my first name is assigned to a variable first_name. The equal sign is an assignment operator. Assigning means storing data in the variable. The equal sign in Python is not equality as in Mathematics.

_Example:_

```py
# Variables in Python
first_name = 'Adam'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 25
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Adam',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }
```

Let us use the _print()_ and _len()_ built-in functions. Print function takes unlimited number of arguments. An argument is a value which we can be passed or put inside the function parenthesis, see the example below.

**Example:**

```py
print('Hello, World!') # The text Hello, World! is an argument
print('Hello',',', 'World','!') # It can take multiple arguments, four arguments have been passed
print(len('Hello, World!')) # It takes only one argument
```

Let us print and also find the length of the variables declared at the top:

**Example:**

```py
# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)
```

### Declaring multiple variables in a line

Multiple variables can also be declared in one line:

**Example:**

```py
first_name, last_name, country, age, is_married = 'Adam', 'Yetayeh', 'Helsink', 25, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
```

Getting user input using the _input()_ built-in function. Let us assign the data we get from a user into first_name and age variables.
**Example:**

```py
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)
```

## Data types

There are several data types in Python. To identify the data type we use the _type_ built-in function. I would like to ask you to focus on understanding different data types very well. When it comes to programming, it is all about data types. I introduced data types at the very beginning and it comes again, because every topic is related to data types. We will cover data types in more detail in their respective sections.

## Checking data types and casting

- Check Data types: To check the data type of certain data/variable we use the _type_
  **Example:**

```py
# Different python data types
# Let's declare variables with various data types

first_name = 'Adam' # str
last_name = 'Yetayeh' # str
country = 'Finland' # str
city= 'Helsinki' # str
age = 25 # int

# Printing out types
print(type('Adam')) # str
print(type(first_name)) # str
print(type(10)) # int
print(type(3.14)) # float
print(type(1 + 1j)) # complex
print(type(True)) # bool
print(type([1, 2, 3, 4])) # list
print(type({'name':'Adam','age':25, 'is_married':25})) # dict
print(type((1,2))) # tuple
print(type(zip([1,2],[3,4]))) # set
```

- Casting: Converting one data type to another data type. We use _int()_, _float()_, _str()_, _list_, _set_
  When we do arithmetic operations string numbers should be first converted to int or float otherwise it will return an error. If we concatenate a number with a string, the number should be first converted to a string. We will talk about concatenation in String section.

  **Example:**

```py
# int to float
num_int = 10
print('num_int',num_int) # 10
num_float = float(num_int)
print('num_float:', num_float) # 10.0

# float to int
gravity = 9.81
print(int(gravity)) # 9

# int to str
num_int = 10
print(num_int) # 10
num_str = str(num_int)
print(num_str) # '10'

# str to int or float
num_str = '10.6'
print('num_int', int(num_str)) # 10
print('num_float', float(num_str)) # 10.6

# str to list
first_name = 'Adam'
print(first_name) # 'Adam'
first_name_to_list = list(first_name)
print(first_name_to_list) # ['A', 'd', 'a', 'm']
```

## Numbers

Number data types in Python:

- Integers: Integer(negative, zero and positive) numbers
  Example:
  ... -3, -2, -1, 0, 1, 2, 3 ...

- Floating Point Numbers(Decimal numbers)
  Example:
  ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...

- Complex Numbers
  Example:
  1 + j, 2 + 4j, 1 - 1j
