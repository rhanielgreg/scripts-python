# crie um program que leia o ano de nascimento de7 pessoas
# no final mostre quantas pesoas  ainda nao atingiram a maioridade
# e quantos ja sao maiores

from datetime import datetime as dt
maiores = 0
menores = 0
for idd in range(0,7):
    ano = int(input('Digite  o ano de nascimento: '))
    idade = dt.now().year - ano

    if idade < 18:
        menores += 1
    else:
        maiores += 1
print(f'ha {maiores} pessoas maiores e {menores} pessoas menores')
    
    

