# crie um programa onde o usuario possa adicionar varios valores numericos
#  e cadastre-os em uma lista.
# caso o numero ja exista la dentro, nao sera adicionado.
# No final sera exibido todos os valores unicos digitados e em ordem crescente

lista_de_valores = []

while True:

    valor = int(input('Digite o valor numerico: '))

    if not valor in lista_de_valores:    
        lista_de_valores.append(valor)
    
    continua = input('aperte enter para adicionar mais valores ou digite "N" para encerrar:').upper()
    if continua == 'N':
        break


print(f'Os valores adicionados foram {sorted(lista_de_valores)}')