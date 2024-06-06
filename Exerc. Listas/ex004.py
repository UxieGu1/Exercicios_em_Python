#04.Crie um programa que solicite o usuário um número N ímpar maior que 1.
#Em seguida, preencha uma lista com N números inteiros positivos (suponha que o 
#usuário sempre digitará números inteiros positivos). Selecione o elemento que está no centro da lista. Ao final, calcule e escreva o fatorial do elemento selecionado
import random as rd
import math as mt

numeros = []
def preencherLista(n):
    for i in range(n):
        numbers = rd.randint(1, 100)
        numeros.append(numbers)
    
def centro_da_lista():
    tamanho = len(numeros)
    if tamanho % 2 == 1:  
        centro = numeros[(tamanho - 1) // 2]
        print(f'O número que está no centro é: {centro}')
    else: 
        centro = numeros[tamanho // 2]
        print(f'O número que está no centro é: {centro}')
    fatorial = mt.factorial(centro)
    
    print(f'O fatorial do número do centro é: {fatorial}')


N = int(input(f'Digite o número ímpar a ser inserido: '))
preencherLista(N)
centro_da_lista()
