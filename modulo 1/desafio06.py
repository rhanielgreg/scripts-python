#crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

name = input('Ola, digite seu nome: ')
n = int(input('Digite um numero: '))
d = n*2
t = n*3
rq = n**(1/2)
print(f'Ola, {name}, o dobro de {n} é {d}\n O triplo de {n} é {t}\n A raiz quadradade {n} é {rq:.0f}')
