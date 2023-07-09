#desenvolva um programa que leia comprimento de TRES retas
#diga se as retas podem ou nao formar um triangulo
print('Siga as instrucoes abaixo para saber se é possivel formar um triangulo.')
l1 = int(input('Digite o primeiro comprimento: '))
l2 = int(input('Digite o segundo comprimento: '))
l3 = int(input('Digite o terceiro comprimento: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('É POSSIVEL FORMAR UM TRIANGULO COM OS NUMEROS DIGITADOS')

else:
    print('NAO É POSSIVEL FORMAR UM TRIANGULO COM OS NUMERO DIGITADOS')