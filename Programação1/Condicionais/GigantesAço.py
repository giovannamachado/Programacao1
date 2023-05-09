nome_boxeador1 = str(input())
vida_boxeador1 = int(input())
ataque_boxeador1 = int(input())
defesa_boxeador1 = int(input())
nome_boxeador2 = str(input())
vida_boxeador2 = int(input())
ataque_boxeador2 = int(input())
defesa_boxeador2 = int(input())

nome_boxeador1 = nome_boxeador1.upper()
nome_boxeador2 = nome_boxeador2.upper()

golpe1 = input()
defesa1 = input()

print('Round 1')
#round1 jogador1 atacando jab
if(golpe1 == 'jab' and  defesa1 == 'X'):
    vida_boxeador2 -=  ataque_boxeador1
    if(vida_boxeador2 <= 0):
        print('NOSSO CAMPEAO E', nome_boxeador1, 'COM UM INCRIVEL NOCAUTE NO PRIMEIRO ROUND')
elif(golpe1 == 'jab' and defesa1 == 'bloqueio'):
         vida_boxeador2 -= (ataque_boxeador1 - (ataque_boxeador1 * defesa_boxeador2 / 100))
         if (vida_boxeador2 <= 0):
            print('NOSSO CAMPEAO E', nome_boxeador1, 'COM UM INCRIVEL NOCAUTE NO PRIMEIRO ROUND')
elif (golpe1 == 'jab' and defesa1 == 'esquiva'):
        ataque_boxeador2 = ataque_boxeador2 + (ataque_boxeador2 * 0.1)
        if (vida_boxeador2 <= 0):
            print('NOSSO CAMPEAO E', nome_boxeador1, 'COM UM INCRIVEL NOCAUTE NO PRIMEIRO ROUND')
    # Round 1 jogador 1 ataca direto
elif (golpe1 == 'direto' and defesa1 == 'X'):
        vida_boxeador2 -= ataque_boxeador1 *1.4
        if (vida_boxeador2 <= 0):
            print('NOSSO CAMPEAO E', nome_boxeador1, 'COM UM INCRIVEL NOCAUTE NO PRIMEIRO ROUND')
elif (golpe1 == 'direto' and defesa1 == 'bloqueio'):
        vida_boxeador2 -= (ataque_boxeador1 * 1.3 - (ataque_boxeador1 * defesa_boxeador2 / 100))
        if (vida_boxeador2 <= 0):
            print('NOSSO CAMPEAO E', nome_boxeador1, 'COM UM INCRIVEL NOCAUTE NO PRIMEIRO ROUND')
elif (golpe1 == 'direto' and defesa1 == 'esquiva'):
        ataque_boxeador2 = ataque_boxeador2 + (ataque_boxeador2 * 0.2)
        if (vida_boxeador2 <= 0):
            print('NOSSO CAMPEAO E', nome_boxeador1, 'COM UM INCRIVEL NOCAUTE NO PRIMEIRO ROUND')
#round 2 jogador 2 atancando com jab
if(vida_boxeador2 > 0):
  golpe2 = input()
  defesa2 = input()
  print('Round 2')
  if(golpe2 == 'jab' and defesa2 == 'X'):
     vida_boxeador1 -= ataque_boxeador2 
     if(vida_boxeador1 <= 0):
         print('NOSSO CAMPEAO E', nome_boxeador2)
  elif(golpe2 == 'jab' and defesa2 == 'bloqueio'):
    vida_boxeador1 -= (ataque_boxeador2 - (ataque_boxeador2 * defesa_boxeador1 / 100))
    if (vida_boxeador1 <= 0):
        print('NOSSO CAMPEAO E', nome_boxeador2)
  elif(golpe2 == 'jab' and defesa2 == 'esquiva'):
     ataque_boxeador1 = ataque_boxeador1 + (ataque_boxeador1 * 0.1)
     if (vida_boxeador1 <= 0):
                print('NOSSO CAMPEAO E', nome_boxeador2)
        # roud 2 jogador2 ataca direto
  elif(golpe2 == 'direto' and defesa2 == 'X'):
      vida_boxeador1 -= ataque_boxeador2 * 1.4
      if(vida_boxeador1 <= 0):
         print('NOSSO CAMPEAO E', nome_boxeador2)
  elif(golpe2 == 'direto' and defesa2 == 'bloqueio'):
      vida_boxeador1 -= (ataque_boxeador2 * 1.3 - (ataque_boxeador2 * defesa_boxeador1 / 100))
      if (vida_boxeador1 <= 0):
        print('NOSSO CAMPEAO E', nome_boxeador2)
  elif(golpe2 == 'direto' and defesa2 == 'esquiva'):
      ataque_boxeador1 = ataque_boxeador1 + (ataque_boxeador1 * 0.2)
      if (vida_boxeador1 <= 0):
       print('NOSSO CAMPEAO E', nome_boxeador2)
  if(vida_boxeador1 > 0):
#roud3 jogadorr 1 ataca jab
    if(vida_boxeador1 > 0):
        golpe3 = input()
        defesa3 = input()
        print('Round 3')
        print(nome_boxeador1, 'SO TEM MAIS UM ROUND PARA DERRUBAR SEU ADVERSARIO')
    if(golpe3 == 'jab' and  defesa3 == 'X'):
        vida_boxeador2 -=  ataque_boxeador1 
        if(vida_boxeador2 <= 0):
            print('NOSSO CAMPEAO E', nome_boxeador1)
    elif(golpe3 == 'jab' and defesa3 == 'bloqueio'):
        vida_boxeador2 -= (ataque_boxeador1 - (ataque_boxeador1 * defesa_boxeador2/100))
        if(vida_boxeador2 <= 0):
         print('NOSSO CAMPEAO E', nome_boxeador1)
    elif(golpe3 ==' jab' and defesa3 == 'esquiva'):
         ataque_boxeador2 = ataque_boxeador2 + (ataque_boxeador2 * 0.1)
         if(vida_boxeador2 <= 0):
            print('NOSSO CAMPEAO E', nome_boxeador1)
    #Round 3 jogador1 ataca direto
    elif(golpe3 == 'direto' and defesa3 == 'X'):
         vida_boxeador2 -= ataque_boxeador1 * 1.4
         if (vida_boxeador2 <= 0):
               print('NOSSO CAMPEAO E', nome_boxeador1)
    elif(golpe3 == 'direto' and defesa3 == 'bloqueio'):
         vida_boxeador2 -= (ataque_boxeador1 * 1.3 - (ataque_boxeador1 * defesa_boxeador2 / 100))
         if (vida_boxeador2 <= 0):
              print('NOSSO CAMPEAO E', nome_boxeador1)
    elif(golpe3 == ' direto' and defesa3 == 'esquiva'):
         ataque_boxeador2 = ataque_boxeador2 + (ataque_boxeador2 * 0.2)
         if (vida_boxeador2 <= 0):
              print('NOSSO CAMPEAO E', nome_boxeador1)
    if(vida_boxeador1 > 0 and vida_boxeador2 > 0):
        print('NOSSO CAMPEAO E', nome_boxeador2)