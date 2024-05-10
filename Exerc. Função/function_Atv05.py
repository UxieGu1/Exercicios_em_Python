"""Faça uma função que retorne o reverso de um número inteiro informado. No caso o número
será uma String Por exemplo: 127 -> 721"""

def reverse(valor):
    size = len(valor) - 1 
    for c in range(size, -1, -1):
        print(valor[c])

string = input(f'Digite o valor/texto a ser revertido: ')
reverse(string)
