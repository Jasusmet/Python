# _Regular Expressions_

A regular expression or RegEx is a special text string that helps to find patterns in data. A RegEx can be used to check if some pattern exists in a different data type. To use RegEx in python first we should import the RegEx module which is called re.

## Index

- [The _re_ module](#the-re-module)
- [Methods in _re_ module](#methods-in-re-module)
  - [re.match()](#rematch)
  - [re.search()](#research)
  - [re.findall()](#refindall)
  - [re.sub()](#resub)
  - [re.split()](#resplit)
- [Writing RegEx patterns](#writing-regex-patterns)
  - [Square bracket](#square-bracket)
  - [Escape character(\\) in RegEx](#escape-character-in-regex)
  - [One or more times(+)](#one-or-more-times)
  - [Period(.)](#period)
  - [Zero or more times(\*)](#zero-or-more-times)
  - [Zero or one time(?)](#zero-or-one-time)
  - [Quantifier in RegEx](#quantifier-in-regex)
  - [Cart ^](#cart-)

### The _re_ module

After importing the module we can use it to detect or find patterns.

```py
import re
```

### Methods in _re_ module

To find a pattern we use different set of _re_ character sets that allows to search for a match in a string:

#### re.match()

Searches only in the beginning of the first line of the string and returns matched objects if found, else returns None

```py
# Syntax
re.match(substring, string, re.I)
# Substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore
```

```py
import re

txt = 'I love to teach python and javaScript'
# It returns an object with span, and match
match = re.match('I love to teach', txt, re.I)
print(match) # <re.Match object; span=(0, 15), match='I love to teach'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span) # (0, 15)
# Let's find the start and stop position from the span
start, end = span
print(start, end) # 0, 15
substring = txt[start:end]
print(substring) # I love to teach
```

As you can see from the example above, the pattern we are looking for (or the substring we are looking for) is _I love to teach_. The match function returns an object **only** if the text starts with the pattern.

```py
import re

txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)
print(match) # None
```

The string does not string with _I like to teach_, therefore there was no match and the match method returned None.

#### re.search()

Returns a match object if there is one anywhere in the string, including multiline strings

```py
# Syntax
re.match(substring, string, re.I)
# Substring is a pattern, string is the text we look for a pattern , re.I is case ignore flag
```

```py
import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns an object with span and match
match = re.search('first', txt, re.I)
print(match) # <re.match object; span=(100, 105), match='first'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span) # (100, 105)
# Let's find the start and stop position from the span
start, end = span
print(start, end) # 100, 105
substring = txt[start:end]
print(substring) # First
```

As you can see, search is much better than match because it can look for the pattern throughout the text. Search returns a match object with a first match that was found, otherwise it returns _None_. A much better _re_ function is _findall_. This function checks for the pattern through the whole string and returns all the matches as a list.

#### re.findall()

Returns all the matches as a list

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
print(matches) # ['language', 'language']
```

As you can see, the word _language_ was found two times in the string. Let us practice some more.
Now we will look for both Python and python words in the string:

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns list
matches = re.findall('python', txt, re.I)
print(matches) # ['Python', 'python']

```

Since we are using _re.I_ both lowercase and uppercase letters are included. If we do not have the re.I flag, then we will have to write our pattern differently. Let us check it out:

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('Python|python', txt)
print(matches) # ['Python', 'python']

#
matches = re.findall('[Pp]ython', txt)
print(matches) # ['Python', 'python']

```

#### re.sub()

Replaces one or many matches within a string

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced) # JavaScript is the most beautiful language that a human being has ever created.
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced) # JavaScript is the most beautiful language that a human being has ever created.
```

Let us add one more example. The following string is really hard to read unless we remove the % symbol. Replacing the % with an empty string will clean the text.

```py

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)
```

```sh
I am teacher and I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs. Does this motivate you to be a teacher?
```

#### re.split()

Takes a string, splits it at the match points, returns a list

```py
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt)) # Splitting using \n - end of line symbol
```

```sh
['I am teacher and  I love teaching.', 'There is nothing as rewarding as educating and empowering people.', 'I found teaching more interesting than any other jobs.', 'Does this motivate you to be a teacher?']
```

## Writing RegEx patterns

To declare a string variable we use a single or double quote. To declare RegEx variable _r''_.
The following pattern only identifies apple with lowercase, to make it case insensitive either we should rewrite our pattern or we should add a flag.

```py
import re

regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches) # ['apple']

# To make case insensitive adding flag '
matches = re.findall(regex_pattern, txt, re.I)
print(matches) # ['Apple', 'apple']
# Or we can use a set of characters method
regex_pattern = r'[Aa]pple' # This mean the first letter could be Apple or apple
matches = re.findall(regex_pattern, txt)
print(matches) # ['Apple', 'apple']

```

- []: A set of characters
  - [a-c] means, a or b or c
  - [a-z] means, any letter from a to z
  - [A-Z] means, any character from A to Z
  - [0-3] means, 0 or 1 or 2 or 3
  - [0-9] means any number from 0 to 9
  - [A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9
- \\: uses to escape special characters
  - \d means: match where the string contains digits (numbers from 0-9)
  - \D means: match where the string does not contain digits
- . : any character except new line character(\n)
- ^: starts with
  - r'^substring' eg r'^love', a sentence that starts with a word love
  - r'[^abc] means not a, not b, not c.
- $: ends with
  - r'substring$' eg r'love$', sentence that ends with a word love
- \*: zero or more times
  - r'[a]\*' means a optional or it can occur many times.
- +: one or more times
  - r'[a]+' means at least once (or more)
- ?: zero or one time
  - r'[a]?' means zero times or once
- {3}: Exactly 3 characters
- {3,}: At least 3 characters
- {3,8}: 3 to 8 characters
- |: Either or
  - r'apple|banana' means either apple or a banana
- (): Capture and group

![Regular Expression cheat sheet](../00_Images/regex.png)

Let's use examples to clarify the meta characters above

### Square bracket

Let us use square bracket to include lower and upper case

```py
regex_pattern = r'[Aa]pple' # This square bracket mean either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches) # ['Apple', 'apple']
```

If we want to look for the banana, we write the pattern as follows:

```py
regex_pattern = r'[Aa]pple|[Bb]anana' # This square bracket means either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches) # ['Apple', 'banana', 'apple', 'banana']
```

Using the square bracket and or operator , we manage to extract Apple, apple, Banana and banana.

### Escape character(\\) in RegEx

```py
regex_pattern = r'\d' # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches) # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1'], this is not what we want
```

### One or more times(+)

```py
regex_pattern = r'\d+' # d is a special character which means digits, + mean one or more times
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches) # ['6', '2019', '8', '2021'] - now, this is better!
```

### Period(.)

```py
regex_pattern = r'[a].' # This square bracket means a and . means any character except new line
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches) # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+' # . any character, + any character one or more times
matches = re.findall(regex_pattern, txt)
print(matches) # ['and banana are fruits']
```

### Zero or more times(\*)

Zero or many times. The pattern could may not occur or it can occur many times.

```py
regex_pattern = r'[a].*' # . any character, * any character zero or more times
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches) # ['and banana are fruits']
```

### Zero or one time(?)

Zero or one time. The pattern may not occur or it may occur once.

```py
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail' # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches) # ['e-mail', 'email', 'Email', 'E-mail']
```

### Quantifier in RegEx

We can specify the length of the substring we are looking for in a text, using a curly bracket. Let us imagine, we are interested in a substring with a length of 4 characters:

```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}' # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches) # ['2019', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1, 4}' # 1 to 4
matches = re.findall(regex_pattern, txt)
print(matches) # ['6', '2019', '8', '2021']
```

### Cart ^

- Starts with

```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This' # ^ means starts with
matches = re.findall(regex_pattern, txt)
print(matches) # ['This']
```

- Negation

```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+' # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches) # ['6,', '2019', '8', '2021']
```

## Exercises

1. What is the most frequent word in the following paragraph?

```py
    paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.
```

```sh
    [
    (6, 'love'),
    (5, 'you'),
    (3, 'can'),
    (2, 'what'),
    (2, 'teaching'),
    (2, 'not'),
    (2, 'else'),
    (2, 'do'),
    (2, 'I'),
    (1, 'which'),
    (1, 'to'),
    (1, 'the'),
    (1, 'something'),
    (1, 'if'),
    (1, 'give'),
    (1, 'develop'),
    (1, 'capabilities'),
    (1, 'application'),
    (1, 'an'),
    (1, 'all'),
    (1, 'Python'),
    (1, 'If')
    ]
```

```py
import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

# Split the paragraph into words using regular expressions
words = re.findall(r'\b\w+\b', paragraph.lower())

# Create a dictionary to store the word frequencies
word_freq = {}

# Count the frequency of each word
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Find the most frequent word
most_frequent_word = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[0]

print(f'The most frequent word is "{most_frequent_word[0]}" which appears {most_frequent_word[1]} times.')
```

2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.

```py
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-12) # 20
```

```py
import re

text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

# Extract numbers from the text using regular expressions
numbers = re.findall(r'-?\d+', text)
numbers = [int(num) for num in numbers]

# Sort the numbers in ascending order
sorted_numbers = sorted(numbers)

# Find the distance between the two furthest particles
distance = sorted_numbers[-1] - sorted_numbers[0]

print("Extracted numbers:", numbers) # [-12, -4, -3, -1, 0, 4, 8]
print("Sorted numbers:", sorted_numbers) # [-12, -4, -3, -1, 0, 4, 8]
print("Distance between the two furthest particles:", distance) # 20
```
