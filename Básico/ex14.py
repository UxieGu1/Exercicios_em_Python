# Criar uma função para resolver equações de segundo grau retornando as raízes dentro de uma
# tupla. Crie também um função principal para receber os termos A, B e C da equação e mostrar o
# resultado para o usuário.


def equation(a, b, c):
    delta = (b ** 2) - 4 * a * c
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)
    return (x1, x2)

def main():
    a = float(input('Insira o valor de A: '))
    b = float(input('Insira o valor de B: '))
    c = float(input('Insira o valor de C: '))
    raizes = equation(a, b, c)
    if len(raizes) == 0:
        print('Esta equação não possui raízes')
    elif len(raizes) == 1:
        print(f'A raíz desta equação é: {raizes[0]}')
    else:
        print(f'As raízes da equação são ', end='')
        print('x1 = {0:.2f} e x2 = {1:.2f}'.format(raizes[0], raizes[1]))

if __name__ == '__main__':
    main()