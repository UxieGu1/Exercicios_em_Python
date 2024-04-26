"""Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do
aluno e dar o seguinte resultado:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que três;
A mensagem “Recuperação”, se a média for maior igual a 3 e menor que sete
A mensagem "Aprovado com Distinção", se a média for igual a dez."""

n1 = int(input('Digite a primeira nota do aluno: '))
n2 = int(input('Digite a segunda nota do aluno: '))

media = (n1 + n2) / 2

if media >= 7:
    print('Aluno Aprovado!')

elif media < 3:
    print('Aluno Reprovado!')

elif media >= 3 or media < 7:
    print('Aluno em Recuperação!')

elif media == 10:
    print('Aluno Aprovado com distinção!')