quantidade = int(input())
lista_hastags = []
lista_minuscula = ''
analise_palavra_minuscula = False


for i in range(quantidade):
    hastags = input()
    if hastags == hastags.lower():
        lista_hastags.append(hastags)
for j in range(len(lista_hastags) - 1):
    for i in range(len(lista_hastags) - 1):
         if lista_hastags[i] > lista_hastags[i + 1]:
                 lista_hastags[i], lista_hastags[i + 1] = lista_hastags[i + 1], lista_hastags[i]
for palavra in lista_hastags:
    if palavra == lista_hastags[-1]:
        lista_minuscula += palavra
    elif palavra != lista_hastags[-1]:
        lista_minuscula += f'{palavra}\n'
    analise_palavra_minuscula = True
if analise_palavra_minuscula == True:
    print(f'{lista_minuscula}')