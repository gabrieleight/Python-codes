"""
Escreva a função soma_elementos que recebe como parâmetro uma lista com números inteiros e 
devolve um número inteiro correspondente à soma dos elementos da lista recebida.
"""

def soma_elementos(lista):
    soma = 0
    for i in lista:
        soma = soma + i
    return soma