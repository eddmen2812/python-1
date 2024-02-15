#clases
class PersonVacia:
    pass

print(PersonVacia())

class Person:
    def __init__(self, name, surname,alias="sin alias"):
        self.full_n = f"{name} {surname} ({alias})"
    def walk(self):
        print(f"{self.full_n} Esta caminnado")
    
my_person=Person("EDISON","MENDOZA","deed28")
print(f"{my_person.full_n}")
my_person.walk()

my_other_person = Person("CARLS", "LOPEZ", "XCAD28")
print(my_other_person.full_n)
my_other_person.walk()
my_other_person.full_n = "Luis es un ejemplo"
print(my_other_person.full_n)