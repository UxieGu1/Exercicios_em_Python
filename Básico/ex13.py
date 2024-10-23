# Escreva um módulo com funções para calcular o máximo divisor comum (MDC) e o mínimo
# múltiplo comum (MMC) de dois números. Para o MDC, você deve adaptar o algoritmo de Euclides
# já estudado. No caso do MMC, pode ser usada a fórmula MMC(n1, n2) = n1 * n2 / MDC(n1, n2).
# Implemente também um script com chamadas a essas funções sobre números digitados pelo
# usuário.


def mmc(n1, n2):
    return (n1 * n2) // mdc(n1, n2)


def mdc(n1, n2):
    if n2 == 0:
        return n1
    return mdc(n2, n1 % n2)

def main():
    n1 = int(input('Insira o primeiro número: '))
    n2 = int(input('Insira o segundo número: '))

    print(f'MDC: {mdc(n1, n2)}')
    print(f'MMC: {mmc(n1, n2)}')    

if __name__ == '__main__':
    main()
