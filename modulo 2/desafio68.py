#faca um programa que jogue par ou impar com o computador.
#o jogo so sera interrompido quando o jogador perder!
#mostre o TOTAL DE VITORIAS CONSECUTIVAS que ele conquistou no final do jogo.

import random
from colorama import Back, Fore, Style
maquina = 0
jogador = 0
quest = ''
soma = 0
vitoria = 0


while True:
    maquina = random.randint(0,10)
    jogador = int(input('Digite um valor: '))
    quest = input(f'Você escolhe {Fore.WHITE}{Back.GREEN}PAR{Style.RESET_ALL} ou {Fore.BLACK}{Back.YELLOW}IMPAR?{Style.RESET_ALL} [P/I]: ').upper()
    soma = maquina + jogador
    print(f'Você escolheu {jogador} e {quest}, eu escolhi {maquina}. {jogador} + {maquina} = {soma}')


    if quest == 'P' and soma % 2 == 0:
        print(f'Parabéns {Fore.WHITE}{Back.BLUE}VOCÊ GANHOU!{Style.RESET_ALL} {soma} é {Fore.WHITE}{Back.GREEN}par{Style.RESET_ALL}')
        vitoria += 1


    elif quest == "I" and soma % 2 != 0:
         print(f'Parabéns {Fore.WHITE}{Back.BLUE}VOCÊ GANHOU!{Style.RESET_ALL} {soma} é {Fore.BLACK}{Back.YELLOW}impar{Style.RESET_ALL}')
         vitoria += 1


    else:
        print(f'{Fore.WHITE}{Back.RED}VOCÊ PERDEU!{Style.RESET_ALL}')
        break

print(f'Você ganhou {vitoria} vezes antes de perder')