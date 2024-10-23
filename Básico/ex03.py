# Considere a fórmula para cálculo de juros simples, J = (C × I × T) / 100, onde J, C, I e T
# correspondem a juros, capital, taxa e tempo, respectivamente. Construa um código que
# solicite ao usuário os valores de C, I e T e calcule J.

capital = float(input('Insira o valor do capital: '))
taxa = float(input('Insira a taxa: '))
tempo = float(input('Insira o tempo: '))

juros = (capital * taxa * tempo) / 100
print(f'Juros: {juros}')