""" Desenvolver um programa para verificar a nota do aluno em uma prova com 5 questões, o programa
deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova (cada
questão possui alternativas de A até E) e assim calcular o total de acertos e a nota (atribuir 2 pontos
por resposta certa). Corrija a prova de três alunos de acordo com o gabarito que cada um marcou e
veja qual foi o que teve a maior pontuação na prova
Caso queira concatenar (unir) várias letras em uma variável, basta utilizar o sinal de adição “+”"""

i = 1
acerto = 0
erro = 0
while i <= 5:
    for a in range(1,6):
        gbt = input(f"digite a resposta oficial da questão {a}")
        res = input(f"digite o item do aluno {i} da questão {a}")
        if gbt == res:
            acerto += 1
        else:
            erro += 1
    i += 1
    nota = acerto * 2
    print(f"a nota do aluno{i} foi {nota}")