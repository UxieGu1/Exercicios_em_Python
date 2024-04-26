"""Os professores de Educação Física estão organizando uma seletiva para montar
a equipe de natação. Para isso, eles convocaram os 7 melhores tempos da
última competição e marcaram o tempo de cada um dos nadadores, na prova
dos 25 metros, estilo livre.
Considerando que não houve tempos iguais, construa um programa que leia o
nome e o tempo (em segundos) de cada atleta e, em seguida, gere o seguinte
relatório:
a. nome do nadador com o melhor tempo
b. nome do nadador com o pior desempenho
c. tempo médio dos nadadores e
d. quantidade de atletas com o tempo entre 12s e 15s"""


melhor_tempo = float('inf')
pior_tempo = float('-inf')
soma_tempos = 0
quantidade_atletas = 0
quantidade_tempo_entre_12_e_15 = 0


contador = 1
while contador <= 7:
    nome = input(f"Digite o nome do nadador {contador}: ")
    tempo = float(input(f"Digite o tempo em segundos do nadador {contador}: "))


    if tempo < melhor_tempo:
        melhor_tempo = tempo
        nadador_melhor_tempo = nome

    if tempo > pior_tempo:
        pior_tempo = tempo
        nadador_pior_tempo = nome

    soma_tempos += tempo
    quantidade_atletas += 1

    if tempo >= 12 and tempo <= 15:
        quantidade_tempo_entre_12_e_15 += 1

    contador += 1

tempo_medio = soma_tempos / quantidade_atletas

print("Relatório:")
print("Melhor tempo:", nadador_melhor_tempo)
print("Pior desempenho:", nadador_pior_tempo)
print("Tempo médio dos nadadores:", tempo_medio)
print("Quantidade de atletas com tempo entre 12s e 15s:", quantidade_tempo_entre_12_e_15)
