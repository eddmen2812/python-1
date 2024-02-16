#Lambdas
sum_lambda = lambda n1,n2: n1+n2
print(sum_lambda(25,56))

multilam = lambda n1,n2:n1*n2
print(multilam(5,5))

def sum_v(n1):
    return lambda n1,n2:n1+n1+n1
print(sum_v(5)(2,4))