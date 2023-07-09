#faca um programa que leia um angulo qualquer e mostre na tela o valor do SENO, COSSENO e TANGENTE
#desse angulo

import math

ang = float(input('Digite qualquer angulo: '))
ang_rad = math.radians(ang)
sen = math.sin(ang_rad)
cos = math.cos(ang_rad)
tan = math.tan(ang_rad)

print(f'Para o angulo de {int(ang)}')
print(f' Seno: {sen:.2f}')
print(f' Cosseno: {cos:.2f}')
print(f' Tangente: {tan:.2f}')