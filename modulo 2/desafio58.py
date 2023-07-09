# MELHORE O DESAFIO 28 ONDE O COMPUTADOR VAI PENSAR EM UM NUMERO ENTRE 0 E 10.
# SO QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR ATÉ ACERTAR, MOSTRANDO NO FINAL QUANTOS PALPITES
# FORAM NECESSÁRIOS PARA VENCER.

import random
j1 = int(random.randint(0,10))
j2 = 0
tenta = 0
while j1 != j2:
    j2 = int(input('Digite um numero de 0 a 10: '))
    if j2 != j1:
        tenta += 1
        print('Você errou, tente novamente!')
        
print(f'Você acertou! e errou {tenta} vezes antes de acertar')