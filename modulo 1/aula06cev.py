v = input('Digite qualquer valor: ')
print(f'o tipo primitivo que voce digitou eh {type(v)}')
print(f'o que foi digitado eh um numero? {v.isnumeric()}')
print(f'o que foi digitado eh alfabetico? {v.isalpha()}')
print(f'o que foi digitado eh alfa-numerico? {v.isalnum()}')
print(f'o que foi digitado esta todo em maiusculo? {v.isupper()}')
print(f'o que foi digitado eh um espaco? {v.isspace()}')
print(f'o que foi digitado comeca com letra maiuscula? {v.istitle()}')
print(f'o que foi digitado esta todo em letra minuscula? {v.islower()}')
 