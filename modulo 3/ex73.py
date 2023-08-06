# crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol.
# Na ordem de colocação.
# Depois mostre:

# A) Apenas os 5 primeiros colocados

# B)_Os ultimos 4 colocados da tabela

# c) uma lista com os times em ordem alfabetica

# d) Em que posicao na tabela está o time da vasco

todos_times = (

'América-MG',
'Athletico-PR',
'Atlético-MG',
'Bahia',
'Botafogo',
'Corinthians',
'Coritiba',
'Cruzeiro',
'Cuiabá',
'Flamengo',
'Fluminense',
'Fortaleza',
'Vasco',
'Grêmio',
'Internacional',
'Palmeiras',
'Bragantino',
'Santos',
'São Paulo',
'Goiás'
               )

print('Os classificados pra a Libertadores são:')
print('-'*20)
print(f' 1- {todos_times[0]} \n 2- {todos_times[1]}\n 3- {todos_times[2]}\n 4- {todos_times[3]}\n'
      f' 5- {todos_times[4]}')
print('-'*20)
      
print('Os ultimos 4 colocados em suas respectivas posições são são:')
print('-'*20)
print(f'{todos_times.index(f"{todos_times[-4]}")}- {todos_times[-4]}\n'
      f'{todos_times.index(f"{todos_times[-3]}")}- {todos_times[-3]}\n' 
      f'{todos_times.index(f"{todos_times[-2]}")}- {todos_times[-2]}\n'
      f'{todos_times.index(f"{todos_times[-1]}")}- {todos_times[-1]}'
    )
print('-'*20)
print('-'*20)
print(f'O time do Vasco está na posição {todos_times.index("Vasco")+1}ª na tabela')
print('-'*20)
print('-'*20)
print(f'Os times em ordem alfabetica: {sorted(todos_times)}')

      
      
      
      
      
  