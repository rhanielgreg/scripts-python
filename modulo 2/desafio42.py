#refaca o desafio 035 dos triangulos acrescentando o recurso de mostrar que tipo de triangulo
#sera formado:

#equilatero - todos os lados iguais
#isosceles - dois lados iguais
# escaleno - todos os lados diferentes

print('Siga as instrucoes abaixo para saber se é possivel formar um triangulo.')
l1 = int(input('Digite o primeiro comprimento: '))
l2 = int(input('Digite o segundo comprimento: '))
l3 = int(input('Digite o terceiro comprimento: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('É POSSIVEL FORMAR UM TRIANGULO COM OS NUMEROS DIGITADOS')
    if l1 == l2 == l3:
        print('O triangulo é um triangulo EQUILATERO')
    
    elif l1 != l2 != l3 != l1:
        print('O triangulo é um triangulo ESCALENO')

    else:
        print('O triangulo é um triangulo ISOSCELES')


else:
    print('NAO É POSSIVEL FORMAR UM TRIANGULO COM OS NUMERO DIGITADOS')