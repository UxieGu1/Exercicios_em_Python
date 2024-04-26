"""Crie uma classe chamada "ContaBancária" que possui os atributos número da conta e saldo.
Implemente métodos para depositar e sacar dinheiro da conta. O método sacar deverá analisar
se será possível sacar o valor requisitado. Em seguida, crie um objeto da classe ContaBancária
e realize algumas operações de depósito e saque."""

class ContaBancaria:
    def __init__(self, Nconta, saldo):
        self.Nconta=Nconta
        self.saldo=saldo

    def depositar(self, d):
        self.saldo += d


    def sacar(self,valor):
        saldo_atual=self.saldo-valor
        if saldo_atual>=0:
            print("Saque realizado com sucesso! Seu saldo atual é de:", saldo_atual )

        else:
            print("Não foi possível realizar o saque")

op= ContaBancaria(1200, 2000)
op.depositar(200)
op.sacar(400)
