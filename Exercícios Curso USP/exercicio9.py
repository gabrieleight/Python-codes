# Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais.
# Para a saída, siga o formato do exemplo abaixo

n = int(input("Digite o valor de n: "))
cont1 = 1
cont2 = 1

while True:
    if cont2 % 2 != 0:
        print(cont2)
        cont1 = cont1 + 1 
    cont2 = cont2 + 1
    if cont1 > n:
        break   