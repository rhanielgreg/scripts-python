# faca um programa que calcule a soma entre todos os numeros
# impares que sao multiplos de 3 e que se encontrem 
# entre 1 e 500.
soma = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        soma += c
print(soma)