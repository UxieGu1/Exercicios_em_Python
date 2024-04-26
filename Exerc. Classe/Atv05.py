"""Crie uma classe chamada "Animal" que possui os atributos nome e idade. Implemente um
método para exibir o som do animal. Em seguida, crie objetos das classes "Cachorro", "Gato" e
"Pato", que herdam da classe Animal, e implemente o método de exibir o som para cada um
deles."""

class Animal:
    def __init__(self, n, i):
        self.nome = n
        self.idade = i

    def somCachorro(self):
        print("AU AU")
    def somGato(self):
        print("MIAU")
    def somPato(self):
        print("QUÁ QUÁ")

animal1 = Animal("Chico", 4)
animal1.somCachorro()

animal2 = Animal("nina", 8)
animal2.somGato()

animal2 = Animal("teia", 3)
animal2.somPato()