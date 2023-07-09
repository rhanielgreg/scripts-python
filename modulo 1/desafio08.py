#escreva um programa que leia em metros e exiba convertido em centimetros e milimetros

m = int(input('Digite uma metragem: '))
cm = m*100
mm = cm*10

print(f'{m} equivale a: \n {cm} centimetros\n {mm} milimetros.')