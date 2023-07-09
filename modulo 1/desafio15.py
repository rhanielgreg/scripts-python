#Escreva um programa que pergunte a quantidade de Km percorridos 
#por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, #sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos Km foram percorridos? '))
dias = int(input('Quantos dias voce usou o carro? '))
diaria = 60
pkm = 0.15

valor = (km*pkm)+(dias*diaria)

print(f'O valor do aluguel a ser pago é de {valor:.2f}')