def palindromo(pa):
    if len(pa) <= 1 and len(pa) == 0:
        return True
    else:
        return pa[0] == pa[-1] and palindromo(pa[1:-1]) #compactando a palavra

quant_pistas = int(input())
verificador = False

for i in range(0,quant_pistas):
    pistas = input()
    pista = list(pistas)
    final = 0
    comeco = 0
    terminar = False
    while not terminar:
        if len(pista) == 0:
            terminar = True
        elif pista[-1] == 'a':
            pista.pop(-1)
            final += 1
        elif pista[0] == 'a':
            pista.pop(0)
            comeco += 1
        else:
            terminar = True

    if final >= comeco:
        if palindromo(pista) == True:
            verificador = True
        else:
          verificador = False
          break

if verificador == True:
    print('ACHEI!!! Peach, estou a caminho.')
else:
    print('Essa não!!! Estou na direção errada.')


