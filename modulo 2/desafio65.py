# CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS INTEIROS PELO TECLADO.
# NO FINAL DA EXECUCAO MOSTRE A MEDIA ENTRE TODOS OS VALORES E QUAL FOI O MAIOR E O MENOR VALOR LIDO.
# O PROGRAMA DEVE PERGUNTAR AO USUARIO SE ELE QUER CONTINUAR OU NAO A DIGITAR VALORES.
cont = 0
n = 0
soma = 0
lista = []
seq = ''
while seq != 'N':
    n = int(input('Digite um numero inteiro: '))
    cont += 1
    soma += n
    lista.append(n)
    seq = input('Deseja continuar? (S/N): ').upper()
print('__' *20)
print('')
print('    :HISTORICO DE DADOS DIGITADOS:')
print('__' *20)
print('')
print(f'Você digitou {cont} números no total;')
print(f'A média de todos os números que você digitou é {soma / cont:.3f}')
print(f'O menor número digitado foi {min(lista)}')
print(f'O maior número digitado foi {max(lista)}')