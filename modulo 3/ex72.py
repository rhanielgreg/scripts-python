#crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte.
#seu programa deverá ler um numero pelo teclado(entre 0 e 20) e mostra-lo por extenso.

contagem = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez',
            'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove',
            'vinte'
             )   




while True: #abre loop com while true
    entrada = input('Digite um numero: ') # input aceitando qualquer caractere digitado

    if entrada.isdigit(): #confere se o campo de entrada é str 
        leitura = int(entrada) # se for str, converte em int
        if 0 <= leitura <= 20: #confere se a int leitura esta entre 0 e 20
            print(contagem[leitura])   #mostra o numero int por extenso, localizado na tupla
            break
        else:
            print('digite apenas numeros de 0 a 20') #mostra um erro caso seja digitado um numero diferente do pedido

    print('Erro: digite apenas NÚMEROS validos') #mostra um erro caso seja digitado letras ao inves de numeros