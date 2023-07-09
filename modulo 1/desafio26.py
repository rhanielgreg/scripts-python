#faca um programa que leia uma frase pelo teclado e mostre: 
#Quantas vezes apareceu a letra A
#Em que posicao aparece a primeira vez
#Em que posicao ela aparece a ultima vez

frase = str(input('Digite uma frae: ')).strip().upper()
conta = frase.count('A')
first = frase.find('A')
last = frase.rfind('A')

print(f'A letra "A" aparece {conta} vezes')
print(f'ela aparece pela primeira vez no carectere {first}')
print(f'Esta letra aparece por ultimo no caractere {last}')
