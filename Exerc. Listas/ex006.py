#06.Crie um programa que declare uma lista L, a qual você pode preenchê-la aleatoriamente com
#números entre 1 e 20. Em seguida, o programa deve calcular a média aritmética entre o menor
#e o maior elemento da lista L. Ao fim, o programa deve imprimir a média aritmética encontrada
#e verificar se existe esse número na lista.
import random as rd

lista = []

def tamanhoLista():
    return int(input(f'Digite o tamanho da lista a ser preenchida: '))

def preencherLista(size):
    for i in range(size):
        numeros = rd.randint(1, 26) 
        lista.append(numeros)

def calcularMedia():
    lista.sort()
    media = (lista[0] + lista[-1]) / 2
    print(f'A média aritmética dos valores é: {media}')

def verificarValor(media):
    if media in lista:
        print(f'A média {media} existe na lista!')
    else:
        print(f'A média {media} não existe na lista!')

size = tamanhoLista()
preencherLista(size)
calcularMedia()
media = (lista[0] + lis
