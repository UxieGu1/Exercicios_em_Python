"""Criar uma função que receba um caractere como parâmetro e retorne 1 (um) caso seja uma
vogal e zero caso não seja"""

def vogal(c):
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        return 1
    else:
        print('0')

caractere = input('Digite um caractere: ')
vogal(caractere)