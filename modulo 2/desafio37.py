# Escreva um programa que leia um numero inteiro qualquer e peca para o usuario escolher 
# qual sera a BASE DE CONVERSAO:
# 1 para binario
# 2 para octal
# 3 para hexadecimal

print('-' * 30)
print(' CALCULADORA HEX - OCT - BIN')
print('-' *30)

inte = int(input('Digite um numero inteiro: '))
print('-----Escolha a base de conversao-----')
print('1 para BINARIO ')
print('2 para OCTAL ')
print('3 para HEXADECIMAL ')
base = int(input('Digite a opcao: '))

if base == 1:
    print('-' * 30)
    print(f'O numero {inte} em binario é {format(inte, "b")}')

elif base == 2:
    print('-' * 30)
    print(f'O numero {inte} em octal é {format(inte, "o")}')

elif base == 3:
    print('-' * 30)
    print(f'O numero {inte} em hexadecimal é {format(inte, "x")}')

else:
    print('-' * 30)
    print('Digite uma opcao valida! (1,2,3)')




