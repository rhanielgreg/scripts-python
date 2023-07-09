# faca um progrrama que leia um numero inteiro e diga se 
# ele é ou nao um numero primo

n = int(input('Digite um numero para descobrir se ele é primo: '))
if n < 2:
    primo = False
else:
    primo = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            primo = False
            break     
        
if primo:
    print(f' O Numero {n} é primo')
else:
    print(f'O numero {n} nao é primo')