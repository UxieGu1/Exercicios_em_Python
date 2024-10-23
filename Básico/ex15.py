# Construir um script capaz de calcular a velocidade média de uma viagem a partir das velocidades
# de cada trecho. O usuário deve informar o número de trechos e, em seguida, informar a distância e
# velocidade de cada trecho. O cálculo da velocidade média é feito somando o produto da distância
# pela velocidade de cada trecho e dividindo essa soma pela soma das distâncias. Após o cálculo da
# velocidade média, o programa deve os trechos com velocidade acima da média.


def main():
    num_trechos = int(input('Insira o número de trechos: '))
    for i in range(num_trechos):
        distancia = float(input('Insira a distância: '))
        velocidade = float(input('Insira a velocidade: '))
        velocidade_med = (distancia * velocidade) / (distancia + velocidade)
        if velocidade_med > velocidade:
            print(f'Velocidade acima da média: {velocidade_med:.2f}')
        else:
            print(f'Velocidade abaixo da média: {velocidade_med:.2f}')


if __name__ == '__main__':
    main()


