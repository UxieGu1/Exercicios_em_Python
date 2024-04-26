"""As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem
compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule
e escreva o custo total da compra."""


maca = int(input("digite a quantidade de maças compradas: "))

if maca < 12:
    maca = maca * 1.30

elif maca >= 12:
    maca = maca * 1.00

print("O preço das maças será", maca)
