# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faca um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
ls = [a1, a2, a3, a4]
es = random.choice(ls)
print(f'O aluno escolhido para apagar o quadro foi: {es}!')
