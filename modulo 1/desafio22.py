#Crie um programa que leia o NOME COMPLETO de uma pessoa e mostre:
#O nome com toda as letras maiusculas
#o nome com todas as letras minusculas
#Quantas letras tem ao todo sem considerar os espacos
#Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: '))
nomelow = nome.lower()
nomeupper = nome.upper()
qtletra = len(nome.replace(" ", ""))
nomediv = nome.split()
qtnome = len(nomediv[0])

print(f'Nome todo em maiusculas: {nomeupper}')
print(f'Nome todo em minusculas: {nomelow}')
print(f'Total de caracteres sem espaco: {qtletra}')
print(f'O primeiro nome tem {qtnome} letras')