"""Crie um programa, escrito na linguagem Python, que indique o nome da função exercida por um
funcionário, cujo código é informado pelo usuário (10 - Técnico, 15 - Analista, 20- Supervisor, 25 -
Gerente). Caso o código da função seja válido (maior que 0), mas não esteja entre estes, deverá
ser informado ao usuário: “Código não corresponde a uma função válida”"""

funcao = int(input('Informe o código de sua função exercida: '))

if funcao == 10:
    print('Técnico')

elif funcao == 15:
    print('Analista')

elif funcao == 20:
    print('Supervisor')

elif funcao == 25:
    print('Gerente')

else:
    print("Código inválido")