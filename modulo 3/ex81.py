# crie um programa que leia varios numeros e coloque numa lista
# depois disso mostre:

# quantos numeros foram digitados
# a lista de valores ordenado em ordem descrescente
# se o valor 5 foi digitado e esta ou nao na lista

lista_total = []
while True:
    numero = int(input('Digite um numero: '))
    lista_total.append(numero)

    continua = input('deseja adicionar mais numeros? S ou N: ').upper()
    if continua == 'N':
        break

if 5 in lista_total:
    print('O numero 5 esta na lista digitada')
else:
    print('o numero 5 não foi digitado na lista')

print(f'O total de numeros digitados foi de {len(lista_total)}')
print(f'A lista em ordem descrescente é {sorted(lista_total, reverse=True)}')