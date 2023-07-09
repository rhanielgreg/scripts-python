#faca um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento

sal = int(input('Digite seu salario atual: '))
por = 15
aum = sal+((sal*por)/100)
print(f'Seu salario com adicional de {por}% é de {aum}')

