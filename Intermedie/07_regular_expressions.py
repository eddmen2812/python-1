# Expresiones Regulares
#Match
import re
my_strings = "Esta es la lección número 7: Lección Regular Expresiones"
my_other_s = "Esta no es la lección 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_strings, re.I)
print(match)
span = match.span()
print(span)
start, end = match.span()
print(my_strings[start:end])


match = print(re.match("Regular_Expressions",my_other_s))
# match != None #Otra forma de ahcerlo
# match is not None #Otra forma de hacerlo
if not (match == None):
    print(match)
    start,end = match.span()
    print(my_other_s[start:end])

print(re.match("esta es la lección", my_strings,re.I))
print(re.match("Esta es la lección",my_other_s))

#Serach
search = re.search("lección", my_strings, re.I)
print(search)
start, end = search.span()
print(my_strings[start:end])

# findall
findall = re.findall("lección",my_strings, re.I)
print(findall)

#splt
split = (re.split(":", my_strings))
print(split)

#sub
sub = re.sub("Expresiones","EXPRESIONES", my_strings)
print(sub)
sub = re.sub("lección | Lección","LECCIONN", my_strings)
print(sub)

#Patterns
patter = r"[lL]ección"
print(re.findall(patter, my_strings))

patter = r'[lL]ección|Expresiones'
print(re.findall(patter, my_strings))

patter = r'[0-9]'
print(re.findall(patter, my_strings))
print(re.match(patter, my_strings))
print(re.search(patter, my_strings))

patter = r"\D"
print(re.findall(patter, my_strings))

patter = r"[l].*"
print(re.findall(patter, my_strings))

#email validaton (regex)
#Aprender expresiones regulares : https://regex101.com
email = "edimen@correo.com"
pattn = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-9-.]+$"
print(re.search(pattn, email))
print(re.findall(pattn, email))
print(re.match(pattn, email))
/*
