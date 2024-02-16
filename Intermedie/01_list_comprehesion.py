#Listas Compresión
my_origin_list = [35,15,489,25,256,36]
my_list = [i for i in my_origin_list]
print(my_list)

my_list=[i +1 for i in range(10)]
print(my_list)

my_range = range(10)
print(list(my_range))

my_list=[i * 2 for i in range(10)]
print(my_list)


my_list=[i * i for i in range(10)]
print(my_list)

def sum_five(n):
    return n * 5

my_list = [sum_five(i) for i in range(10)]
print(my_list)
