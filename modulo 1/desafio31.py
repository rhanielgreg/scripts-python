#desenvolva um programa que pergunte a distancia de uma viagem em km.
# calcule o preco da passagem, cobrando 50 centavos por KM para viagens de ate 200km...
# e 45 centavos para viagens mais longa.

km = int(input('Digite em quilometros a distancia: '))

if km > 200:
    p1 = km * 0.45
    print(f'O preco da sua passagem é de R$ {p1:.2f}!')
else:
    p1 = km * 0.50
    print(f'O preco da sua passagem é de R$ {p1:.2f}!')