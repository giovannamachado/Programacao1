quant_frases = int(input())

def palindromo(pa):
    pa = pa.replace(' ', '')
    inverter = pa[::-1]
    if pa == inverter:
        return True
    return False

def pangrama(pan):
    alfabeto = 'abcdefghijlmnopqrstuvxz'
    for letra in alfabeto:
        if letra not in pan.lower():
            return False
    return True

def epizeuxis():
    repetidas = 0
    for i in separado:
        contador = separado.count(i)
        if contador > 1:
            repetidas += 1
        if repetidas > 1:
            return True
    return False


for i in range(quant_frases):
    frases = input()
    separado = frases.split()
    espaco = frases.replace(' ', '')

    if palindromo(frases):
        print(f'Freddy, "{frases}" é um palíndromo!')
    elif pangrama(frases):
        print(f'Tenho certeza de que "{frases}" é um pangrama!')
    elif epizeuxis():
        print(f'Freddy, Freddy, "{frases}" é definitivamente uma epizeuxe!')
    else:
        print('Essa aqui é uma pegadinha, não há nada aqui!')