# Simular uma calculadora simples. O código deve solicitar ao usuário a operação desejada (soma,
# multiplicação, divisão, subtração ou potência) ou então sair. Quando o usuário escolher uma
# operação, o código deve solicitar dois números, realizar a operação sobre estes números e exibir o
# resultado. O código deve sempre solicitar uma nova operação até que o usuário escolha sair.

while True:
    op = input('Insira a operação desejada: ')
    if op == 'sair':
        break
    num1 = float(input('Insira o primeiro número: '))
    num2 = float(input('Insira o segundo número: '))

    if op == 'soma':
        print(num1 + num2)
    elif op == 'multiplicação':
        print(num1 * num2)
    elif op == 'divisão':
        print(num1 / num2)
    elif op == 'subtração':
        print(num1 - num2)
    elif op == 'potência':
        print(num1 ** num2)