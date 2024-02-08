# Strings
my_string ="mi estring"
my_other_s ="mi otro seting"
print(len(my_string))
print(len(my_other_s))

print(my_string + "" + my_other_s)
my_new_s="mi nuefo \n string"
print(my_new_s)

my_tab_s=("\t mi nuevo string")
print(my_tab_s)

#formateo
name, sur,age="edi", " men", 29
print("mi nombre es> {}{} y mi edad {}".format(name,sur,age))

print("mi nombre es %s %s y edad de> %d" %(name,sur,age))

print (f"mi nobre es {name} {sur} y edad de {age}")

# Desempecador de caracteres
lenguage="pyThon"
a,b,d,e,f,g=lenguage
print(f"{a}")
print(f"{b}")
print(f"{d}")
print(f"{b}")
print(f"{f}")
print(f"{g}")
# Division
lanague_slice = lenguage[1:3]
print(lanague_slice)

lanague_slice=lenguage[1:]
print(f"{lanague_slice}")

lanague_slice=lenguage[-2]
print(f"{lanague_slice}")

# reverse
reverse_languaje =lenguage[::-1]
print(f"{reverse_languaje}")

#Fuciones
print(lenguage.capitalize())
print(lenguage.upper())
print(lenguage.count("t"))
print(lenguage.isnumeric())
print("1".isnumeric())
print(f"{lenguage.lower()}")
print(f"{lenguage.lower().isupper()}")
print(f"{lenguage.startswith("py")}")
print("Py" == "py")

