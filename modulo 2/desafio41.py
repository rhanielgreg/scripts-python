#a confederacao nacional de natacao precisa de um programa que leia o ano de nascimento 
#de um atleta e mostre sua categoria, de acordo com a idade:

#ate 9 anos  - mirim
#ate 14 anos - infantil
#ate 19 anos - junior
#ate 20 anos - senior
#acima - master
import datetime as dt

nasc = int(input('Digite o ano de nascimento do atleta: '))
atual = dt.datetime.now().year
idd = atual - nasc

if idd <= 9:

    print('O aluno esta na categoria MIRIM')

elif idd > 9 and idd < 15:
    print('A categoria do atleta é INFANTIL')

elif idd >= 15 and idd < 20:
    print('A categoria do atleta é JUNIOR')

elif idd == 20:
    print('A categoria do atleta é SENIOR')

else:
    print('A categoria do atleta é MASTER')