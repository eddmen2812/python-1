#Fuctions
def my_function():
    print("eSTO ES UNA FUNCIÓN")
my_function()

def sum_two_values (fn,sn):
    sum=fn+sn
    print(f"{sum}")
sum_two_values(10,10)
sum_two_values(1156100,10498456)
sum_two_values("10","10")
sum_two_values(120.15,10.23)

def sum_2_values_return(fn,sn):
    return sn+fn

my_result=sum_two_values(1.4,1.5)
print(my_result)

my_result=sum_2_values_return(10,10)
print(my_result)

def p_name(name, surnane):
    print(f"{name} {surnane}")
    
p_name(surnane="Mendoza",name="EDISON")

def p_name_default(name,surname,alias='Alias DESCONOCIDO'):
    print(f"{name} {surname} {alias}")
p_name_default("EDISON","MENDOZA")
p_name_default("edison","mendoza", "deed2812")

def p_text(*texts):
    #print(text)
    for text in texts:
        print(text.upper())
p_text("hola","mundo", "deed28")
p_text("holatext")