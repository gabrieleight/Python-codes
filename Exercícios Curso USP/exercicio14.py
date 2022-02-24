"""
Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e 
False se for uma consoante.
"""

def vogal(vogal):
    vogais = ["a", "e", "i", "o", "u"]
    if vogal.lower() in vogais:
        return True
    else:
        return False