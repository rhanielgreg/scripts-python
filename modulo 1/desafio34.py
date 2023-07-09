# escreva um programa que pergunte o salario de um funcionario e calcule o valor do aumento
# para salarios superiores a 1250 calcule um aumento de 10%
# para salarios inferiores calcule um aumento de 15%

sal = int(input('Digite o seu salario: '))

if sal >= 1250:
    aum = sal + (sal * 0.1)
    print(f'O seu salario com aumento de 10% é de R$ {aum:.2f}')

else:
    aum2 = sal + (sal * 0.15)
    print(f'O Seu salario com aumento de 15% é de R$ {aum2:.2f}')