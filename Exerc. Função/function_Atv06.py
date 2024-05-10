"""Crie uma função que receba como entrada uma string e retorne “É palíndromo” se a string for
um palíndromo e “Não é palíndromo” caso contrário"""

def palindromo(string):
    string = string.replace(" ", "").lower()
    
    if string == string[::-1]:
        return "É palíndromo"
    else:
        return "Não é palíndromo"


print(palindromo("Ame a ema"))  
print(palindromo("Python"))    
