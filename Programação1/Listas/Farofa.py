lista_convidados = []
lista_atualizada = ''
final_lista = ''
contador = False

while contador != True:
    entrada = input()
    if entrada == 'adicionar':
        nome_adicionar, posicao_adicionar = input().split(' ')
        adicionar = int(posicao_adicionar)
        lista_convidados.insert(adicionar,nome_adicionar)
    elif entrada == 'remover':
        nome_remover = input()
        lista_convidados.remove(nome_remover)
    elif entrada == 'atualizar indice':
         atualizacao_nome, atualizacao_indice = input().split(' ')
         for lista_posicao in range(len(lista_convidados)):
             if lista_posicao == int(atualizacao_indice):
                 if lista_convidados[lista_posicao] == atualizacao_nome:
                     print(f'Nada mudou, a lista permanece igual')
                 else:
                     lista_posicao = int(atualizacao_indice)
                     lista_convidados.remove(atualizacao_nome)
                     lista_convidados.insert(int(atualizacao_indice), atualizacao_nome)
    elif entrada == 'imprimir lista atual':
         for palavra in lista_convidados:
             lista_atualizada += palavra
             if palavra != lista_convidados[-1]:
                 lista_atualizada += ' '
         print(lista_atualizada)
         lista_atualizada = ''
    elif entrada == 'lista finalizada':
        for palavra in lista_convidados:
            final_lista += palavra
            if palavra != lista_convidados[-1]:
                final_lista += ' '
        print('A lista ficou da seguinte forma:')
        print(f'{final_lista}')
        contador = True
    else:
        print('Opçao não encontrada')













