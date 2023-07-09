# CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS INTEIROS PELO TECLADO.
# O PROGRAMA SÓ VAI PARAR QUANDO O USUARIO DIGITAR 999 QUE É A CONDIÇÃO DE PARADA.
# NO FINAL MOSTRE QUANDO NUMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES.
# DESCONSIDERANDO  O FLAG

tentativas = 0
soma = 0
n = 0 
n = int(input('Digite qualquer numero inteiro: '))
while n != 999:
    tentativas += 1
    soma += n
    n = int(input('Digite qualquer numero inteiro: '))
print(f'Você digitou {tentativas} números e a soma desses numeros é {soma}')