"""Faça uma função que receba o número inteiro. Esse número inteiro corresponde ao número
de vezes que um dado foi arremessado. A função deverá gerar um número aleatório entre 1
e 6. Faça o programa mostrar quantas vezes o número 5 saiu.
Para usar a função Random do Python, deverá importar a biblioteca Random no inicio do
código. Exemplo :"""

import random

def dado(number): 
    resultados = []
    for i in range(number):
        randomN = random.randint(0, 6)
        resultados.append(randomN)
        qtd_cinco = resultados.count(5)
        print(qtd_cinco)

dado(10) 
