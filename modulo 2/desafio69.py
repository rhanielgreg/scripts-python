#crie um programa que leia: IDADE e SEXO de varias pessoas;
#a cada pessoa cadastrada o programa deve perguntar ao usuario se ele quer continuar.
#no final mostre quantas pessoas tem mais de 18 anos, quantos homens foram cadastrados, e 
#... quantas mulheres tem menos de 20 anos

maior = 0
maior_lista = []

homem = 0
homem_lista = []

mulher_20 = 0
mulher_lista = []

idade = 0
sexo = ''
continua = ''

while True:
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu SEXO(M para mulher e H para homem): ').upper()
   
    if sexo == 'M' and idade < 20:
        mulher_20 += 1
        mulher_lista.append(idade)


    if sexo == 'H':
        homem += 1
        homem_lista.append(sexo)



    if idade >= 18:
        maior += 1
        maior_lista.append(idade)
     
     
    continua = input('Cadastrar mais alguma pessoa?[S/N]: ').upper()
    if continua != 'S':
        break
    
   
    
print(f'{maior} maiores de 18')
print(f'{maior_lista}')
print(f'{homem} homens cadastrados')
print(f'{homem_lista}')
print(f'{mulher_20} mulheres menos de 20')
print(f'{mulher_lista}')