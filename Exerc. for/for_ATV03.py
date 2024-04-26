"""A função len() em Python tem ela tem por objetivo retornar o comprimento do item inserido, o
retorno dela sempre vai ser algum número, ou um erro caso sua sintaxe esteja errada.
Analise o código a seguir
 No exemplo, o texto “Uma casa linda” possui 12 letras e 2 espaços, totalizando 14 caracteres.
É possível acessar letra por letra de um texto a partir do seu índice. Por exemplo:
Com isso, faça um programa usando um for e os conceitos mostrado anteriormente para pedir ao
usuário que escreva uma frase e depois mostre:
a) Quantas vogais, quantas consoantes e quantos espaços o texto tem?
b) Escreva a frase ao contrário
c) Imprimir a frase novamente mas onde tiver vogal “a” , “i” e “u” colocar um “–“, e onde tiver as
vogais “e” e “o” colocar um “@”"""


frase = input("Digite uma frase: ")

# Inicializando as variáveis de contagem
vogais = 0
consoantes = 0
espacos = 0

# Contagem de vogais, consoantes e espaços
for letra in frase:
    if letra.lower() in 'aeiou':
        vogais += 1
    elif letra.isalpha():
        consoantes += 1
    elif letra.isspace():
        espacos += 1

# Impressão das contagens
print("Quantidade de vogais:", vogais)
print("Quantidade de consoantes:", consoantes)
print("Quantidade de espaços:", espacos)

# Impressão da frase ao contrário
print("Frase ao contrário:", frase[::-1])

# Impressão da frase com substituição de vogais
nova_frase = ""
for letra in frase:
    if letra.lower() in 'aiu':
        nova_frase += "-"
    elif letra.lower() in 'eo':
        nova_frase += "@"
    else:
        nova_frase += letra

print("Frase com substituição de vogais:", nova_frase)

