"""Escreva um programa que, dado o valor da venda, imprima a comissao que dever ˜ a ser ´ paga ao
vendedor. Para calcular a comissao, considere a tabela abaixo:"""

valorVenda = int(input("Digite o valor da venda: "))
valorPagar = int
if valorVenda >= 100000:
    valorPagar = 700 + (valorVenda * 0.16)

elif valorVenda  < 100000 and valorVenda >= 80000:
    valorPagar = 650 + (valorVenda * 0.14)

elif valorVenda < 80000 and valorVenda >= 60000:
    valorPagar = 600 + (valorVenda * 0.14)

elif valorVenda < 600000 and valorVenda >= 40000:
    valorPagar = 550 + (valorVenda * 0.14)

elif valorVenda < 400000 and valorVenda >= 20000:
    valorPagar = 500 + (valorVenda * 0.14)

elif valorVenda < 20000:
    valorPagar = 400 + (valorVenda * 0.14)

print("O valor a ser a pago sera: ", valorPagar)