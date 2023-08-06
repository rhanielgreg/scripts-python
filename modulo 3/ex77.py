# crie um programa que tenha uma tupla com varias palavras(nao usar acentos).
# Depois disso você deve mostrar, para cada palavra, quais são suas vogais.

palavras =(

'rhaniel',
'greg',
'de',
'paula',
'silveira'

)

for p in palavras:
    print(f'\nNa palavra "{p.upper()}" temos as vogais ', end='')
    for letras in p:
        if letras in 'aeiou':
            print(f'"{letras}"', end=' ')

