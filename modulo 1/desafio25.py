#crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome

nome = str(input('Digite seu nome completo: ')).strip().upper()
lista = nome.split()
check = "SILVA" in lista

########################################
if check == True:
    print('Seu nome TEM Silva!!!')

else:
    print('Seu nome NAO TEM Silva!!!')
########################################



#codigo "certo" pra aula
#print(f'O seu nome tem Silva?')
#print(check)



