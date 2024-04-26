"""Crie um programa que calcule a média de um conjunto de números inteiros informados pelo
usuário. O programa deve solicitar ao usuário a quantidade de números que serão informados e, em
seguida, solicitar cada um desses números. Ao final, o programa deve exibir a média APENAS DOS
NÚMEROS IMPARES."""

quantidade = int(input("Quantidade de números a serem informados: "))
numeros = []
soma = 0
contador = 0

for i in range(quantidade):
    numero = int(input("Informe o número: "))
    numeros.append(numero)

    if numero % 2 != 0:
        soma += numero
        contador += 1

if contador == 0:
    print("Nenhum número ímpar foi informado.")
else:
    media = soma / contador
    print("A média dos números ímpares é:", media)
