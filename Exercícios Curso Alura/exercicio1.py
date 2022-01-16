# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

numeroMetros = float(input("Digite um valor em metros (m):\n"))

### Múltiplos do metro
numeroQuilometros = numeroMetros / 1000
numeroHectometros = numeroMetros / 100
numeroDecametros = numeroMetros / 10

### Submúltiplos do metro
numeroDecimetros = numeroMetros * 10
numeroCentimetros = numeroMetros * 100
numeroMilimetros = numeroMetros * 1000

print()
print("*" * 100)
print(f"O valor inserido para os múltiplos do metro são: {numeroQuilometros} km, {numeroHectometros} hm e {numeroDecametros} dam")
print(f"O valor inserido para os submúltiplos do metro são: {numeroDecimetros} dm, {numeroCentimetros} cm e {numeroMilimetros} mm")