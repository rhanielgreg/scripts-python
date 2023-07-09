# FAÇA UM PROGRAMA QUE LEIA UM NOMERO QUALQUER E MOSTRE SEU FATORIAL

# EX:
# 5! = 5X4X3X2X1=120

numero = int(input("Digite um número inteiro positivo: "))
contador = numero
fatorial = 1
print(f'calculando {numero}! = ', end='')
while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1 
print(f'{fatorial}')