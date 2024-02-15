# Exceptiociones o manejo de errores
n1, n2 = 5,1
n2 = "1"
"""
#criterios de aceptacion
if type(n2)==int:
    print (n1+n2)
else:
    print("no se cumpli")
    """
## try except 
try:
    print(n1+n2)
    print("no hay errores")
except:
    print("hay errores ")
    
#try execpt else
try:
    print(n1+n2)
    print("no hay errores")
except:
    print("se haproduceid un error")
else:
    # se ejecuta si no se produce una exception
    print("continua la ejecuci[on]")
finally: #opcional
    # se ejecuta siempre
    print("contunia la ejecucuion de finally")
    
#exceptionces por tipo
try:
    print(n1+n2)
    print("no hay errore")
except ValueError :
    print("se ha producido un erroe valuerror")
except TypeError:
    # se ejeucuta si se produce una exception
    print("se ha producido un error un typeError")
    
#captura de la informaci[on de la exception] 
try:
    print(n1+n2)
    print("no hay errore")
except ValueError as error:
    print(error)
except Exception as error:
    print(error)


