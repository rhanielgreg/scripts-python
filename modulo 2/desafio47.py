# crie um programa que mostre na tela todos os
# numeros pares que estao no intervalo entre 1 e 50

from time import sleep

for p in range(1, 51):
    if p % 2 == 0:
        sleep(.5)
        print(p)
print('FIM')