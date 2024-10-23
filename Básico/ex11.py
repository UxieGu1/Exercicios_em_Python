# Crie a função input_int(mensagem) semelhante à função input(). A função deve receber uma
# mensagem, exibi-la ao usuário e garantir que o número digitado seja válido. Enquanto o usuário
# digitar um número inválido, a função deve informar o erro e solicitar e digitação novamente. Dica:
# utilize a instrução try.

def input_int(mensagem):
    while True:
        try:
            num = int(input(mensagem))
            return num
        except ValueError:
            print('Erro! Digite um número inteiro!')

input_int('Insira um número: ')