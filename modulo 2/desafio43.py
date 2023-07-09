#desenvolva uma logica que leia o peso e a altura de uma pessoa.
#calcule seu IMC e mostre seu status de acordo com a tabela abaixo

#abaixo de 18.5 - abaixo do peso
#entre 18.5 e 25 - peso ideal
#25 ate 30 - sobrepeso
#30 ate 40 - obesidade
#acima de 40 - obesidade morbida

from colorama import Fore, Back, Style
print(f'{Back.GREEN}{Fore.BLACK}--{Style.RESET_ALL}'*10)
print(f'{Back.GREEN}{Fore.BLACK} CALCULADORA DE IMC {Style.RESET_ALL}')
print(f'{Back.GREEN}{Fore.BLACK}--{Style.RESET_ALL}'*10)



peso = float(input('Digite o seu peso em KG: ')) #usuario insere peso em quilos
alt = float(input('Digite a sua altura em Metros: ')) # usuario insere altura em metros
imc =  peso / (alt**2) # formula para calcular IMC

if imc == imc < 18.5:
    print(f'O seu IMC é de {imc:.2f} e voce está {Fore.WHITE}{Back.RED}ABAIXO{Style.RESET_ALL} do peso!')

elif imc == imc >= 18.5 and imc <= 25 :
    print(f'O seu IMC de {imc:.2f} é o {Fore.WHITE}{Back.BLUE}IDEAL!{Style.RESET_ALL} Parabens!')

elif imc == imc >= 26 and imc <= 30:
    print(f'O seu imc de {imc:.2f} é de {Fore.BLACK}{Back.YELLOW}SOBREPESO!{Style.RESET_ALL}')

elif imc == imc >= 31 and imc <= 40:
    print(f'O seu IMC de {imc:.2f} é de {Fore.WHITE}{Back.RED}OBESIDADE!{Style.RESET_ALL}')

elif imc == imc > 40:
    print(f'O seu IMC de {imc:.2f} é de {Fore.WHITE}{Back.RED}OBESIDADE MORBIDA!{Style.RESET_ALL} ')


    



