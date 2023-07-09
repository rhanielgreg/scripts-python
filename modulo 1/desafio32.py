#faca um programa que leia um ano qualquer e mostre se ele eh um ano BISSEXTO

#regras de ano bssexto:
# DIVIDIDO POR 4 TEM QUE SER INTEIRO(SEM RESTO)
# DIVIDIDO POR 100 PRECISA TER RESTO, POREM...
# DIVIDIDO POR 400 TEM QUE SER INTEIRO (SEM RESTO)  

ano = int(input('Digite um ano com 4 digitos: '))
c1 = ano % 4
c2 = ano % 100
c3 = ano % 400

if c1 == 0 and c2 != 0:
    print(f'O ano {ano} é bissexto!')

elif c1 == 0 and c2 == 0 and c3 == 0:
    print(f'O ano de {ano} é bissexto!')

else: 
    print(f'O ano {ano} NAO é bissexto!')