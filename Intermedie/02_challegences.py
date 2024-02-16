#Challenges
"""
el Famoso FIZZ BUZZ
Con un print mostrar por consola los números del 1 al 100
(ambos incluidos y con un salto de linea entre cada compresión), sustituyendo lo siguiente:
- Múltiplos de 3 por la palabra fizz
- Multipos de 5 por la palabra buxx
- Multiplos de 3 y 5 a la vez por la palabara fizzbuzz
"""

def sec_num():
    for index  in range(1,101):
        if index % 3 == 0 and index % 5 == 0:
            print(f"{"fizzbuzz"}")
        elif index % 3 ==0:
            print(f"{"Fizz"}")
        elif index % 5 ==0:
            print(f"{"BUZZ"}")
        else:
            print(index)
sec_num()


"""
#ES UN ANAGRAMA':?
#Escribir una función que reciba dos palabras (strings) y retorne v o f (bool) según sean o no anagramas
- un anagrama consiste en formar una palabra reordenando Todas las letras
de otra palabra inicial.
- No hace falta comprobar ambas paabras existan.
- Dos palabras exactamente ifuales no son anagramas
"""

def rec_strings(p1,p2):
    if p1.lower() == p2.lower():
        return False
    return sorted(p1.lower()) == sorted(p2.lower())

print(rec_strings("Amor","Amor "))


#Fibonacci
"""
Escribe un programa que imprima los 50 primeros números de la sucesión de
Fibonacci empezando de 0.
- La serie de fibonnaci se commpone por una seucesión de números en 
la que el siguiente siempre es la suam de los dos anteriores.
0,1,1,2,3,5,8,13...
"""

def bifo():
    prev = 0
    next = 1
    for i in range(0,51):
        print(prev)
        
        fib = prev + next
        prev = next
        next = fib
bifo()

#Es un numero primo
""" 
Un script que compruebe cuando un número es primo y no primo
Imprime desde el uno al 1000
"""

def def_pri():
    for n in range(1,101):
        if n >= 2:
            is_divi = False
            
            for index in range(2,n):
                if n % index == 0:
                    is_divi = True
                    break
            if not is_divi:
                print(n)
        
def_pri()


#Inertido
"""
Un scritp que invierta el orden de una cadena de textp
sin usar funciones propias del lenguaje que lo automaticen
- si le pasamos hola mundo, nos retornaría odnum aloh
"""

def reversa(text):
    text_len = len(text)
    rever_text = ""
   
    for index in range(0,text_len):
        rever_text += text[text_len - index -1]
    return rever_text

print(reversa("hola mundo"))
