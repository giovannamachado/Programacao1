pessoas = int(input())
pessoas_lista = []
pessoa = ''
generos_lista = []
genero = ''
lista_feminina = []
feminina = ''
lista_masculina = []
masculina = ''


for i in range(pessoas):
    pessoa, genero = input().split(' - ')
    pessoas_lista.append(pessoa)
    pessoas_lista.append(genero)
    if genero == 'M':
        lista_masculina.append(pessoa)
    else:
        if genero == 'F':
            lista_feminina.append(pessoa)

for nome_m in lista_masculina:
    masculina += f'{nome_m}, '
for nome_f in lista_feminina:
    feminina += f'{nome_f}, '

if len(lista_feminina) == 0:
    print(f'{masculina}Querem cafe?')
    print(f'Serao necessarias {len(lista_masculina)} porcoes de cafe')
elif len(lista_masculina) != 0 and len(lista_feminina) !=0:
    print(f'{masculina}Querem cafe?')
    print(f'{feminina}Desculpa, so pros meninos HAHAHAHAAHHAHAHA')
    print(f'Serao necessarias {len(lista_masculina)} porcoes de cafe')
elif len(lista_masculina) ==0:
    print(f'{feminina}Desculpa, so pros meninos HAHAHAHAAHHAHAHA')
    print(f'Nao tem meninos na lista, nao precisa fazer cafe, Neuma')








