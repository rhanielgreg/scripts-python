#crie um programa que simule um caixa eletronico.
#pergunte o valor a ser sacado no inicio(numero inteiro)
#o programa ira dizer quantas cedulas de cada valor serao entregues
#considere que o caixa tem cedular de 1, 10, 20 e 50


valor = int(input('Digite o valor a ser sacado: R$ '))
total = valor
cedula = 50
totaldecedula = 0

while True:
    if total >= cedula:
        total -= cedula
        totaldecedula += 1
    else:
        if totaldecedula > 0:
            print(f'{totaldecedula} cedulas de {cedula}')
        
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totaldecedula = 0

        if total == 0:
            break

