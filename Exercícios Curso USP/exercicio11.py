"""
Programa que calcula um número binomial (ou coeficiente binomial) de dois números inteiros N e K
"""

def fatorial(x):
    for i in range(1, x):
        x = x*i
    if x == 0:
        x = 1
    return x

def fatorial_metodo_dois(x):
    # Outro método mais fácil de calcular o fatorial de um número!
    contador = x
    while True:
        if contador == 0:
            x = 1
            break
        x = x * (contador - 1)
        contador -= 1
        if contador == 1:
            break
    return x

def fatorial_metodo_três(x):
    # Outro método ainda mais fácil de calcular um fatorial de um número!
    fat = 1
    while x > 1:
        fat = fat * x
        x -= 1
    return fat

def coeficiente_binomial(n, k):
    coeficiente = 0
    if fatorial(k)*fatorial(n-k) > 0:
        coeficiente = fatorial(n)/(fatorial(k)*fatorial(n-k))
    else:
        print(f"Não é possível calcular o coeficiente binomial para esse valores!")
    return coeficiente

def main():
    n = int(input("Digite um número inteiro N: "))
    k = int(input("Digite um número inteiro K: "))
    numero = coeficiente_binomial(n, k)
    
    print(f"O resultado é {numero:.0f}")
    
if __name__ == "__main__":
    main()