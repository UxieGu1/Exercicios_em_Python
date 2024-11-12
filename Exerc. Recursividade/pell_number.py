# Os números de Pell são definidos pela seguinte recursão
# Exemplo de números desta sequência são: 0, 1, 2, 5, 12, 29, 70, 169, 408, 985...
# Implemente um método recursivo que receba como entrada um número N e retorne o Nésimo número de Pell


def pell(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 2 * pell(n - 1) + pell(n - 2)
    

n = int(input('Insira um número: '))
print(pell(n))
