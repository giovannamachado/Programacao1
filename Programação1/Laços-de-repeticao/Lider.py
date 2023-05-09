letra_sorteada = input()
participante = int(input())
quantidade_letra = 0
ganhador = ''
maior_quantidade = 0
palavra_ganhadora = ''

for i in range(participante):
    nome_participante, palavra = str(input()).split("-")
    for letra in palavra:
        if letra == letra_sorteada:
            quantidade_letra += 1
    if quantidade_letra > maior_quantidade:
        maior_quantidade = quantidade_letra
        ganhador = nome_participante
        palavra_ganhadora = palavra
    quantidade_letra = 0


if ganhador != 'Prior':
    print(f'Vish! O Mago Prior pode ir pro paredao, ja que quem ganhou foi {ganhador}, com a palavra {palavra_ganhadora} e {maior_quantidade} aparicoes da letra {letra_sorteada}.')
elif ganhador == 'Prior':
    print(f'Joga y joga! Mago Prior e o novo lider com a palavra {palavra_ganhadora} com {maior_quantidade} aparicoes da letra {letra_sorteada}.')
else:
    print()











