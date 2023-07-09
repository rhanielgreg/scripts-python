n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2

print(f'A soma de {n1} e {n2} vale {n1+n2}', end='>>>')
print(f' o produto vale {m} e a divisao vale {d}')
print(f'a divisao inteira vale {di} \n A exponenciacao de {n1} elevado a {n2} vale {e:.3f}')

#pra quebrar a linha dentro do print eh "\n" e para seguir na mesma linha dois print diferente...
#...aplicar apos a aspa ' a virgula e entao end=''