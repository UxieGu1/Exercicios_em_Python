"""O Sra. Ana Mary possui uma grande loja de doces, onde o produto mais vendido são suas trufas.
Para agilizar o cálculo de quanto cada cliente deve pagar pelas trufas, ela desenvolveu uma tabela
que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a
atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de
preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que
conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
o Lojas Doces Mary - Tabela de preços
o 1 - R$ 2.49
o 2 - R$ 4.98
o ...
o 50 - R$ 124.50"""

print("o Lojas Doces Mary - tabela de preços")
valor = 2.49
for i in range(1, 51):
     total = valor * i
     print(f"o {i} - R$ {total:.2f}")
