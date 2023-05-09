lista_passos = []
passo = ''
while passo != 'FIM':
    passo = input()
    if passo != 'FIM':
      lista_passos.append(passo)

print(f'Olá seguimores! O primeiro passo da dancinha é {lista_passos[0]}')
print(f'Depois, a gente faz o {lista_passos[1]} e {lista_passos[2]}')
print(f'Temos ainda mais {len(lista_passos) - 3} passos pra aprender!')
print(f'Por último, vamos fazer o {lista_passos[-1]}')