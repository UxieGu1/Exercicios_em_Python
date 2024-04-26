"""Crie um programa no qual o usuário informe a idade de um número
indeterminado de alunos. Para encerrar a leitura dos dados, o usuário deve
informar uma idade negativa. No final, o programa deve mostrar a média
aritmética entre a maior e a menor idade."""


menorIdade = 100
maiorIdade = 0
idadeAlunos = int(input("Digite a idade de um aluno: "))
print("para terminar o progama digite um numero negativo")

while idadeAlunos > 0:
    if idadeAlunos < menorIdade:
        menorIdade = idadeAlunos

    elif idadeAlunos > maiorIdade:
        maiorIdade = idadeAlunos

    idadeAlunos = int(input("Digite a idade de um aluno: "))
print(" A média da maior idade para a menor é de: ", maiorIdade / menorIdade)
