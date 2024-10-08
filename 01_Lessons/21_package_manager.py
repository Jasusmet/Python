### Package Manager ###

# PIP https://pypi.org

import numpy # pip install numpy

from mypackage import arithmetics

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))

print(numpy_array * 2)

import pandas # pip install pandas

# pip list
# pip uninstall
# pip show numpy

#pip install requests
import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
print(response)
print(response.status_code)
print(response.json())

# Arithmetics Package

print(arithmetics.sum_two_values(1, 4))