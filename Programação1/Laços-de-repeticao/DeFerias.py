numero_festas = int(input())
mais_bebida = 0
quantidade_cerveja= 0
quantidade_caipirinha = 0
quantidade_vodca = 0
soma1 = 0
soma2 = 0
soma3 = 0


for i in range(numero_festas):
    numero_copos = int(input())
    for j in range(numero_copos):
        bebida = input()
        if bebida == 'cerveja':
            quantidade_cerveja += 1
        elif bebida == 'caipirinha':
            quantidade_caipirinha += 1
        elif bebida == 'vodca':
            quantidade_vodca += 1

    if quantidade_cerveja > quantidade_caipirinha and quantidade_cerveja > quantidade_vodca:
        print(f'O que ele mais tomou nessa festa foi: cerveja')
    elif quantidade_caipirinha > quantidade_cerveja and quantidade_caipirinha > quantidade_vodca:
        print(f'O que ele mais tomou nessa festa foi: caipirinha')
    elif quantidade_vodca > quantidade_cerveja and quantidade_vodca > quantidade_caipirinha:
        print(f'O que ele mais tomou nessa festa foi: vodca')

    soma1 += quantidade_cerveja
    soma2 += quantidade_caipirinha
    soma3 += quantidade_vodca

    quantidade_cerveja = 0
    quantidade_caipirinha = 0
    quantidade_vodca = 0

print(f'cerveja - {soma1}')
print(f'caipirinha - {soma2}')
print(f'vodca - {soma3}')






















