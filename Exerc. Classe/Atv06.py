"""Implemente uma classe Aluno, que deve ter os seguintes atributos: nome, curso, tempoSemDormir (em horas).
Essa classe deverá ter os seguintes métodos:
– estudar (que recebe como parâmetro a qtd de horas de estudo e acrescenta tempoSemDormir )
– Dormir (que recebe como parâmetro a qtd de horas de sono e reduz tempoSemDormir )
Crie um código de teste da classe, criando um objeto da classe aluno e usando os métodos estudar e dormir. Ao
final imprima quanto tempo o aluno está sem dormir"""

class Aluno:
    def __init__(self, nome, curso, tempoSemDormir):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempoSemDormir


    def estudar(self, qtdH):
        self.tempoSemDormir += qtdH


    def dormir(self, qtdH):
        self.tempoSemDormir -= qtdH


al = Aluno("Riquelme", "Informática", 10)
al.estudar(5)
print(f"{al.nome} está a {al.tempoSemDormir} horas sem dormir")
al.dormir(10)
print(f"{al.nome} está a {al.tempoSemDormir} horas sem dormir")