# crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem
# no final, de acordo com a media atingida.

#media abaixo de 5.0 - reprovado
#media entre 5.0 e 6.9 - recuperacao
#media 7.0 ou superior - aprovado

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
med = (n1 + n2) / 2


if med < 5:
    print(f'Sua media foi {med} e por isso voce foi REPROVADO')

elif med >= 7:
    print(f'Sua media foi {med} e por isso voce foi APROVADO')

else:
    print(f'Sua media foi {med} e por isso voce esta de RECUPERACAO')