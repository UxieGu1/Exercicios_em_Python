# Calcular o imposto de renda de um salário considerando as seguintes alíquotas:
#  Até R$ 1.903,98: isento;
#  De R$ 1.903,99 até R$ 2.826,65: 7,5%;
#  De R$ 2.826,66 até R$ 3.751,05: 15%;
#  De R$ 3.751,06 até R$ 4.664,68: 22,5%;
#  Acima de R$ 4.664,68: 27,5%.

salario = float(input('Insira o salario: '))

if salario <= 1903.98:
    print('Isento')
    
elif 1903.99 <= salario <= 2826.65:
    print(f'{salario * 0.075:.2f}')

elif 2826.66 <= salario <= 3751.05:
    print(f'{salario * 0.15:.2f}')

elif 3751.06 <= salario <= 4664.68:
    print(f'{salario * 0.225:.2f}')

else:
    print(f'{salario * 0.275:.2f}')