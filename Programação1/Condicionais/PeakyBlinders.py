numero = int(input())

arma_1 = str('Cassetete')
arma_2 = str('Garrafa de Whisky')
arma_3 = str('Soco Ingles')
arma_4 = str('Lamina Escondida')
arma_5 = str('Pe de Cabra')
arma_6 = str('Canivete')

tipo_1 = str('atordoante')
tipo_2 = str('cortante')

if (numero == 1):
    print(f'A arma corpo a corpo escolhida foi: {arma_1}')
    print(f'A arma corpo a corpo escolhida e {tipo_1}')
elif (numero == 2):
    print(f'A arma corpo a corpo escolhida foi: {arma_2}')
    print(f'A arma corpo a corpo escolhida e {tipo_2}')
elif(numero == 3):
    print(f'A arma corpo a corpo escolhida foi: {arma_3}')
    print(f'A arma corpo a corpo escolhida e {tipo_1}')
elif (numero == 4):
    print(f'A arma corpo a corpo escolhida foi: {arma_4}')
    print(f'A arma corpo a corpo escolhida e {tipo_2}')
elif (numero == 5):
    print(f'A arma corpo a corpo escolhida foi: {arma_5}')
    print(f'A arma corpo a corpo escolhida e {tipo_1}')
elif (numero == 6):
    print(f'A arma corpo a corpo escolhida foi: {arma_6}')
    print(f'A arma corpo a corpo escolhida e {tipo_2}')
else:
    print('Numero invalido')
