# tipo de errores

# SyntaxError
#print "!Hola munco!"//Error
print("hola error")

# NameError
lengua = "Spanish" #comentar para que se vea el error
print(lengua)

# Index Errror
myList = ["Python","Astro","Go","JavaScript"]
print(myList[0])
print(myList[-1])
#print(myList[5])# Indeex error

#ModuleNotFoundError
#import maths# descomentar para error
import math

#AttributeError

#print(math.PI)# descomentar para ver el error
print(math.pi)

#KeyError
my_dict={"NOMBRE":"EDISON","APELLIDO":"MENDOZA", "EDAD":25, 1:"Pyhton"}
print(my_dict["EDAD"])
#print(my_dict["apellido"])#descomentar para ver error

#TypeError
#print(myList["0"])#descoemtar para ver el error
print(myList[1])

#ImportError
#from math import PI #descoemntar para ver el error
from math import pi
print (pi)

#ValueError
my_int = int("10")
#my_int = int ("10 Anios")#descomentar para ver el error
print(type(my_int))

#ZeroDisionError
print(4/2)
#print(4/0) #Descomentar para ver el error