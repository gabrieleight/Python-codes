"""
Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior
número primo menor ou igual ao número passado à função
"""

def éPrimo(k):
    contador = 0
    for i in range(k, 0, -1):
        if k % i == 0:
            contador += 1
    if contador == 2:
        return True
    else:
        return False
        
        
def maior_primo(numero):
    for i in range(1, numero+1):
        if éPrimo(i) == True:
            maior_primo = i
    return maior_primo