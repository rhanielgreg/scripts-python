# desenvolva um programa que leia o primeiro termo
# e a razao de uma PA.
# No final, mostre os 10 primeiros termos dessa progressao

pt = int(input('Digite o primeiro termo da PA: '))
rz = int(input('Digite a razao: '))

for i in range(10):
    print(pt)
    pt += rz
 
    