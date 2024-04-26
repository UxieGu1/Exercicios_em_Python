"""Crie um programa no qual o usuário informe o código do cargo de um
funcionário (ver tabela abaixo) e o seu respectivo salário. Para encerrar a
leitura dos dados, defina uma condição de parada (por exemplo, código do
cargo igual a zero). Ao fim, o programa deve informar a média salarial dos
nutricionistas."""

i = 0
media = 0
while i < 3:
    code = int(input('informe o código do cargo de funcionario: '))
    sal = int(input('Informe seu salário: '))
    media += sal

    if code == 1:
        print('Enfermeiro')

    elif code == 2:
        print('Nutricionista')

    elif code == 3:
        print('Médico')

    elif code == 0 or sal == 0:
        media /= 3
        print(f'a média salarial é {media}')
