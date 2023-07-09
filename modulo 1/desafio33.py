# faca um programa que leia 3 numeros e mostre qual eh o maior e qual o menor.

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o ultimo numero: '))
lista = [n1, n2, n3]
lista.sort()

print(f'O menor numero é {lista[0]} e o maior numero é {lista[2]}')
