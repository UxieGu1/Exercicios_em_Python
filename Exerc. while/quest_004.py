"""Numa eleição para o grêmio estudantil existem duas chapas (Chapa A e Chapa
B). A maioria dos alunos já tinham votado e o sistema aferiu que a eleição
estava empatada, no entanto ainda faltavam 9 alunos para votar. Faça um
programa que receba esses 8 novos restantes e ao final mostre a chapa
vencedora e a diferença de votos do vencedor """

# Inicialização das variáveis
chapa_a = 0
chapa_b = 0
votos_restantes = 9

while votos_restantes > 0:
    voto = int(input("Digite o número correspondente à chapa escolhida (1 para Chapa A, 2 para Chapa B): "))

    if voto == 1:
        chapa_a += 1
    elif voto == 2:
        chapa_b += 1
    else:
        print("Voto inválido. Digite apenas 1 para Chapa A ou 2 para Chapa B.")
        continue

    votos_restantes -= 1


if chapa_a > chapa_b:
    vencedora = "Chapa A"
    diferenca = chapa_a - chapa_b

elif chapa_b > chapa_a:
    vencedora = "Chapa B"
    diferenca = chapa_b - chapa_a

else:
    vencedora = "Empate"
    diferenca = 0

print("Resultado:")
print("Chapa A:", chapa_a)
print("Chapa B:", chapa_b)
print("Chapa vencedora:", vencedora)
print("Diferença de votos:", diferenca)
