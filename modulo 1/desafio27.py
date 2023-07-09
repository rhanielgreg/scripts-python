#faca um program que leia o nome completo de uma pessoa e em seguida
#mostre o primeiro e o ultimo nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip().upper()
divide = nome.split()
print(f'primeiro nome: {divide[0]}')
print(f'ultimo nome: {divide[-1]}')