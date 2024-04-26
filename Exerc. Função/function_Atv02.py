"""Criar uma função que retorna o seguinte: A função recebe 3 valores float e retornar o
quadrado do 1º + a soma dos outros dois. Imprima o resultado"""

def produto(n1, n2, n3):
    quadrado = n1** 2 + (n2 + n3)
    print(f"O resultado da expressão é: {quadrado}")
    
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))
produto(v1, v2, v3)