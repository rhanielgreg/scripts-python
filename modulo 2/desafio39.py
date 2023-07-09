# Faca um progrma que leia o ANO DE NASCIMENTO de um jovem  informe, de acordo com sua idade:
# Se ele ainda vai se alista ao servico militar.
# Se eh a hora de se alistar 
# Se ja passou do tempo do alistamento.
#Seu programa devera mostrar o tempo que falta ou que passou do prazo.

import datetime as dt
while True:
    nasc  = int(input('Digite o ano do seu nascimento com 4 digitos: '))
    anoat = int(dt.datetime.now().year) #recebe o ano atual e transforma em numero inteiro
    idade = anoat - nasc
    dif   = 17 - idade
    dif2  = idade - 17

    if idade == 17:
        print("Voce devera se alistar! O Alistamente é obrigatorio!")

    elif idade > 17:    
        print("Seu prazo de alistamento ja passou! Se nao se alistou busque a junta militar!")
        print(f'Voce deveria ter se alistado ha {dif2} anos')

    elif idade < 17:
        print('Voce ainda é muito jovem para o alistamento!')
        print(f'Ainda falta(m) {dif} ano(s) para voce se alistar!')

    opcao = input("Deseja reiniciar o programa? Digite 's' para sim ou qualquer outra tecla para sair: ")
    if opcao.lower() == 's':
        continue
    else:
        break