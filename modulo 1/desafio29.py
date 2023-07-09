# escreva um programa que leia a velocidade de um carro.
# se ele ultrapassar 80km/h mostre uma msg que ele foi multado
# a multa vai custar 7 reais por cada kilometro acima do limite

v = int(input('Digite a velocidade do seu carro: '))
vmax = 80
vl = 7

if v > 80:
    multa = (v - vmax)*7
    print(f'Voce foi multado no valor de R$ {multa:.2f}')
else:
    print('Voce nao foi multado!')


# nao foi pedido explicitamente para calcular a multa, porem fiz pois mostra o valor...
# por km excedido. Entendi implicitamente que deveria fazer assim.