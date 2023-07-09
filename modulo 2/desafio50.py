# desenvolva um programa que leia seis numeros inteiros
# e mostre a soma apenas daqueles que forem pares, se for impar desconsidere

soma = 0
for i in range(0,6):
    b = int(input('Digite um numero: '))
    if b % 2 == 0:
        soma += b

print(f'A soma dos numeros pares digitados é igual a: {soma}')