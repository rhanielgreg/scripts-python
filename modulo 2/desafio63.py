# ESCREVA UM PROGRAMA QUE LEIA UM NUMERO N INTEIRO E MOSTRE NA TELA OS N PRIMEIROS ELEMENTOS DE UMA 
# SEQUENCIA FIBONACCI.

# EX: 0 - 1 - 1 - 2 - 3 - 5 - 8

print('-'* 30)
print('Sequencia de Fibonacci')
print('-'* 30)
n = int(input('Quantos termos deseja mostrar? '))
t1 = 0 
t2 = 1
print(f'{t1} - {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' - {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' - Fim')