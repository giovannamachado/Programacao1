numero_desejado = int(input())
progresso = int(input())
soma = 0


while progresso > 0:
    fatorial = 1
    while progresso > 1:
        fatorial += progresso
        progresso -= 1
    soma += fatorial
    progresso = int(input())

if soma < numero_desejado:
        print('Ainda nos falta um pouco...')
elif soma == numero_desejado:
        print('Pode beijar a noiva, afinal, vocês conseguiram!')
elif numero_desejado < soma < numero_desejado*20:
        print('Parece que os pombinhos passaram um pouco do local...')
elif 20 * numero_desejado < soma <= 100 * numero_desejado:
        print('Acho que nos perdemos um pouco no caminho, onde estamos?')
elif soma > numero_desejado * 100:
        print('Hum... acho que o casal deve rever seus votos de matrimônio...')
else:
    print()