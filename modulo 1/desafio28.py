#escreva um programa que faca o computador pensar em um numero inteiro entre 0 a 5 e...
#peca para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
#O programa devera escrever na tela se o usuario venceu ou perdeu.

import random
from time import sleep

n = int(random.randint(0,5))
nu = int(input('Descubra qual o numero sorteado (de 0 a 5): '))
print('Escolhendo o numero...')
sleep(3)

if nu == n:
    print('Voce acertou!')
else:
    print(f'Voce errou! O numero é {n}')