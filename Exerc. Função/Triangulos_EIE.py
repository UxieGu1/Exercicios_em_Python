"""Escreva uma função que recebes 3 valores reais X, Y e Z e que verifique se esses valores
podem ser os comprimentos dos lados de um triângulo Crie outra função que retorne qual é o
tipo de triângulo formado
Para que X, Y e Z formem um triângulo é necessário que a seguinte propriedade seja satisfeita
o comprimento de cada lado de um triângulo é menor do que a soma do comprimento dos
outros dois lados O procedimento deve identificar o tipo de triângulo formado observando as
seguintes definições
Triângulo Equilátero: os comprimentos dos 3 lados são iguais
Triângulo Isósceles: os comprimentos de 2 lados são iguais
Triângulo Escaleno: os comprimentos dos 3 lados são diferentes"""

def validarTriangulo(l1,l2,l3):
    if l1 + l2 > l3 and l2 +l3 >l1 and l1 + l3 > l2:
        print("Triângulo válido")
        return True

    else:
        print("Triângulo inválido")
        return False
def tipoTriangulo(l1,l2,l3):
    if l1 == l2 and l2 == l3: #testanto se os lados são iguais
        print("Triângulo Equilátero")

    elif not (l1 == l2) and not (l2 == l3) and not (l1 == l3): #testando se os lados são diferentes
        print("Triângulo Escaleno")

    else:
        print("Triângulo Isósceles")

lado1 = int(input("Digite o lado 1 do triângulo: "))
lado2 = int(input("Digite o lado 2 do triângulo:"))
lado3 = int(input("Digite o lado 3 do triângulo: "))

verificar = validarTriangulo(lado1,lado2,lado3)

if verificar : #Caso tenha retornado VERDADEIRO(True), indica qual é o tipo do triângulo
    tipoTriangulo(lado1,lado2,lado3)
