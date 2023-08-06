# crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços, na sequencia.
# no final mostre a listagem de preços, organizando os dados em forma tabular.


compras = (
'CELULAR',2000, #1
'NOTEBOOK',4500,#2
'MONITOR',1250, #3
'MOUSE',100,    #4
'TECLADO',150,  #5
'FONTE',120,    #6
'HEADSET',180   #7 
           )


pedido = 0
print('-'*40)
print(f'{"LISTA DE PRODUTOS":^40}')
print('-'*40)


for posicao in range(0, len(compras)):
    if posicao %2 == 0:
        print(f'{compras[posicao]:.<30}', end='')
    else:
        print(f'R$ {compras[posicao]:>7.2f}')


print('-'*40)