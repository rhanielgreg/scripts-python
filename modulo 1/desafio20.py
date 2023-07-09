# O mesmo professor do desafio anterior quer sortear a ordem de apresentacao de trabalho dos alunos.
# Faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

a1 = input('primeiro aluno: ')
a2 = input('segundo aluno: ')
a3 = input('terceiro aluno: ')
a4 = input('quarto aluno: ') 
lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'a ordem sorteada foi:')
print(lista)