# FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SÓ ACEITE OS VALORES 'F' E 'M'.
# CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO NOVAMENTE ATÉ TER UM VALOR CORRETO.

sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = input('Digite seu sexo(F ou M): ').upper()
    if sexo != 'F' and sexo != 'M':
        print(f'{sexo} é um valor INVALIDO, digite um valor valido como M ou F.')
print('Obrigado!')