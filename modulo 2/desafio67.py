#faça um programa que mostre a tabuada de varios numeros, um de cada vez para cada valor digitado.
# o programa sera interrompido quando o valor solicitado for negativo.

n = 0
while True:
    n = int(input('Digite um valor para gerar a tabuada: '))
    if n < 0:
        break
    for t in range(1,11):
        print(f'{n} x {t} = {n*t}')
   
print('fim do programa')
