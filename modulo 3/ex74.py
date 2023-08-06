# crie um programa que vai gerar 5 numeros aleatorios e colocar em uma tupla.
# Depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estao 
# na tupla

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1,10), randint(1,10))

print('Os numeros gerados aleatoriamente são: ')
for n in numeros:
 
    print(f'{n}, ', end='')

print(f' \n O maior número da tupla é {max(numeros)}')
print(f' O menor número da tupla é {min(numeros)}')