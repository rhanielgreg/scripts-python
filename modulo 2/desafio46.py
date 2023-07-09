# faca um progrma que mostre uma
# tela de contagem regressiva para o estouro
# de fogos de artificio, indo de 10 ate 0 com 
# uma pause de 1 segundo entre elas

from colorama import Back, Fore, Style
from emoji import emojize
from time import sleep

print(f'{Back.WHITE}{Fore.BLACK}CONTAGEM ANO NOVO.')
for cr in range(10, -1, -1):
        sleep(1)
        print(f'{cr}')
print(emojize(f':firecracker: Feliz ano novo! :firecracker:{Style.RESET_ALL}'))
