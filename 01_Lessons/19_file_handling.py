### File Handling ###

"""
So far we have seen different Python data types.
We usually store our data in different file formats.
In addition to handling files, we will also see different file formats(.txt, .json, .xml, .csv, .tsv, .excel) in this section.
First, let us get familiar with handling files with common file format(.txt).
File handling is an import part of programming which allows us to create, read, update and delete files.
In Python to handle data we use open() built-in function.
"""

import xml
import csv
import json
import os

# .txt file

# "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

txt_file = open("02_Intermediate/my_file.txt", "r+") # Read and write
print