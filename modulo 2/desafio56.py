# desenvolva um programa que leia Nome, idade e sexo de 4 
# pessoas.
# No final mostre:

# a media de idade do grupo
# qual o nome do homem mais velho
# e quantas mulheres tem menos de 21 anos

somaidade = 0
media = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for dados in range(1, 6):
    nome = input(f'Digite o nome {dados}: ')
    idade = int(input(f'Digite a idade {dados}: '))
    sexo = input(f'Digite o sexo  {dados} (H para homem e M para mulher): ').upper()
    somaidade += idade
    if dados == 1 and sexo in 'Hh':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Hh' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm'and idade < 21:
        totmulher20 += 1


#calcula a media das idades de dentro da lista
media = somaidade/4
############################################
    

print(f'A media de idade do grupo é de {media} anos')
print(f'O homem mais velho se chama {nomevelho} e tem {maioridadehomem}')
print(f'Há {totmulher20} mulheres com menos de 21 anos')