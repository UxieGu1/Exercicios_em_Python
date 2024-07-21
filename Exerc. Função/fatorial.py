"""Escreva uma função que receba como entrada um número inteiro e retorne o fatorial desse
número."""

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)



valor =int(input("Digite um valor inteiro: "))
resultado = fatorial(valor)
print(resultado)
