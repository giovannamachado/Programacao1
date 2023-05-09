quant_rodadas = int(input())

def calculo(quant_rodadas, kills, vivos):
    calcular = (10 * quant_rodadas + kills) - vivos
    return calcular
print(f'Haverá 10 inimigos na rodada 1')

for i in range(quant_rodadas - 1):
    mortes, vivos = input().split(' - ')
    deaths = int(mortes)
    lifes = int(vivos)
    calculo2 = calculo(i+2, deaths, lifes)

    print(f'Haverá {calculo2} inimigos na rodada {i + 2}')
