#01.Desenvolva um programa que pede 6 números para o usuário digitar para que sejam inseridas 
#em uma lista. Sem seguida exclua o segundo e o quinto número. Ao final, faça a média aritmética 
#com os números que sobraram e imprima a lista.

lista_numeros = []
for i in range(6):
  numeros = float(input(f'Digite o {i + 1}° número: '))
  lista_numeros.append(numeros)

lista_numeros.pop(1)
lista_numeros.pop(4)
media = sum(lista_numeros) / len(lista_numeros)
print(f'A média final da lista é {media}')
