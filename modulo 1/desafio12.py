#faca um algoritmo que leia o preco do produto e mostre seu novo preco com 5% de desconto.

p = int(input('Digite o preco do produto: '))
d = p-((p*5)/100)
print(f'O produto com desconto é de {d}')