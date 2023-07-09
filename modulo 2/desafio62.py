# MELHORE O DESAFIO 61 PERGUNTANDO PARA O USUARIO SE ELE QUER MOSTRAR MAIS ALGUNS TERMOS.
# O PROGRAMA ENCERRA QUANDO ELE DISSE QUE QUER MOSTRAR 0 TERMOS.

first = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = first
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo}, ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Digite o total de termo que deseja adicionar. Caso não queira digite 0: '))
print('Finalizando...')
print(f'Você usou {total} termos.')
