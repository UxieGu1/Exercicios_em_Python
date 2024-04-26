"""[OBI -2022] A prefeitura contratou um novo professor para ensinar as crianças
do bairro a jogar tênis na quadra de tênis do parque municipal. O professor
convidou todas as crianças do bairro interessadas em aprender a jogar tênis.
Ao final do primeiro mês de aulas e treinamentos foi organizado um torneio
em que cada participante disputou exatamente seis jogos. O professor vai usar
o desempenho no torneio para separar as crianças em três grupos, de forma a
ter grupos de treino em que os participantes tenham habilidades mais ou
menos iguais, usando o seguinte critério:
• participantes que venceram 5 ou 6 jogos serão colocados no Grupo 1;
• participantes que venceram 3 ou 4 jogos serão colocados no Grupo 2;
• participantes que venceram 1 ou 2 jogos serão colocados no Grupo 3;
Os participantes que não venceram nenhum jogo não serão convidados a
continuar com os treinamentos. Dada uma lista com o resultado dos jogos de
um participante, escreva um programa para determinar em qual grupo ele será
colocado.
A entrada consiste de seis linhas, cada linha indicando o resultado de um jogo
do participante. Cada linha contém um único caractere: V se o participante
venceu o jogo, ou P se o jogador perdeu o jogo. Não há empates nos jogos.
Informe qual grupo o participante irá entrar"""


jogo1 = input("Resultado do jogo 1 (V/P): ")
jogo2 = input("Resultado do jogo 2 (V/P): ")
jogo3 = input("Resultado do jogo 3 (V/P): ")
jogo4 = input("Resultado do jogo 4 (V/P): ")
jogo5 = input("Resultado do jogo 5 (V/P): ")
jogo6 = input("Resultado do jogo 6 (V/P): ")


contador_vitorias = 0

if jogo1 == "V":
    contador_vitorias += 1
if jogo2 == "V":
    contador_vitorias += 1
if jogo3 == "V":
    contador_vitorias += 1
if jogo4 == "V":
    contador_vitorias += 1
if jogo5 == "V":
    contador_vitorias += 1
if jogo6 == "V":
    contador_vitorias += 1

if contador_vitorias >= 5:
    grupo = 1
elif contador_vitorias >= 3:
    grupo = 2
elif contador_vitorias >= 1:
    grupo = 3
else:
    grupo = "Não convidado para continuar com os treinamentos"

print("Grupo:", grupo)
