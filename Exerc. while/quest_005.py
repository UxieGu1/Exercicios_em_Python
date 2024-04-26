"""Desenvolva um programa que faça a tabuada de um número qualquer inteiro
que será digitado pelo usuário, mas a tabuada não deve necessariamente
iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados
também pelo usuário, conforme exemplo abaixo:"""

tab = int(input("Montar a tabuada de: "))
com = int(input("Começar por: "))
ter = int(input("Terminar em: "))

print(f"Vou montar a tabuada de {tab} começando em {com} e terminando em {ter}: ")

while com <= ter:
    print(f"{tab} x {com} = {tab*com}")
    com += 1