#Sets -> tiene array pero no existe en si, son listas
my_sets = set()
my_other_set={}

print(type(my_sets))
print(f"{type(my_other_set)}") #inicialmente es un dict

my_other_set={"EDISON", "MENDOZA", 35}
print(f"{type(my_other_set)}")

print(f"{len(my_other_set)}")

print(f"{my_other_set}")

my_other_set.add("EMMA")
print(f"{my_other_set}") # no es una estructuraordenada y no se puede acceder acada elemento o id para controlar

my_other_set.add("EMMA") # no admite repetidos pero en listas y tuplas si los caeptan
print(f"{my_other_set}")

print("EDISON"  in my_other_set)
print(f"{"edison" in my_other_set}")

my_other_set.remove("EDISON")
print(f"{my_other_set}")

my_other_set.clear()
print(f"{len(my_other_set)}")

del my_other_set
#print(f"{my_other_set}") # se carga la variable

my_sets={"EDUSON", "MENDOZA", 35}
my_list = list(my_sets)
print(f"{my_list}")
print(f"{my_list[0]}")

my_other_set = {"Hotilinn","Swithf","python"}
my_sew_set = my_other_set.union(my_sets)
print(f"{my_sew_set.union(my_sew_set).union({"Java","C+"})}")

print(f"{my_sew_set.difference(my_sets)}")