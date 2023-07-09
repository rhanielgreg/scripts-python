#faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
#unidade, dezena, centena e milhar

milhar = int(input('digite um numero entre 0 e 9999: '))
u = milhar // 1 % 10
d = milhar // 10 % 10
c = milhar // 100 % 10
m = milhar // 1000 % 10

#ainda nao entendi mto claramente essas matematicas mas vamo que vamo(ex-aluno media 3 de exatas)

print(f'unidade: {u}')
print(f'dezena: {d}')
print(f'centena: {c}')
print(f'milhar: {m}')
