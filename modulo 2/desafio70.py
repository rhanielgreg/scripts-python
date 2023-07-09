#crie um programa que leia NOME e PREÇO  de varios produtos.
#o programa devera perguntar se o usuario quer continuar
#no final mostre:
#qual o total gasto na compra
#quantos produtos custam mais de 1000 reais
#qual o nome do produto mais barato

from colorama import Fore as f, Style as s, Back as b
contador = 0
preco = 0
total_gasto = 0
mais_de_mil = 0
preco_barato = 0
produto = ''
produto_barato = ''
continua = ''

print(f'{b.GREEN}{f.RED}-' *20)
print(f'{b.GREEN}{f.RED}Analise de produtos')
print(f'{b.GREEN}{f.RED}-' *20)
print(f'{b.GREEN}{f.RED}{s.RESET_ALL}')

while True:
    produto = str(input(f'Digite o {f.WHITE}{b.BLUE}NOME DO PRODUTO{s.RESET_ALL}: ')).upper()
    preco = int(input(f'Digite o {f.WHITE}{b.YELLOW}PREÇO DO PRODUTO{s.RESET_ALL}: '))   
    contador += 1
    total_gasto += preco

    #se houver apenas 1 produto cadastrado ele sera o mais barato
    if contador == 1:
        produto_barato = produto
        preco_barato = preco

    #se houver mais de 1 produto cadastrado ele ira comparar o preco com os outros produtos e alterar o valor
    if contador > 1:
        if preco < preco_barato:
            produto_barato = produto
            preco_barato = preco
    
    #adiciona os produtos que custam mais de 1000 reais na lista de produtos com mais de 1000
    if preco > 999:
        mais_de_mil += 1

    continua = input(f'Deseja adicionar mais produtos? {b.WHITE}[{f.WHITE}{b.GREEN} S {s.RESET_ALL}{b.WHITE}/{f.WHITE}{b.RED} N {s.RESET_ALL}{b.WHITE}]{s.RESET_ALL}: ').upper()
    if continua != 'S':
        break

print(f'{s.BRIGHT}O total gasto com produtos foi de: {f.WHITE}{b.RED}R$ {total_gasto:.2f}{s.RESET_ALL}')

print(f'{s.BRIGHT}Há {mais_de_mil} produtos que custam mais de {f.WHITE}{b.BLUE}R$1.000{s.RESET_ALL}')
print(f'{s.BRIGHT}{f.WHITE}{b.GREEN}{produto_barato}{s.RESET_ALL}{s.BRIGHT} é o produto mais barato custando {f.WHITE}{b.BLUE}R$ {preco_barato:.2f}!{s.RESET_ALL}')

    




