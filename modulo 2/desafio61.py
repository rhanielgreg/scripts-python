# REFAÇA O DESAFIO 51. LENDO O TERMO E A RAZAO DE UMA PA, MOSTRANDO OS 10 PRIMEIROS TERMOS DA 
# PROGRESSAO USANDO A ESTRUTURA WHILE

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
termo = primeiro
contador = 1

while contador <= 10:
    print(f'{termo}, ', end='')
    termo += razao
    contador += 1
print('Fim')