"""As tarifas de certo parque de estacionamento são as seguintes: ˜
• 1a e 2a hora - R$ 1,00 cada
• 3a e 4a hora - R$ 1,40 cada
• 5a hora e seguintes - R$ 2,00 cada
O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste modo, quem
estacionar durante 61 minutos pagará por duas horas, que é o mesmo que pagaria se tivesse
permanecido 120 minutos. Os momentos de chegada ao parque e partida deste são apresentados
na forma de pares de inteiros, representando horas e minutos.
Por exemplo, o par 12 50 representara “dez para a uma da tarde”. Pretende-se criar um programa
que, lidos pelo teclado os momentos de chegada e de partida, escreva na tela o preço cobrado pelo
estacionamento. Admite-se que a chegada e a partida se dão com intervalo não superior a 24 horas.
Portanto, se uma dada hora de chegada for superior a da partida, isso não e uma situação de erro,
antes significar a que a partida ocorreu no dia seguinte ao da chegada"""

hEntrada = int(input("Digite a hora de entrada \n"))
mEntrada = int(input("Digite os minutos de entrada \n"))
hSaida = int(input("Digite a hora de saída \n"))
mSaida = int(input("Digite os minutos de saída \n"))

# cálculo da permanência

if hEntrada > hSaida:
    horaFinal = (hSaida + 24) - hEntrada
else:
    horaFinal = hSaida - hEntrada

if mEntrada > mSaida:
    minutoFinal = (mSaida + 60) - mEntrada
else:
    minutoFinal = mSaida - mEntrada

print(f"A permanência foi de: {horaFinal} horas e {minutoFinal} minutos \n")

# cálculo do valor

tempoMinutos = horaFinal * 60 + minutoFinal

if 1 <= tempoMinutos <= 60:
    preco = 1
    print(f"O valor a ser pago será de R$ {float(preco)}")
elif 60 < tempoMinutos <= 120:
    preco = 2
    print(f"O valor a ser pago será de R$ {float(preco)}")
elif 120 < tempoMinutos <= 180:
    preco = 4.2
    print(f"O valor a ser pago será de R$ {float(preco)}")
elif 180 < tempoMinutos <= 240:
    preco = 5.6
    print(f"O valor a ser pago será de R$ {float(preco)}")
elif tempoMinutos > 240:
    preco = horaFinal * 2
    print(f"O valor a ser pago será de R$ {float(preco)}")
else:
    print(f"Tempo de permanência mínimo, não será necessário pagar!")