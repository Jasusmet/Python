# Questions & Answers

Interviews are stressful for everyone. Candidates are trying to present themselves as fitting for the job and great employees while hiring managers want to create a comfortable environment and find their perfect employee through a couple of basic Python interview questions.

However, a little bit of preparation goes a long way for both parties. It will help Python developers reduce stress and do their best and hiring managers will know what Python advanced interview questions to ask to get the most accurate picture of the candidate.

Here is the list of Python interview questions and answers that can help you prepare and go through the most successful and efficient interviews!

## Junior Python Developer Interview Questions

### 01 - What is Python mostly used for?

<details>
  <summary><b>Show/Hide Answer</b></summary>
  <br>

<b>Python is a versatile programming language used for a wide range of applications.</b> Here are some of it's common uses:

- <b>Data Science and Machine Learning:</b> Python's readability and extensive libraries like _NumPy_, _Pandas_, and _Scikit-learn_ make it a popular choice for data analysis, visualization and building machine learning models.

- <b>Web Development:</b> Frameworks like _Django_ and _Flask_ provide a robust foundation for creating dynamic and scalable web applications.

- <b>Scientific Computing:</b> Python is used in fields like physics, chemistry and biology for simulations, data analysis and numerical computations.

- <b>Automation:</b> Python's scripting capabilities can be used to automate repetitive tasks, such as file management, web scraping or system administration.

- <b>Game Development:</b> Python can be used to create games, especially 2D games and prototypes, using libraries like _Pygame_.

- <b>Artificial Intelligence:</b> Python's simplicity and powerful AI libraries like _TensorFlow_ and _PyTorch_ make it a popular choice for developing AI applications.

In essence, Python's versatility, readability and extensive ecosystem of libraries make it a valuable tool for a wide variety of tasks in the tech industry and beyond.

</details>

### 02 - Is Python case-sensitive?

<details>
  <summary><b>Show/Hide Answer</b></summary>
  <br>

<b>Yes, Python is case-sensitive.</b> This means that it treats uppercase and lowercase characters differently. For example, `myVariable` and `myvariable` are considered two distinct variables in Python.

</details>

### 03 - Is Python an interpreted language?

<details>
  <summary><b>Show/Hide Answer</b></summary>
  <br>

<b>Yes, Python is an interpreted language.</b> This means that the code is executed line by line, without the need for a compilation step. This can make it easier to develop and test code, but it can also result in slower execution compared to compiled languages.

</details>

### 04 - What is slicing in Python?

<details>
  <summary><b>Show/Hide Answer</b></summary>
  <br>

Slicing is a powerful technique used to extract a specific portion of a sequence data type, such as a string, list, or tuple. It involves specifying a range of indices using square brackets, where the indices start from 0.

#### Basic syntax:

```py
sequence[start:stop:step]
```

- start: The index of the first element to include (default is 0)
- stop: The index of the first element to exclude (default is the length of the sequence)
- step: The number of elements to skip between each element (default is 1)

#### Examples

#### String slicing:

```py
my_string = "Hello, World!"

# Extract the first 5 characters
first_5 = my_string[:5] # Output: "Hello"

# Extract characters from index 7 to 10 (inclusive)
substring = my_string[7:11] # Output: "World"

# Extract every other character
every_other = my_string[::2] # Output: "Hlo ol!"
```

#### List slicing:

```py
my_list = [1, 2, 3, 4, 5]

# Extract the first 3 elements
first_3 = my_list[:3] # Output: [1, 2, 3]

# Extract elements from index 2 to 4 (inclusive)
sublist = my_list[2:5] # Output: [3, 4, 5]

# Reverse the list
reversed_list = my_list[::-1] # Output: [5, 4, 3, 2, 1]
```

#### Tuple slicing:

```py
my_tuple = (10, 20, 30, 40, 50)

# Extract the last 3 elements
last_3 = my_tuple[-3:] # Output: (30, 40, 50)

# Extract elements from index 1 to 3 (inclusive)
subtuple = my_tuple[1:4] # Output: (20, 30, 40)
```

#### Key points:

- Negative indices can be used to count from the end of the sequence.
- If the start or stop index is omitted, the default is the beginning or end of the sequence, respectively.
- If the step is negative, the sequence is sliced in reverse order.
</details>

### 05 - How to delete a file from Python?

<details>
  <summary><b>Show/Hide Answer</b></summary>
  <br>

To delete a file in Python, you can use the `os.remove()` functions fromt the `os` module. Here's how to use it:

```py
import os

file_path = "path/to/your/file.txt"

try:
  os.remove(file_path)
  print("File deleted successfully.")
except FileNotFoundError:
  print ("File not found".)
```

Replace `"path/to/your/file.txt"` with the actual path to the file you want to delete.

</details>

### 06 - What are built-in data types in Python?

<details>
  <summary><b>Show/Hide Answer</b></summary>
  <br>

Python provides several built-in data types that can be used to store different kinds of values. Here's a breakdown of the most common ones:

#### Numerical data types

- int: Represents integers (10, -5, 0)
- float: Represents floating-point numbers (3.14, -2,5)
- complex: Represents complex numbers (2+3j)

#### Sequence data types

- list: Ordered collection of items, allowing duplicates.
- tuple: Ordered, immutable collection of items.
- range: Sequence of numbers.
- str: Sequence of characters.

#### Mapping data type

- dict: Unordered collection of key-value pairs.

#### Set data types

- set: Unordered collection of unique items.
- frozenset: Immutable set.

#### Boolean data type

- bool: Represents True or False values.

#### None data type

- None: Represents the absence of a value.

#### Example:

```py
# Creating variables of different data types
x = 10 # int
y = 3.14 # float
z = 2+3j # complex

my_list = [1, 2, 3] # list
my_tuple = (4, 5, 6) # tuple
my_dict = {'name': 'Alice', 'age': 30} # dict
my_set = {7, 8, 9} # set

# Printing the data types
print(type(x))
print(type(y))
print(type(z))
print(type(my_list))
print(type(my_tuple))
print(type(my_dict))
print(type(my_set))
```

This code will output the data types of each variable.

</details>

### 07 - What's the difference between tuples and lists in Python?

<details>
  <summary><b>Show/Hide Answer</b></summary>
  <br>

In Python, tuples and lists are both used to store collections of elements. However, they have some key differences:

#### Tuples:

- Immutable: Once created, tuples cannot be modified. This means you cannot add, remove or change elements in a tuple.

- Enclosed in parentheses: Tuples are defined using parentheses, e.g., `my_tuple = (1, 2, 3)`.

- Used for:

  - Storing fixed collections of elementes that won't change.

  - Returning multiple values from a function.

  - Creating keys for dictionaries.

#### Lists:

- Mutable: Lists can be modified after creation. You can add, remove or change elements using various methods.

- Enclosed in square brackets: Lists are defined using square brackets. e.g., `my_list = [1, 2, 3]`.

- Used for:

  - Storing collections of elements that may change over time.

  - Performing operations like sorting, filtering and appending.
  </details>

### 08 - What's the difference between pass by value and pass by reference?

<details>
  <summary><b>Show/Hide Answer</b></summary>
  <br>

In Python, arguments are passed to functions by reference, not by value. This means that when you pass a variable to a function, the function receives a reference to the object that the variable is pointing to. If the function modifies the object, the changes will be visible outside the function as well.

#### Pass by value:

- A copy of the variable's value is passed to the function.

- Any modifications made inside the function do not affect the original variable.

- Typically used for primitive data types like numbers and strings.

#### Pass by reference:

- A reference to the variable's object is passed to the function.

- Modifications made inside the function affect the original object.

- Typically used for complex data types like lists, dictionaries, and objects.

#### Example:

```py
def modify_list(my_list):
    my_list.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list) # Output: [1, 2, 3, 4]
```

In this example, `modify_list` receives a reference to the `my_list` object. When it appends the value 4, the original `my_list` is modified as well.
</details>

### 09 - What are pickling and unpickling?

<details>
  <summary><b>Show/Hide Answer</b></summary>
  <br>

<b>Pickling and unpickling</b> are processes in Python that allow you to serialize and deserialize objects. This means converting Python objects into a byte stream (pickling) and then converting that byte stream back into the original Python objetct (unpickling).

<b>Pickling</b> is useful when you need to:

- Save an object's state: Store the object's data and attributes for later use.

- Transmit an object: Send the object over a network or store it in a file.

- Create a persistent object: Make the object available for use in different Python sessions.

<b>Unpickling</b> is used to:

- Restore an object's state: Recreate the original object from it's pickled representation.

- Load an object from a file or network: Retrieve the object and use it in your code.

#### How it works:

#### Pickling:

- The `pickle` module is used to serialize the object.

- The object's data and attributes are converted into a byte stream.

- The byte stream can be written to a file or transmitted over a network.

#### Unpickling:

- The `pickle` module is used to deserialize the byte stream.

- The original object is reconstructed from the byte stream.

#### Example:

```py
import pickle

# Create a list
my_list = [1, 2, 3, "hello"]

# Pickle the list
with open("my_list.pkl", "wb") as f:
    pickle.dump(my_list, f)

# Unpickle the list
with open("my_list.pkl", "rb") as f:
    unpickled_list = pickle.load(f)

print(unpickled_list) # Output: [1, 2, 3, 'hello']
```

#### Important considerations:

- Security: Pickling can be a security risk if you unpickle untrusted data, as it can potentially execute malicious code. Be cautious when unpickling data from unknown sources.

- Compatibility: Pickling can be sensitive to changes in the object's structure or the version of Python used. Ensure compatibility when using pickled data.

- Alternatives: While pickling is a convenient way to serialize objects, there are other options available, such as *JSON* and *msgpack*, which may be more suitable for certain use cases.
</details>

## Mid Python Developer Interview Questions

