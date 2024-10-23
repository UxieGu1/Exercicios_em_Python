# Escrever um código para receber uma lista de números. Percorrer a lista e utilizar um dicionário
# para sumarizar a quantidade de vezes que cada número aparece na lista.

numbers = []

while True:
    number = int(input('Insira um número(0 para parar): '))
    if number == 0:
        break
    numbers.append(number)

dic_num = {}
for number in numbers:
    if number in dic_num:
        dic_num[number] += 1
    else:
        dic_num[number] = 1

print(dic_num)