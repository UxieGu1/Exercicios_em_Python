"""Os números primos possuem várias aplicações dentro da Computação, por exemplo na
Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um
programa que peça um número inteiro e determine se ele é ou não um número primo."""


numero = int(input("Digite um número inteiro: "))

if numero < 2:
    primo = False
else:
    primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            primo = False
            break


if primo:
    print(numero, "é um número primo.")
else:
    print(numero, "não é um número primo.")
