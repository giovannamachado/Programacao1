palavra = 'prova-do-anjo-bbb'.upper()
acertos = 0
erros = 0
tentativas = 3
letras_acertadas = ''
letras_erradas = ''
letra_usadas = ''
contador = 0

while acertos != 9 and erros != 3:
    letra_digitada = input().upper()
    letra_contida = False
    letra_ja_foi_digitada = False

    for letra in letra_usadas:
        if letra == letra_digitada:
            letra_ja_foi_digitada = True
    if letra_ja_foi_digitada == True:
        print(f'Voce ja digitou a letra {letra_digitada.upper()}')


    if letra_ja_foi_digitada == False:
        for letra in palavra:
            if letra == letra_digitada:
                letra_contida = True


        if letra_contida == True:
            print('Parabens, voce conseguiu mais uma letra!')
            letras_acertadas += letra_digitada
            letra_usadas += letra_digitada
            acertos += 1
        else:
            tentativas -= 1
            if tentativas != 0:
                print(f'Que pena, voce tem mais {tentativas} chances!')
            letras_erradas += letra
            letra_usadas += letra_digitada
            erros += 1

    letra_verificada = False
    if tentativas != 0:
        mensagem = ''
        for posicao_em_palavra in palavra:
            for posicao_em_acertadas in letras_acertadas:
                if posicao_em_palavra == posicao_em_acertadas:
                    letra_verificada = True

            if letra_verificada == True:
                mensagem += f'{posicao_em_palavra}'
                letra_verificada = False
            else:
                mensagem += '-'
        print(mensagem)
    contador += 1

if tentativas > 0:
    print('Boa, voce e o novo Anjo da semana!')
else:
    print('Fim de jogo, sem almoco do anjo pra voce!')