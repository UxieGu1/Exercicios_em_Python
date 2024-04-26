"""Uma empresa, que presta serviço à companhia de energia elétrica do estado, necessita de um
programa que auxilie os seus eletricistas no cálculo das principais grandezas da Eletricidade que
são Tensão, Resistência e Corrente. Sabe-se que:
U=Ri, onde, U é a Tensão (em V), R é a Resistência (em Ώ) e i a Corrente (em A).
Você foi contratado(a) pela empresa para atender a essa solicitação. Construa um programa que apresente o seguinte
menu:
************************************************
CÁLCULO DE GRANDEZAS ELÉTRICAS
************************************************
1. Tensão (em Volt)
2. Resistência (em Ohm)
3. Corrente (em Ampére)
************************************************
Qual grandeza deseja calcular?
Em seguida, o programa deve solicitar que o eletricista informe o valor das outras duas grandezas
para realizar o cálculo. Quando o eletricista escolher:
a. Tensão, o programa deve solicitar que ele informe os valores da Resistência e da Corrente
b. Resistência, o programa deve solicitar que ele informe os valores da Tensão e da Corrente
c. Corrente, o programa deve solicitar que ele informe os valores da Tensão e da Resistência
Por fim, o programa deve calcular e apresentar o valor encontrado para a grandeza escolhida."""

print('************************************************')
print('CÁLCULO DE GRANDEZAS ELÉTRICAS')
print('************************************************')
print('1. Tensão (em Volt)')
print('2. Resistência (em Ohm)')
print('3. Corrente (em Ampére)')
print('************************************************')
print('Qual grandeza deseja calcular? ')

grandeza = input('Informe a grandeza que deseja calcular: ')

if grandeza == 'tensão':
    corrente = int(input('Informe o valor da corrente: '))
    resistence = int(input('Informe o valor da resistence: '))
    tensao = corrente * resistence
    print(tensao)

elif grandeza == 'resistencia':
    tensao = int(input('Informe o valor da tensao: '))
    corrente = int(input('Informe o valor da corrente: '))
    resistence = tensao / corrente
    print(resistence)

elif grandeza == 'corrente':
    tensao = int(input('Informe o valor da tensao: '))
    resistence = int(input('Informe o valor da corrente: '))
    corrente = tensao / resistence
    print(corrente)



