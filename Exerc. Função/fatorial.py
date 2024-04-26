"""Escreva uma função que receba como entrada um número inteiro e retorne o fatorial desse
número."""

def fatorial(num):
    total = 1
    for i in range(num, 0, -1):
        print(i, end=" ")
        total *= i

    print(f"Total é {total}")

valor =int(input("Digite um valor inteiro: "))
fatorial(valor)
