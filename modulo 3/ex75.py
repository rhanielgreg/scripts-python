# desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final mostre:

# 1 - quantas vezes apareceu o valor 9

# 2 - em que posição foi digitado o primeiro valor 3

# 3- quais foram os numeros pares


lista_de_numeros = (

int(input('Digite o primeiro número: ')),
int(input('Digite o segundo número: ')),
int(input('Digite o terceiro número: ')),
int(input('Digite o quarto e último número: '))

)

lista_do_tres = []
pares = []
quantidade_de_nove = 0



for numeros in lista_de_numeros:
    if numeros % 2 == 0:
        pares.append(numeros)

    lista_para_str = str(numeros)
    quantidade_de_nove += lista_para_str.count('9')
    lista_do_tres.extend(lista_para_str)

print(f'O numero 9 foi digitado {quantidade_de_nove} vezes')

try:
    index_do_3 = lista_do_tres.index('3') +1
    print(f'O primeiro número 3 digitado está na posição {index_do_3}')
    
except ValueError:
    print('Não há nenhum número "3" nesta lista')


print(f'Os numeros pares são: {pares}')
