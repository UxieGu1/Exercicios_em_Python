"""Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade
de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
(use um while para impedir que a turma tenha mais de 40 alunos)"""

turma = int(input("quantidade de turmas:"))
aluno = 0
total = 0
for t in range(turma):
    numAlu = int(input("digite a quantidade de alunos:"))

    while numAlu > 40:
        numAlu = int(input("digite novamente a quantidade de alunos: "))
    total += numAlu

print(f"A media é {numAlu / turma}")