#desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media.

name = input('Digite o nome do aluno: ')
a1 = float(input('Digite a nota da Avaliacao 1: '))
a2 = float(input('Digite a note da Avaliacao 2: '))
s = a1 + a2
media = s/2
print(f'Considerando as seguintes notas:\n A1: {a1}\n A2: {a2}\n A média final de {name} é {media}.')
