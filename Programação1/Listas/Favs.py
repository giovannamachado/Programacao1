numeros_tiktokers = int(input())
lista_nomes = []
lista_seguidores = []

for i in range(numeros_tiktokers):
    nomes_seguidores = input().split('-')
    lista_nomes.append(nomes_seguidores[0])
    lista_seguidores.append(int(nomes_seguidores[1]))

for j in range (numeros_tiktokers - 1):
    for i in range(numeros_tiktokers - 1):
        if lista_seguidores[i] > lista_seguidores[i+1]:
            lista_seguidores[i], lista_seguidores[i+1] = lista_seguidores[1+i], lista_seguidores[i]
            lista_nomes[i], lista_nomes[i+1] = lista_nomes[i+1], lista_nomes[i]
        elif lista_seguidores[i] == lista_seguidores[1+1]:
            if len(lista_nomes[i]) > len(lista_nomes[i+1]):
                lista_nomes[i], lista_nomes[i+1] = lista_nomes[1+i], lista_nomes[i]
                lista_seguidores[i], lista_seguidores[i + 1] = lista_seguidores[1 + i], lista_seguidores[i]
          
            
            

for i in range(numeros_tiktokers):
    print(f'{lista_nomes[i]}-{lista_seguidores[i]}')

