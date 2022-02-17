"""
Programa que calcula um número binomial (ou coeficiente binomial) de dois números inteiros N e K
"""

def fatorial(x):
    for i in range(1, x):
        x = x*i
    return x

def fatorial_metodo_dois(x):
    # Outro método mais fácil de calcular o fatorial de um número!
    contador = x
    while True:
        x = x * (contador - 1)
        contador -= 1
        if contador == 1:
            break
    return x

def coeficiente_binomial(n, k):
    coeficiente = fatorial(n)/(fatorial(k)*fatorial(n-k))
    return coeficiente

def main():
    n = int(input("Digite um número inteiro N: "))
    k = int(input("Digite um número inteiro K: "))
    numero = coeficiente_binomial(n, k)
    
    print(f"O resultado é {numero:.0f}")
    
if __name__ == "__main__":
    main()