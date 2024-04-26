"""Numa eleição existem três candidatos (candidato A, candidato B e candidato C). Faça um
programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o
número de votos de cada candidato"""

eleitoresN = int(input('O número total de eleitores é: '))
cA = 0
cB = 0
cC = 0
for i in range(eleitoresN):
    voto = input('escolha qual candidato voce irá votar(candidato A, candidato B e candidato C: ').upper()
    if voto == "A":
        cA += 1
    elif voto == "B":
        cB += 1
    elif voto == "C":
        cC += 1
    else:
        print('Candidato inválido!')
        break

print(f'O total de votos do candidato A é {cA}')
print(f'O total de votos do candidato B é {cB}')
print(f'O total de votos do candidato C é {cC}')