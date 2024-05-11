"""Uma loja de roupa resolveu fazer uma promoção onde o cliente vai falar uma frase. De acordo
com a frase citada, ganhará um desconto em sua compra. Faça uma função que receba uma
frase e conte quantas vogais “a” ela possui. O programa deverá retornar o valor encontrado e
esse será o desconto que o cliente ganhará. Em seguida faça outra função que receba o valor
de desconto e o preço da compra e em seguida imprima o valor descontado e o novo preço
que será pago
"""
def contarVogal(string):
    vogal_a = 'a'       
    cont = 0
    for letra in string: 
        if letra.lower() == vogal_a:
            cont += 1
    return cont
    print(f'O total de letras "a" é {cont}')

def desconto(valorOriginal, percDesconto):
    valorDesconto = valorOriginal * (percDesconto / 100)
    valorFinal = valorOriginal - valorDesconto
    print(f'O desconto será de {valorOriginal - valorFinal}' )
    return valorFinal

frase = input('Digite sua frase: ').lower()
resultado = contarVogal(frase)
print(f'O total de letras "a" na frase é {resultado}')

valor = int(input('Digite o valor original da compra: '))
desconto(valor, resultado)
