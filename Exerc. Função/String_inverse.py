"""Escreva uma função que receba como entrada uma string e retorne uma nova string com os
caracteres em ordem inversa."""

def inverter(valor):
    tamanho = len(valor) - 1

    for s in range(tamanho,-1,-1):
        print(valor[s],end="")

palavra = input("Digite uma palavra/texto inteiro: ")
inverter(palavra)