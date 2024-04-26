"""[OBI – 2022 - Alterada] João conseguiu contratar um ótimo plano de
Internet para o seu telefone celular. O plano permite que João utilize uma
quota de até X megabytes de dados por mês para navegar na Internet. Se João
não usa toda a sua quota no mês, os megabytes que ele não usou são
adicionados à quota do mês seguinte. Pelo contrato, João nunca pode usar
mais megabytes do que a sua quota corrente.
Por exemplo, se X=200 megabytes e João usou 150 no primeiro mês e 220
megabytes no segundo mês, então no terceiro mês João tem uma quota de 230
megabytes para usar (50 megabytes são transferidos do primeiro para o
segundo mês, 30 megabytes são transferidos do segundo para o terceiro mês).
Nesta tarefa são dados:
• o valor da quota mensal X
• quantos megabytes João usou em cada um dos primeiros 5 meses do
plano.
Você deve determinar quantos megabytes João tem para usar no 6º mês """

# Leitura da quota mensal X
quota_mensal = int(input("Digite o valor da quota mensal (X): "))

# Leitura dos megabytes usados nos primeiros 5 meses
mes1 = int(input("Digite a quantidade de megabytes usados no primeiro mês: "))
mes2 = int(input("Digite a quantidade de megabytes usados no segundo mês: "))
mes3 = int(input("Digite a quantidade de megabytes usados no terceiro mês: "))
mes4 = int(input("Digite a quantidade de megabytes usados no quarto mês: "))
mes5 = int(input("Digite a quantidade de megabytes usados no quinto mês: "))

# Cálculo da quota para o sexto mês
quota_atual = quota_mensal + mes1 + mes2 + mes3 + mes4 + mes5

# Exibição da quota para o sexto mês
print("Quota para o sexto mês:", quota_atual)
