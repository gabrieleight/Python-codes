"""
Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem
na borda do retângulo sejam espaços
"""

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
larg = largura
alt = altura

while altura > 0:
    if larg > 0:
        if largura == larg or altura == 1:
            print("#" * largura)
        else:
            print("#" + (" " * (largura - 2)) + "#")
    larg = larg - 1
    altura = altura - 1