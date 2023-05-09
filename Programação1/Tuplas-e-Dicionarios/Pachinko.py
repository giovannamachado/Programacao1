#quantidade preço resgatados
dicionario = {'bichinho de pelucia': [10, 750,0],
                         'boneco articulado com armadura': [20, 1000, 0],
                         'estatua de cena memoravel': [10, 1250, 0],
                         'camiseta tematica': [10, 500, 0],
                         'chaveiro': [50, 250, 0],
                         'bolinhas':[10000, 1000, 0]}

vendas = 0
verificador = False
bolinhas_restantes = 10000
resgates = 0
bolinhas_recebidas = 0
premios_restantes = 100
ienes = 0

while verificador != True:
    comando = input()
    if comando == 'comprar':
        n_bolinhas_compra = int(input())
        if dicionario['bolinhas'][0] >= n_bolinhas_compra:
            dicionario['bolinhas'][0]-= n_bolinhas_compra
            dicionario['bolinhas'][2]+= n_bolinhas_compra
            ienes += n_bolinhas_compra*1000
            vendas += 1
            bolinhas_restantes -= n_bolinhas_compra
            print(f'O jogador comprou {n_bolinhas_compra} bolinhas por {n_bolinhas_compra *1000} ienes.')
        elif dicionario['bolinhas'][0] == 0:
            print('Nao ha mais bolinhas disponiveis, melhor esperar um pouco.')
    elif comando == 'trocar':
        premio, bolinhas_oferecidas = input().split(' - ')
        bolinhas_int = int(bolinhas_oferecidas)
        if premio not in dicionario or dicionario[premio][0] == 0:
            print(f'O jogador veio trocar suas bolinhas mas o premio {premio} nao esta disponivel.')
        elif dicionario[premio][0] > 0 and bolinhas_int >= dicionario[premio][1]:
            dicionario[premio][0] -= 1
            dicionario[premio][2] += 1
            resgates += 1
            bolinhas_restantes += dicionario[premio][1]
            bolinhas_recebidas += dicionario[premio][1]
            premios_restantes -= 1
            print(f'O jogador trocou {dicionario[premio][1]} bolinhas por um {premio}.')
        elif dicionario[premio][0] > 1 and bolinhas_int <= dicionario[premio][1]:
            print(f'O jogador precisa de mais {dicionario[premio][1] - bolinhas_int } bolinhas para trocar por um {premio}.')
    if comando == 'hora de fechar':
        verificador = True

print()

print(f'O resumo do dia foi:\nArrecadado: {ienes} ienes em {vendas} vendas;\nBolinhas: {bolinhas_restantes} restantes;\nResgates feitos: {resgates};\nBolinhas recebidas: {bolinhas_recebidas};\nPremios: {premios_restantes} restantes;\nDeu a hora, amanha tem mais!')












