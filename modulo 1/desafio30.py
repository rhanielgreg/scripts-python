#crie um programa que leia um numero inteiro e mostre na tela se ele eh par ou impar

n = int(input('Digite um numero qualquer: '))

if n % 2 == 0:
    print(f'O numero {n} é PAR')
else:
    print(f'O numero {n} é IMPAR')