import time

def contagem(n):
    if n == 1:
        print(n)
    else:
        print(n)
        time.sleep(2)
        print(contagem(n - 1))
        
contagem(10)
