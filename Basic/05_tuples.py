#Tuplas NO SON MUTABLES COMO LAS LISTAS (es decir rempalzar un id)
my_tuple=tuple()
my_other_tuple=(35,60,50,2.21)

my_tuple=(35,2.20,"EDISON","MENDOZA","MENDOZA")
print(f"{my_tuple}")
print(f"{type(my_tuple)}")

print(f"{my_tuple[0]}")
print(f"{my_tuple[-1]}")
#print(f"{my_tuple[4]}")#eeror
#print(f"{my_tuple[-6]}")#error

print(f"{my_tuple.count("MENDOZA")}")
print(f"{my_tuple.index("EDISON")}")
print(f"{my_tuple.index("MENDOZA")}")

#my_tuple[1]=1.80 #no es mutab;es
print(f"{my_tuple}")

sum_tupla=my_tuple+my_other_tuple
print(f"{sum_tupla}")

print(f"{sum_tupla[4:6]}")

my_tuple = list(my_tuple)
print(f"{type(my_tuple)}")

my_tuple[4] = "ALMACHI"
my_tuple.insert(1,"verde")
my_tuple = tuple(my_tuple)
print(f"{my_tuple}")
print(f"{type(my_tuple)}")

#del my_tuple[2]#error de eliminar xq no es mutable
del my_tuple
#print(f"{my_tuple}") #error | elimina definitivo
