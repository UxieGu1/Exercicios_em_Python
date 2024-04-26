"""Construa um programa que receba o nome e o preço de 5 medicamentos de
uma drogaria (considere que o usuário informou cinco medicamentos
distintos). O programa deve informar o nome e o preço do medicamento mais
barato, bem como a média aritmética dos preços informados."""

precobarato = 1000
nomebarato = " "
media = 0
i = 0
while i < 5:
    nome = input('Digite o nome do medicamento: ')
    preco = int(input('Digite o preço do medicamento: '))
    media += preco
    i += 1

    if preco < precobarato:
        precobarato = preco
        nomebarato = nome
print('O nome do medicamento mais barato é ', nomebarato, 'e o preço é R$', precobarato)
print('A media de preço é ', media / 5)