def juros_simples(C, I, T):
    juros = C * (I / 100) * T
    montante = C + juros
    print(f'Juros Simples: {juros}')
    print(f'Montante Simples: {montante}')

def juros_compostos(C, I, T):
    montante = C * (1 + (I / 100)) ** T
    juros_compostos = montante - C
    print(f'Juros Compostos: {round(juros_compostos, 2)}')
    print(f'Montante Compostos: {round(montante, 2)}')

juros_simples(1000, 10, 1)
juros_compostos(6000, 3.5, 12)
