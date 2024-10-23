# Leia uma quantidade indeterminada de números. A cada número informado, o usuário deve
# informar se deseja continuar ou parar. Ao final, o código deve retornar o maior e o menor número
# recebido.

maior = int(input('Insira um número: '))
menor = int(input('Insira um número: '))

while True:
    num = int(input('Insira um número: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    resp = input('Deseja continuar? [S/N] ').upper()
    if resp == 'N':
        break
print(f'Maior: {maior}, Menor: {menor}')