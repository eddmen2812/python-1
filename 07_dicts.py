#Diccionarios
my_dict=dict()
print(f"{type(my_dict)}")

my_other_dict={}
print(f"{type(my_other_dict)}")

my_other_dict={"NOMBRE":"EDISON","APELLIDO":"MENDOZA","EDAD":39,1:"pYTHON"}

my_dict= {
    "NOMBRE":"EDISON","APELLIDO":"MENDOZA",
    "EDAD":39,
    "Lenguajes":{"pYTHON","Swictj","Ktrlin"},
    1:1.77
    }

print(my_other_dict)
print(my_dict)

print(f"{len(my_dict)}")
print(f"{len(my_other_dict)}")

my_dict["NOMBRE"]="LOLA"
print(f"{my_dict["NOMBRE"]}")

print(f"{my_dict["Lenguajes"]}")

print(f"{my_dict[1]}")

my_dict["DIRECCION"]="PUERTO QUITO"
print(f"{my_dict}")

del my_dict["DIRECCION"]
print(f"{my_dict}")

print(f"{"EDISON" in my_dict}")
print(f"{"NOMBRE" in my_dict}")

print(f"{my_dict.items()}")
print(f"{my_dict.keys()}")
print(f"{my_dict.values()}")

my_list = ["nombre1",11,"piso1"]
print(f"{dict.fromkeys(my_list)}")

print(f"{my_other_dict.fromkeys(("1","NOMBRE"))}")

my_new_dict = dict.fromkeys(("NOMBRE",1,"sola"))
print(f"{my_new_dict}")

my_new_dict = dict.fromkeys((my_dict))
print(f"{(my_new_dict)}")

my_new_dict = dict.fromkeys(my_dict,"oza")
print(f"{(my_new_dict)}")


my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(f"{dict.fromkeys(list(my_new_dict))}")
print(f"{tuple(my_new_dict)}")
print(f"{set(my_new_dict)}")