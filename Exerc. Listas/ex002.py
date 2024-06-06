#02.Uma turma de formandos está vendendo rifas para angariar recursos financeiros para sua 
#cerimônia de formatura. Construa um programa para cadastrar os nomes das pessoas que 
#compraram a rifa. Ao fim, o programa deve sortear o ganhador do prêmio e imprimir o seu nome.
import random as rd

compradores = []
for i in range(5):
  alunos = str(input(f'Digite o nome dos alunos que compraram a rifa: '))
  compradores.append(alunos)

sorteado = rd.choice(compradores)
print(f'O ganhador da rifa é o(a) {sorteado}')
