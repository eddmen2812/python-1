#Listas
my_list = list()
my_otrher_list = []
print(f"{len(my_list)}")

my_list = [29,15,23,30,30,15,50,10]
print(f"{my_list}")
print(f"{len(my_list)}")

my_otrher_list = [10,1.25,"EDI", "MEN"]
print(f"{type(my_otrher_list)}")
print(f"{type(my_list)}")

print(f"{my_otrher_list[0]}")
print(f"{my_otrher_list[1]}")
print(f"{my_otrher_list[-1]}")
#print(f"{my_otrher_list[5]}") #error
#print(f"{my_otrher_list[6]}")#error
print(f"{my_list.count(30)}")

age, heigth, name, surname = my_otrher_list
print(f"{name}")

print(f"{my_list+my_otrher_list}")
#print(f"{my_list+my_otrher_list}")#eeror
my_otrher_list.append("MENDOZA")
print(f"{my_otrher_list}")

my_otrher_list.insert(1,"AZUL")
print(f"{my_otrher_list}")

my_otrher_list.remove("AZUL")
print(f"{my_otrher_list}")

my_pop=my_list.pop(2)
print(f"{my_pop}")
print(f"{my_list}")

del my_list[2]
print(f"{my_list}")

my_new_list = my_list.copy()
my_list.clear()
print(f"{my_list}")
print(f"{my_new_list}")

my_new_list.reverse()
print(f"{my_new_list}")

my_new_list.sort()
print(f"{my_new_list}")

print(f"{my_new_list[2:5]}")
