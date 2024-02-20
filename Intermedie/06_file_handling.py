# Manejo de Ficheros
import os
# .txt file
txt_file= open("Intermedie/my_file.txt", "w+") #leer y escribir

txt_file.write("Yo me llamare Edison Mendoza\nMe apellidare Mnedoza Alma\nEdad de 29 a;os\ny me agrada Astro | Python")
#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline())
#print(txt_file.readlines())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAlgo m[as] para agrregar y es git")

print(txt_file.readline())

txt_file.close()
#os.remove("Intermedie/my_file.txt")

# .json file
import json
json_file = open("Intermedie/my_file.json", "w+")
json_test = {
    "name":"Edison",
    "lastn":"Mendoza",
    "age":29,
    "lengs":[
        "Astro",
        "Go",
        "Python"
        ],
    "site":"https://eddmen2812.github.io/edisonmendoza"
}

json.dump(json_test,json_file,indent=4)
json_file.close()
#json.dump(json_test,json_file,indent=2)

    
with open("Intermedie/my_file.json") as my_ot_file:
    for line in my_ot_file.readlines():
        print(line)
        
        
json_dict =(json.load(open("Intermedie/my_file.json")))
print(json_dict)
print(type(json_dict))
print(json_dict["lastn"])

# .cvs file
import csv
csv_file = open("Intermedie/my_file.csv","w+")
csv_writer = csv.writer(csv_file)
csv_writer.writerow([
    "name",
    "last",
    "age",
    "lang",
    "site"
])
csv_writer.writerow([
    "Edison",
    "Mendoza",
    29,
    "https://eddmen2812.github.io/edisonmendoza"
])
csv_writer.writerow([
    "Carlos",
    "Indal",
    19,
    "https://ecarlosidal.com"
])

csv_file.close()

with open("Intermedie/my_file.csv") as my_csv:
    for line in my_csv.readlines():
        print(line)

#.xlsx file
#import xlrd # debe instalrse este modulo
#.xml file
import xml