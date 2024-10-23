# Implemente um módulo com as funções:
#  ano_bissexto(ano), retorna True se o ano for bissexto e False, em caso negativo;
#  dias_mes(ano, mes): retorna a quantidade de dias do mês, deve usar a função
# ano_bissexto().
# Construa um script que receba uma data do usuário (mês e ano) e mostre o resultado das funções
# implementadas.

def ano_bissexto(ano):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        return True
    return False

def dias_mes(ano, mes):
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        return 31
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return 30
    elif mes == 2 and ano_bissexto(ano):
        return 29
    elif mes == 2 and not ano_bissexto(ano):
        return 28

ano = int(input('Insira o ano: '))
mes = int(input('Insira o mes: '))
print('Bissexto' if ano_bissexto(ano) else 'Não bissexto')
print(f'Quantidade de dias: {dias_mes(ano, mes)}')
