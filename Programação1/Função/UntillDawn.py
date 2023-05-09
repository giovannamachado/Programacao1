#parte 1 codigo = interecao x ou o
LISTA_PERSONAGENS = ['Sam', 'Chris', 'Ashley', 'Jessica', 'Mike', 'Emily', 'Matt']

matriz = [[-1,5,5,5,5,5,5],
          [5,-1,6,5,5,5,5],
          [5,6,-1,5,5,5,5],
          [5,5,5,-1,7,4,5],
          [5,5,5,7,-1,3,4],
          [5,5,5,4,3,-1,7],
          [5,5,5,5,4,7,-1]]


vivos = ['Sam', 'Chris', 'Ashley', 'Jessica', 'Mike', 'Emily', 'Matt']
mortos = []

def interacao(matriz_interacao, p1, inten, p2):
        if inten == 'X':
            matriz_interacao[p1][p2], matriz_interacao[p2][p1] = matriz_interacao[p1][p2] - 1, matriz_interacao[p2][p1] -1
            return matriz_interacao[p1][p2]
        elif inten == 'O':
            matriz_interacao[p1][p2], matriz_interacao[p2][p1] = matriz_interacao[p1][p2] + 1, matriz_interacao[p2][p1] +1
            return matriz_interacao[p1][p2]
        return  False

#media coom 1 nome
def media_aritmetica(matriz_relacionameto, nome1):
        calculo = (sum(matriz_relacionameto[LISTA_PERSONAGENS.index(nome1)]) / 6)
        return calculo

num_interacoes = int(input())

for _ in range(num_interacoes):
    nome1, tipo_interacao, nome2 = input().split(' ')
    posicao1 = LISTA_PERSONAGENS.index(nome1)
    posicao2 = LISTA_PERSONAGENS.index(nome2)
    print(interacao(matriz,posicao1, tipo_interacao, posicao2))

# parte 2 = parte dinamica

num_dinamica = int(input())

for b in range(num_dinamica):
    nome = input().split(' - ')
    if len(nome) == 1:
        primeira = nome[0]
        if primeira in mortos:
            print("entrada invalida!!! voce so pode jogar com jogadores vivos")
        else:
            media = media_aritmetica(matriz,primeira)
            if media > 5:
                print(f'UFA!!! foi por pouco mas {primeira} conseguiu escapar do Wendigo.')
            else:
                print(f'{primeira} infelizmente nao conseguiu sobreviver ao ataque do Wendigo.')
                mortos.append(primeira)
    else:
        primeira = nome[0]
        segunda = nome[1]
        if primeira in mortos or segunda in mortos:
            print("entrada invalida!!! voce so pode jogar com jogadores vivos")
        else:
            indice = matriz[LISTA_PERSONAGENS.index(primeira)][LISTA_PERSONAGENS.index(segunda)]
            if indice > 6:
                print(f'felizmente {primeira} ajudou {segunda} a escapar do Wendigo.')
            else:
                print(f'que pena! {primeira} nao conseguiu ajudar {segunda} do ataque do Wendigo.')
                mortos.append(primeira)

for d in vivos:
    vivo = vivos[LISTA_PERSONAGENS.index(d)]
    if vivo in vivos:
        vivos.append(d)

if len(vivos) > 0:
    print('Sobreviventes')
    for b in vivos:
        print(b)
else:
    print("Tristemente, ninguém sobreviveu")

















