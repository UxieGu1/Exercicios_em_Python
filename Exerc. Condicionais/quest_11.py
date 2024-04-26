"""Leia uma data de nascimento de uma pessoa fornecida através de três números inteiros: ´ Dia, Mes
e Ano. Teste a validade desta data para saber se esta é uma data válida. Teste se o dia fornecido
e um dia válido: dia > 0, dia ≤ 28 para o mês de fevereiro (29 se o ano for bissexto), dia ≤ 30 em
abril, junho, setembro e novembro, dia ≤ 31 nos outros meses. Teste a validade do mês: mês > 0 e
mês < 13. Teste a validade do ano: ano ≤ ano atual (use uma constante definida com o valor igual
a 2023). Imprimir: “data válida” ou “data inválida” no final da execução do programa."""

dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

valida = False
# Meses com 31 dias
if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or \
    mes == 8 or mes == 10 or mes == 12):
    if (dia <= 31):
        valida = True
# Meses com 30 dias
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    if (dia <= 30):
        valida = True
elif mes == 2:
    # Testa se é bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        if (dia <= 29):
            valida = True
    elif (dia <= 28):
        valida = True

if (valida):
    print("Data válida")
else:
    print("Inválida")
