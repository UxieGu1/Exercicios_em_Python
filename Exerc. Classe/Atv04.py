"""Crie uma classe chamada "Produto" que possui os seguintes atributos:
Nome do produto
Preço do produto
Quantidade em estoque do produto
A classe "Produto" deve ter os seguintes métodos:
Um método para adicionar unidades do produto ao estoque.
Um método para remover unidades do produto do estoque.
Um método para exibir todas as informações do produto.
Crie um objeto da classe "Produto" e teste todos os métodos implementados."""

class Produto:
    def __init__(self, nomeP, PrecoP, qtdP):
        self.nomeProduto = nomeP
        self.PrecoProduto = PrecoP
        self.QuantidadeEstoque = qtdP

    def AdicionarEstoque(self):
        self.QuantidadeEstoque += high

    def RemoverEstoque(self):
        self.QuantidadeEstoque -= low

    def DadosProduct(self):
        print('Nome do produto é: ', P1.self.nomeProduto)
        print('Preço do produto: ', self.PrecoProduto)
        print('Quantidade de estoque do produto: ', self.QuantidadeEstoque)


high = int(input('Digite a quantidade de produtos a mais: '))
aumento = Produto(high)
aumento.AdicionarEstoque()

low = int(input('Digite a quantidade de produtos a menos: '))
decremento = Produto(low)
decremento.RemoverEstoque()

P1 = Produto('Coca-cola', 10, 1200)
print(P1.nomeProduto)
print(P1.PrecoProduto)
print(P1.QuantidadeEstoque)