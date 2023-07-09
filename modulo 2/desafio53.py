# # crie um programa que leia uma frase qualquer e diga se ela eh um palindromo
# desconsiderando os espacos

texto = input("Digite uma frase: ").upper().strip()
palavras = texto.split()
textore = ''.join(palavras)
if textore == textore[::-1]:
    print('PALINDROMO')
else:
    print('NAO EH PALINDROMO')