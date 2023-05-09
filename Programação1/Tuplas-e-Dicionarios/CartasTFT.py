dicionario_tft = dict()

for i in range(0,5):
    carta, custo = input().split(' - ')
    dicionario_tft.update({carta: custo})

dicionario_tft = dict(sorted(dicionario_tft.items(), key= lambda item: item[1]))
for i in dicionario_tft:
    print(f'{i} - {dicionario_tft[i][0]}')





