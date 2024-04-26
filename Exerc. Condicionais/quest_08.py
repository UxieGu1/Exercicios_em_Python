"""Suponha que o professor Fábio possui 2 logins na rede acadêmica da instituição. Construa um
programa que valide o acesso do professor à rede. Caso o par usuário/senha informado esteja
correto, o programa deve imprimir a mensagem “Seja bem vindo!”. Caso contrário, “Usuário e senha
não conferem”.
 Login 1            login 2
usuário: procopio   usuário: paiva
senha: 12345        senha: 54321"""

login = int(input("digite seu login: "))
usuario = input
senha = int

if login == "1":
    usuario = input("digite o seu usuario:" )
    if usuario == "procopio":
        senha = int(input("digite sua senha"))
        if senha == "12345":
            print("Seja bem-vindo!")

elif login == "2":
    usuario = input("digite o seu usuario:" )
    if usuario == "paiva":
        senha = int(input("digite sua senha"))
        if senha == "54321":
            print("Seja bem-vindo!")