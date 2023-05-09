lista_libero = []
lista_levantador = []
lista_central = []
lista_ponteiro = []
lista_oposto = []
lista_jogadores = []
libero = ''
levantador = ''
central = ''
ponteiro = ''
oposto = ''
contador = False

while not contador:
    comando = input()
    if comando == 'adicionar':
        nome, posicao = input().split(': ')
        if posicao == 'Libero':
            lista_libero.append(nome)
            lista_jogadores.append(nome)
            if len(lista_libero) > 2:
                print('ERRO: liberos demais, nao temos uniformes suficientes')
                contador = True
        elif posicao == 'Levantador':
            lista_levantador.append(nome)
            lista_jogadores.append(nome)
            if len(lista_levantador) == 5:
                print(f'Cuidado! voce ja possui 5 levantadores')
        elif posicao == 'Central':
            lista_central.append(nome)
            lista_jogadores.append(nome)
            if len(lista_central) == 5:
                print(f'Cuidado! voce ja possui 5 centrais')
        elif posicao == 'Ponteiro':
            lista_ponteiro.append(nome)
            lista_jogadores.append(nome)
            if len(lista_ponteiro) == 5:
                print(f'Cuidado! voce ja possui 5 ponteiros')
        elif posicao == 'Oposto':
            lista_oposto.append(nome)
            lista_jogadores.append(nome)
            if len(lista_oposto) == 5:
                print(f'Cuidado! voce ja possui 5 opostos')
        if len(lista_jogadores) > 18:
            print('ERRO: voce estrapolou o numero de jogadores')
    elif comando == 'relatorio':
        print('No nosso time ja possuimos:')
        print(f'Liberos: {len(lista_libero)}')
        print(f'Levantadores: {len(lista_levantador)}')
        print(f'Ponteiros: {len(lista_ponteiro)}')
        print(f'Centrais: {len(lista_central)}')
        print(f'Opostos: {len(lista_oposto)}')
        print(f'TOTAL: {len(lista_jogadores)}')
    elif comando == 'nomes':
        posicao_nomes = input()
        libero = '\n'.join(lista_libero)
        levantador = '\n'.join(lista_levantador)
        ponteiro = '\n'.join(lista_ponteiro)
        central = '\n'.join(lista_central)
        oposto = '\n'.join(lista_oposto)
        if posicao_nomes == 'Libero':
            if libero == '':
                print('Ainda nao temos jogadores nessa posicao')
            else:
                print(f'Os liberos sao:')
                print(libero)
        elif posicao_nomes == 'Levantador':
            if levantador == '':
                print('Ainda nao temos jogadores nessa posicao')
            else:
                print(f'Os levantadores sao:')
                print(levantador)
        elif posicao_nomes == 'Central':
            if central == '':
                print('Ainda nao temos jogadores nessa posicao')
            else:
                print(f'Os centrais sao:')
                print(central)
        elif posicao_nomes == 'Ponteiro':
            if ponteiro == '':
                print('Ainda nao temos jogadores nessa posicao')
            else:
                print(f'Os ponteiros sao:')
                print(ponteiro)
        elif posicao_nomes == 'Oposto':
            if oposto == '':
                print('Ainda nao temos jogadores nessa posicao')
            else:
                print(f'Os opostos sao:')
                print(oposto)
    elif comando == 'buscar':
        nome_buscar = input()
        verificacao = False
        for palavra in lista_jogadores:
            if palavra == nome_buscar:
                verificacao = True
        if verificacao == True:
            if nome_buscar == 'Samuel':
                print('Sim, Samuel, voce ja esta na lista de jogadores')
            else:
                print(f'Sim, {nome_buscar} esta na lista de jogadores')
        else:
            if nome_buscar == 'Samuel':
                print('Como voce pode esquecer de si mesmo? Voce nao esta na lista')
            else:
                print(f'O jogador {nome_buscar} nao esta na lista de jogadores')
    elif comando == 'fim':
        contador = True

    else:
        print('***COMANDO INVALIDO***')
if len(lista_libero) == 2 and len(lista_levantador) >= 2 and len(lista_central) >= 2 and len(lista_oposto) >= 2 and \
        len(lista_ponteiro) >= 2 and len(lista_jogadores) <= 18:
    print(f'O Navegantes esta pronto para disputar o Estadual! Desejem sorte aos'
          f' nossos {len(lista_jogadores)} jogadores!')
else:
    print('Quem mandou ficar perdendo tempo com TikTok... Agora o Navegantes nao conseguira jogar o estadual :(')