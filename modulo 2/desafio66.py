#crie um programa que leia varios numeros inteiros pelo teclado
#o programa só vai parar quando o usuario digita 999 que é a condição de parada
#no final:
#mostre QUANTOS NUMEROS foram digitados e qual foi a SOMA entre eles(desconsiderando o flag)

n = 0
contador = 0
soma = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    contador += 1
    soma += n
print(f'Você digitou {contador} numeros!')
print(f'A soma dos numeros digitados é {soma}')