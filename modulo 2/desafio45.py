#crie um programa que faca o computador jogar JOKENPO com voce

#pedra
#papel 
#tesoura

import random as rd
print("VAMOS JOGAR JOKENPO!")
p1 = input('EscolhA: PEDRA, PAPEL ou TESOURA: ').strip().upper()
bot = ['PEDRA', 'PAPEL', 'TESOURA']
bt1 = rd.choice(bot)

if p1 == bt1:
        print('EMPATAMOS!')
###############################################################################
if p1 == 'PEDRA' and bt1 == 'TESOURA': #pedra esmaga tesoura - jogador vence
        print(f'Parabens, voce ganhou! :( - voce escolheu {p1} e eu escolhi {bt1}')

elif p1 == 'PEDRA' and bt1 == 'PAPEL':#PAPEL embrulha pedra - programa vence
        print(f'HAHAHA Voce perdeu - Voce escolheu {p1} e eu {bt1}') 

################################################################################

elif p1 == 'TESOURA' and bt1 == 'PEDRA':#pedra esmaga tesoura - programa vence
        print(f'HAHAHA Voce perdeu - Voce escolheu {p1} e eu {bt1}') 

elif p1 == 'TESOURA'and bt1 == 'PAPEL':# tesoura corta papel e jogador vence
        print(f'Parabens, voce ganhou! :( - voce escolheu {p1} e eu escolhi {bt1}')

#################################################################################

elif p1 == 'PAPEL' and bt1 == 'TESOURA': #tesoura corta papel - programa vence
        print(f'HAHAHA Voce perdeu - Voce escolheu {p1} e eu {bt1}') 

elif p1 == 'PAPEL' and bt1 == 'PEDRA':#papel embrulha pedra - jogador vence
         print(f'Parabens, voce ganhou! :( - voce escolheu {p1} e eu escolhi {bt1}')