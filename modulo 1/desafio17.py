#faca um programa que leia o comprimento do cateto oposto e do cateto adjacente...
#... de um triangulo retangulo. 
#Calculo e mostre a o comprimento da hiputenusa.

import math

cato = int(input('digite o comprimento do cateto oposto: '))
cata = int(input('digite o comprimento do cateto adjacente: '))
hip  = math.hypot(cato, cata)

print(f'A hipotenusa de do triangulo é: {hip}')

