# Desenvolva a classe Ponto que possui os valores de sua posição no eixo X e eixo Y, adicione o método
# calcularDistancia(), que receba um outro ponto como argumento e calcule a distância euclidiana entre
# eles.
# Considerando dois pontos (P e Q), a distância euclidiana é calculada pela fórmula:

# Crie o programa de teste, crie alguns pontos e calcule a distância entre eles.

import math
class Ponto:
    def __init__(self, eixo_x, eixo_y):
        self.eixo_x = eixo_x
        self.eixo_y = eixo_y
        
    def calcular_distancia(self, outro_ponto):
        dx = self.eixo_x - outro_ponto.eixo_x
        dy = self.eixo_y - outro_ponto.eixo_y
        
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        return distancia
    
ponto1 = Ponto(2, 6) #VALORES ALEATÓRIOS
ponto2 = Ponto(4, 5) #VALORES ALEATÓRIOS
distancia = ponto1.calcular_distancia(ponto2)
print(f'A distância entre os pontos é {distancia}')
