rating_beth = int(input())
rating_adversario = int(input())
resultado_partida = str(input())

vitoria = int(1)
empate = float(0.5)
n = int(empate)
derrota = int(0)

probabilidade = (1 / (1 + 10**((rating_adversario - rating_beth) / 400)))

if (resultado_partida == 'vitoria'):
    novo_rating = (rating_beth + 40 * (vitoria - probabilidade))
    print('O novo rating da Beth Harmon é', int(novo_rating))
elif(resultado_partida == 'empate'):
    novo_rating2 = int(rating_beth + 40 * (empate - probabilidade))
    print('O novo rating da Beth Harmon é',int(novo_rating2))
elif(resultado_partida == 'derrota'):
    novo_rating3 = int(rating_beth + 40 * (derrota - probabilidade))
    print('O novo rating da Beth Harmon é',int(novo_rating3))
else:
    print("Resultado da partida invalido")