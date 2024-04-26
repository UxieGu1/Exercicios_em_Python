"""Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcula r e
escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for
maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo
Negativo'."""
conta = int(input('Informe o número da conta: '))
saldo = int(input('Informe o saldo da conta: '))
debito = int(input('Informe o debito da conta: '))
credito = int(input('Informe o credito da conta: '))

saldoAtual = (saldo - debito) + credito

if saldoAtual >= 0:
    print('Saldo Positivo')

else:
    print('Saldo Negativo')
