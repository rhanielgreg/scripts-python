# crie uma lista que leia varios numeros e coloque numa lista
# depois crie duas listas extras que vao conter apenas o valores pares e impares
# digitados, respectivamente.

# no final mostre o conteudo das 3 listas

lista_geral = []
pares = []
impares = []

while True:
    valores = int(input('Digite o valor: '))
    lista_geral.append(valores)

    if valores % 2 == 0:
        pares.append(valores)
    else:
        impares.append(valores)

    continuar = input('Deseja parar? S/N: ').upper()
    if continuar == 'S':
        break

print(lista_geral)
print(pares)
print(impares)