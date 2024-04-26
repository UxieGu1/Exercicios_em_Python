"""Implemente uma classe chamada Carro com as seguintes propriedades:
•Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de
combustível no tanque.
•O consumo é especificado no construtor e o nível de combustível inicial é 0.
•Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de
combustível no tanque de gasolina. Esse método recebe como parâmetro a distância em km.
•Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
•Forneça um método adicionarGasolina( ), para abastecer o tanque.
•Faça um programa para testar a classe Carro."""

class carro:
    def __init__(self, kmL, Ct):
        self.kmL = kmL
        self.Ct = Ct

    def andar (self, dist):
        self.Ct = self.kmL * dist
        print("Km ", dist)

    def obterGasolina (self):
        print("Quantidade de gasolina no tanque: ",self.Ct)

    def adicionarGasolina (self, add):
        self.Ct += add
        print("Adicionou ", add , " litros de gasolina no tanque")

carro1 = carro(12, 0)
carro1.adicionarGasolina(100)
carro1.andar(5)