# Calcule o fatorial de um número. O fatorial de um número n, representado por n!, é calculado como
# n! = n × (n − 1) × ... × 2 × 1. Sendo que 1! = 0! = 1.

num = int(input('Insira um número: '))

fatorial = 1
while num > 1:
    fatorial *= num
    num -= 1
    
print(fatorial)