# Crie um programa que insira 9 números aleatórios em uma lista. Em seguida embaralhe esses
# números e insira em uma nova lista. Imprima as duas listas no formato de matriz e em seguida
# imprima a soma das duas no formato de matrizes também
import random
import numpy 

lista = []
colunas = 3
linhas = 3

for i in range(0, 9):
    lista.append(random.randint(0, 9))

matriz = numpy.array(lista).reshape(linhas, colunas)
print(matriz)

lista_embaralhada = lista[:]
random.shuffle(lista_embaralhada)

nova_matriz = numpy.array(lista_embaralhada).reshape(linhas, colunas)
print(nova_matriz)

soma_matrizes = matriz + nova_matriz
print(soma_matrizes)
