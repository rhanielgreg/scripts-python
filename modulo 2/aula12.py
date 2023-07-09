################ESTRUTURA CONDICIONAL ANINHADA##################

nome = str(input('Qual o seu nome? ')).capitalize()
####
if nome == 'Greg':
    print('Que nome bonito!')
 ##############################################################
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome eh bem popular no Brasil!')
###############################################################
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino!')
################################################################
else:
    print('Seu nome eh bem comum!')

print(f'tenha um bom dia {nome}')

################ESTRUTURA CONDICIONAL ANINHADA##################