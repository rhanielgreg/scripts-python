#crie um progrma que leia o nome de uma cidade e diga se ela comeca ou nao com o nome santo

cidade = str(input('Digite o nome da sua cidade: ')).strip()
cidadeup = cidade.upper()
lista = cidadeup.split()
print(f'Sua cidade tem Santo no nome? {lista[0] == "SANTO"}')


#queria usar um if-else nesse, mas ai vai alem do pedido, acho que poder atrapalhar...
#...meu aprendizado.
