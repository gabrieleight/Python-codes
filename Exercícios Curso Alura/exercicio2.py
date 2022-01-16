# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

numeroDaTabuada = int(input("Digite qual a tabuada de multiplicar que vc quer: "))

print("-" * 12)
for i in range(1, 11):
    print(f"{numeroDaTabuada} x {i:2} = {numeroDaTabuada * i:2}")
print("-" * 12)
