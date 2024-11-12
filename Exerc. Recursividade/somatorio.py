# Escreva um método recursivo e estático que rebeba um número inteiro positivo N e
# calcule o somatório dos números de 1 a N.

def somatorio(n):    
    if n == 1:
        return 1
    else:
        return n + somatorio(n-1)
    
print(somatorio(5))
