#crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte.
#seu programa deverá ler um numero pelo teclado(entre 0 e 20) e mostra-lo por extenso.

contagem = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez',
            'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove',
            'vinte'
             )   




while True:
    leitura = int(input('Digite um numero: '))

    if 0 <= leitura <= 20:
        print(contagem[leitura])   
        break
    else:
        print('digite apenas numeros de 0 a 20')