# crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os 
# em uma lista, ja na posição correta de inserção no final mostre a lista ordenada.

lista = []

for numero in range(0,5):
    valores = int(input(f'Digite o {numero+1} valor: '))
    lista.append(valores)

print(f'A lista de numeros: {sorted(lista)}')