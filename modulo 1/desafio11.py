#faca um programa que leia a altura e a largura de uma parede em metros
# calcule a sua area, e a quantidade de tinta necessaria para pinta-la 
#sabendo que cada litro de tinta pinta uma area de 2m^2

h = int(input('Digite a altura da parede: '))
w = int(input('Digite a largura da parde: '))
a = h*w
t = a/2
print(f'Voce precisa de {t:.0f}L para pintar sua parede de {a}m^2')


