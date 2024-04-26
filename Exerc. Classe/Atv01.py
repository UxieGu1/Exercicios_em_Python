"""Crie uma classe chamada "Pessoa" que possui os atributos nome, idade e profissão. Em
seguida, crie um objeto da classe Pessoa e atribua valores aos seus atributos. Por fim, exiba na
tela as informações da pessoa."""

class Pessoa:
    def __init__(self, nome, idade, pro):
        self.nome = nome
        self.idade = idade
        self.pro = pro

p1 = Pessoa("Guizin", 16, "bodybuilder")
print (p1.nome)
print (p1.idade)
print(p1.pro)