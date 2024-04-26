"""A empresa Tech Tudo percebendo que durante o ano de 2019 o lucro foi muito bom, decidiu
gratificar os funcionários de sua empresa. A ideia tomada foi gratificar os funcionários com um valor
referente a 10% de seus salários. No entanto, o valor da gratificação não pode ultrapassar os 200
reais se o conceito do funcionário for o conceito “B” . Na empresa existem o conceito A e B para os
funcionários. Desenvolva um programa em Python que receba o salário de um funcionário da empresa
e seu conceito, ao final imprima a gratificação recebida e a soma da gratificação com o salário."""

conceito = input("Qual o conceito do funcionário(A e B): ")
salario = int(input("Digte o salário do funcionário: "))
gratificacao = int

if conceito == "A":
    gratificacao = salario * 0.1
    print("O valor da sua gratificação é de R$: ", gratificacao)

elif conceito == "B" and salario <= 2000:
    gratificacao = salario * 0.1
    print("O valor da sua gratificação é de R$: ", gratificacao)