# Loops | bucles | ciclos

# While

my_condition = 0

while my_condition < 10:
    print(f"{my_condition}")
    my_condition+=2
else: # es opcional
    print("mi condicicon es mayor o igual que 10")
print("contnua el bucle")

while my_condition < 20:
    my_condition+=1
    if my_condition ==15:
        print("mi condición es  y se detiene")
        break
    print(my_condition)
    
print("continúa el bucle")


#For -> intera una lista de elementos

my_lists=[35,25,26,87,101,14,0.0,12]

for element in my_lists:
    print(element)

my_tuple=(35,1.77,25,"Edison","Mendoza")
for element in my_tuple:
    print(element)


my_set={"Edison","Mendoza",29}
for element in my_set:
    print(f"{element}")


my_dict={"NOmbre":"Edison","Apellido":"Mendoza","edad":29,1:"P"}
for element in my_dict:
    print(f"{element}")
    
for element in my_dict.values():
    print(f"{element}")

else:
    print(f"{"Se acabo el for del cict"}")


for element in my_dict:
    print(f"{element}")
    if element == "edad":
        break
    print("Se asomo la edad")
else:
    print(f"{"Se acabo el for del cict"}")
print(f"{"c0nftinua el for"}") 


for element in my_dict:
    print(f"{element}")
    if element == "edad":
        continue #no es acosejable usarlo en la actualidad
    print("Se ejecuta")
else:
    print(f"{"Se acabo el for del cict"}")
print(f"{"c0nftinua el for"}")   
