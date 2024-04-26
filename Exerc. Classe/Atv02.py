"""Crie uma classe chamada "Círculo" que possui o atributo raio. Implemente métodos para calcular
a área e o perímetro do círculo. Em seguida, crie um objeto da classe Círculo e teste os métodos
implementados."""



class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def Area(self):
       area = 3.14 * self.raio**2 #pi vezes o raio elevado ao quadrado  (A = π r²)
       print(area)
    def Perimetro(self):
        peri = 2 * 3.14 * self.raio #C = 2 * π * r, onde: C = comprimento da circunferência ou perímetro
        print(peri)


Raio1 = float(input("Digite o valor do raio: "))
Comprimento = float(input('Digite o comprimento do circulo: '))

R1 = Circulo(Raio1)
R1.Area()

P1 = Circulo(Comprimento)
P1.Perimetro()