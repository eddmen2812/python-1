# Gestor de paquetes para python
# pip #https://pypi.org

import numpy
print(numpy.version.version)
num_array = numpy.array([35,45,87,952,4851,7,14,147,562,56])
print(type(num_array))
print(num_array * 2)

import pandas 
# pip list
# pip show numpy

import requests
response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())
#Aritmetchis Package
from my_package import arithmetrics
print(arithmetrics.sum_2_values(1,2))

from other_package import other_aritm
print(other_aritm.sum_2_values(3,6))

