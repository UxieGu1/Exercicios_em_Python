"""Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros
formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e
custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o
imposto sobre venda"""

def somaImposto(taxaImposto, custo ):
    resultado_imoposto = custo + (custo * taxaImposto / 100)
    return resultado_imoposto

somaImposto(20, 120.00)
