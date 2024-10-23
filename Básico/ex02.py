# Escreva um código que receba um número de segundos e converta este número em
# horas, minutos e segundos. Escreva também um código que faça o contrário.

segundos = int(input('Insira o número de segundos: '))

horas = segundos // 3600
segundos = segundos % 3600
minutos = segundos // 60
segundos = segundos % 60

print(f'{horas}:{minutos}:{segundos}')
