#Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor eh maior
# O segundo valor eh maior
# Nao existe valor maior, os dois sao iguais

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print('o primeiro valor é maior!')

elif n2 > n1:
    print('O segundo valor é maior!')

else: 
    print('Nao existe valor maior pois os dois sao iguais!')