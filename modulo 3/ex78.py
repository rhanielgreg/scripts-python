# faça um programa que leia 5 valores numericos e guarde os em uma lista

# no final mostre qual foi o valor maior e o menor digitado
# e as suas respectivas posiçoes 

numeros = []

for n in range(0,5):
    num = int(input(f'Digite o {n+1} valor: '))
    numeros.append(num)

posicao_maior = numeros.index(max[numeros])
print(f'O maior valor digitado foi {max[numeros]} e esta na posicao ')
print(f'O menor falor digitado foi {min[numeros]} e esta na posicao ')

print(posicao_maior)

