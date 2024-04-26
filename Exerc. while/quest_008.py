"""Escreva um programa que calcule o preço a pagar pelo fornecimento de energia
elétrica de três estabelecimentos. Pergunte a quantidade de kWh consumida e
o tipo de instalação: R para residências, I para indústrias e C para comércios.
Calcule o preço a pagar de acordo com a tabela a seguir.
Ao final indique qual estabelecimento foi o mais econômico"""

i = 0
precoP = 0
while i < 3:
    kWh = int(input('Digite a quantidade de kWh consumida: '))
    inst = input('informe o tipo de instalação(R para residências, I para indústrias e C para comércios): ').upper()
    i += 1

    if kWh <= 500 and inst == "R":
        preco = kWh * 0.40

    elif kWh > 500 and inst == "R":
        preco = kWh * 0.65

    elif kWh <= 1000 and inst == "C":
        preco = kWh * 0.55

    elif kWh > 1000 and inst == "C":
        preco = kWh * 0.60

    elif kWh <= 5000 and inst == "I":
        precoP = kWh * 0.55

    elif kWh > 5000 and inst == "I":
        preco = kWh * 0.60

precoP += preco
print(f'O valor a pagar será R${precoP}')