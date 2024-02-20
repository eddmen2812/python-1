#   Funciones de orden alto
from functools import reduce
def sum_one(n1):
    return n1+1

def sum_five(n1):
    return n1+5
def sum_v (n1,n2,f):
    return f(n1+n2)

print(sum_v(5,2,sum_one))
print(sum_v(5,2,sum_five))

#Closures

def sum_ten(n1o):
    def add(n1):
        return n1 + 10+n1o
    return add
add_closs = sum_ten(1)
print(add_closs(5))
print((sum_ten(5))(1))

#   Funciones de orden alto que esten en el leguaje
#map

num = [2,5,10,20]
def mult(n):
    return n * 2

print(list(map(mult, num)))

print(list(map(lambda n1:n1*2,num)))

# Filter
def filt_val(n1):
    if n1 > 10:
        return True
    return False
print(list(filter(filt_val, num)))
print(list(filter(lambda n1:n1 > 10, num)))

#Reduce
num = [2,5,10,20]
def sum_2_values(n1,n2):
    print(n1)
    print(n2)
    return n1+n2
print(reduce(sum_2_values, num))