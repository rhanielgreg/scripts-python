# Escreva um programa para aprovar o emprestimo bancario para a  compra de uma casa.

# O programa vai perguntar o VALOR DA CASA, o SALARIO do comprador e em QUANTOS ANOS vai pagar
# Calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 30% do salario,
#ou entao o emprestimo sera negado.

from colorama import Fore, Back, Style 
class emprestimo:

    print (Fore.BLUE + Back.WHITE + '-=-=' *15 + Style.RESET_ALL)
    print(Fore.BLUE + Back.WHITE + ' APROVACAO DE EMPRESTIMO BANCARIO PARA COMPRA DE RESIDENCIA ' + Style.RESET_ALL)
    print (Fore.BLUE + Back.WHITE + '-=-=' *15 + Style.RESET_ALL)
    vcasa = float(input('Digite o valor da casa: R$ '))
    sal = float(input('Digite o seu salario: R$ '))
    ano = int(input('Em quantos anos voce vai pagar? '))
    parc = vcasa / (ano * 12)

    if parc > sal * 0.3:
        print(f'{Fore.BLACK}{Back.RED}EMPRESTIMO NEGADO{Style.RESET_ALL}')
    else:
        print(Fore.BLACK + Back.GREEN + 'EMPRESTIMO APROVADO!' + Style.RESET_ALL)
        print(f'O valor da prestacao sera de' + Fore.GREEN + f' R${parc:.2f}' + Style.RESET_ALL + f' em {ano*12} meses')

