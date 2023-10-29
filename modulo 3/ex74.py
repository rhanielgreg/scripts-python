# crie um programa que vai gerar 5 numeros aleatorios e colocar em uma tupla.
# Depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estao 
# na tupla

from random import randint #importa o item randint da biblioteca random

###
#cria uma tuma em que cada item da tupla é um numero inteiro aleatorio entre 1 e 10
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1,10), randint(1,10))
###


print('Os numeros gerados aleatoriamente são: ')
for n in numeros: #loop for usado para coletar os numeros da tupla um por um
 
    print(f'{n}, ', end='') # end='' usado para não ter quebra de linha a cada for

print(f' \n O maior número da tupla é {max(numeros)}') #mostra o maior valor dentro da tupla 
print(f' O menor número da tupla é {min(numeros)}')#mostra o menor valor dentro da tupla