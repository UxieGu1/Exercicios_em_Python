#Faça um programa que insira 10 números aleatórios de 1 a 100 em uma lista. 
#Em seguida percorra a lista e conte quantos números são pares ou impares e 
#quantos são maiores e menores que 50.
 import random as rd

numeros = []
def preencherLista(n):
  for i in range(10):
    numeros_random = rd.randint(1, 100)
    numeros.append(numeros
    print(numeros)
def contarParImpar():
  contPar = 0
  contImpar = 0
  for value in numeros:
    if value % 2 == 0:
      contPar += 1
    else:
      contImpar += 1
    print(f'A quantidade de números pares é: {contPar}')
    print(f'A quantidade de números ímpares é: {contImpqr}')
def maior_menor50():
  maior50 = 0
  menor50 = 0
  for value in numeros:
    if value > 50:
      maior50 += 1
    else:
      menor50 += 1
    print(f'A quantida de números maiores que 50 são: {maior50}')
    print(f'A quantida de números menores que 50 são: {menor50}')

preencherLista()
contarParImpar()
maior_menor50()
