def frec(quant_moedas, pista, velo_inicial):
    quant = int(quant_moedas)
    velo = int(velo_inicial)
    if quant_moedas == 1:
        return pista
    else:
        return frec(quant_moedas - 1, pista, velo_inicial)

competidor = input()
v_ini = int(input())
pista2 = input()
moedas = int(input())
velocidade_final = 0
calculo = 0
mario_kart = 3
bowsers_castle = 4
moo_moo = 5
yoshi = 6
rainbow = 7

if pista2 == 'Mario Kart Stadium':
    velocidade_final = frec(moedas, pista2, v_ini)
    calculo = moedas * mario_kart + v_ini
    print(f'Correndo na pista {pista2}, {competidor} coletou {moedas} moedas e terminou a corrida na incrivel velocidade de {calculo} km/h.')
elif pista2 == 'Bowsers Castle':
    velocidade_final = frec(moedas,pista2, v_ini)
    calculo = moedas * bowsers_castle + v_ini
    print(f'Correndo na pista {pista2}, {competidor} coletou {moedas} moedas e terminou a corrida na incrivel velocidade de {calculo} km/h.')
elif pista2 == 'Moo Moo Meadows':
    velocidade_final = frec(moedas,pista2,v_ini)
    calculo = moedas * moo_moo + v_ini
    print(f'Correndo na pista {pista2}, {competidor} coletou {moedas} moedas e terminou a corrida na incrivel velocidade de {calculo} km/h.')
elif pista2 == 'Yoshi Valley':
    velocidade_final = frec(moedas,pista2, v_ini)
    calculo = moedas * yoshi + v_ini
    print(f'Correndo na pista {pista2}, {competidor} coletou {moedas} moedas e terminou a corrida na incrivel velocidade de {calculo} km/h.')
elif pista2 == 'Rainbow Road':
    velocidade_final = frec(moedas,pista2, v_ini)
    calculo = moedas * rainbow + v_ini
    print(f'Correndo na pista {pista2}, {competidor} coletou {moedas} moedas e terminou a corrida na incrivel velocidade de {calculo} km/h.')


