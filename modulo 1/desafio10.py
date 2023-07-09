#Crie um programa que leia quanto dinheiro ela tem na carteira e mostre quantos dolares ela pode comprar.
#considere o 1 dolar = R$ 3,27

name = input('Ola, digite seu nome: ')
real = int(input('Digite quantos Reais voce tem: '))
dolar = real * 3.27
print(f'{name}, voce pode comprar ${dolar}(em dolares) com seu dinheiro disponivel.')