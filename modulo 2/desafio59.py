# CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:

# [1] SOMAR
# [2] MULTIPLICAR
# [3] MAIOR
# [4] NOVOS NUMEROS
# [5] SAIR DO PROGRAMA

# SEU PROGRAMA DEVERA REALIZAR A OPERAÇÃO SOLICITADA EM CADA CASO.

maior = []
n1 = int(input('Digite um numero qualquer: ')) 
n2 = int(input('Digite mais um numero qualquer: '))

menu = 0

while menu != 5:
    print('MENU DE OPÇÕES')
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NUMEROSS')
    print('[5] SAIR DO PROGRAMA')
    menu = int(input('DIGITE UMA DA OPÇÕES ACIMA: '))
    
    if menu == 1:
        print(f'Você escolheu SOMAR e a soma de de {n1} e {n2} é {n1+n2}')

    elif menu == 2:
        print(f'Você escolheu MULTIPLICAR: a multiplicação de {n1} e {n2} é {n1*n2}')

    elif menu == 3:
        maior.append(n1)
        maior.append(n2)
        print(f'O número maior entre {n1} e {n2} é {max(maior)}')

    elif menu == 4:
        n1 = int(input('Digite outro primeiro numero: '))
        n2 = int(input('Digite agora outro segundo numero: '))

    elif menu == 5:
        print('finalizando...')
    else: 
        print('comando invalido. Tente novamente')