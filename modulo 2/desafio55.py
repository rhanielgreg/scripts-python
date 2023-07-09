# faca um programa que leia o peso de 5 pessoas
# informe qual o maior e o menor peso lido

pesos = []

for p in range(0,5):
    peso = float(input(f'Digite o peso {p+1}: '))
    pesos.append(peso)

pesado = max(pesos)
leve = min(pesos)

print(f'O maior peso é {pesado:.2f} e o menor peso é {leve:.2f}')