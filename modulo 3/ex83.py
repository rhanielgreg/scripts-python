# crie um programa onde o usuario digite uma expressao qualquer que use parenteses
# Seu aplicativo devera analisar se a expressão passada esta com os parenteres 
# abertos e fechados na ordem correta

parenteses = []

entrada = input('Digite uma expressão: ')

for par in entrada:
    if par == '(':
        parenteses.append('(')
    elif par == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')') 
            break

if len(parenteses) == 0:
    print('Parabens, sua expressão esta correta')
else:
    print('sua expressão esta esta errada.')