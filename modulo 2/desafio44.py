#elabore um programa que calcule o valor a ser pago por um produto
# considerando seu preco normal e condicao de pagamento.
#a vista - dinheiro/cheque - 10% de desconto
#a vista - cartao - 5% de desconto
#em ate 2x no cartao - preco normal
#3x ou mais no cartao 20% de juros

nprod = float(input('Digite o valor do produto: '))
forma = int(input('Escolha a forma de pagamento: 1 para pagamento a vista e 2 para pagamento parcelado: '))
avdc = nprod - (nprod * .1)
acc = nprod - (nprod * .05)
trespar = nprod + (nprod * .2)

if forma == 1:

    form1 = int(input('O pagamento sera A VISTA no cartao(digite 1) ou em dinheiro(digite 2): '))
    if form1 == 1:
        print(f'O valor a ser pago com desconto a vista no debito é de {acc:.2f}!')
    elif form1 == 2:
        print(f'O valor a ser pago com desconto a vista do dinheiro é de {avdc:.2f}!')

elif forma == 2: 
    form1 = int(input('Escolha em quantas parcelas voce quer pagar: '))
    if form1 <= 2:
        print(f'Para pagamentos em ate 2x no credito nao ha acrescimo de juros e nem descontos!')
        print(f'O valor a ser pago é de {nprod:.2f}!')
    elif form1 >= 3:
        print(f'O valor a ser pago com juros de 20% é de R$ {trespar:.2f}!')
