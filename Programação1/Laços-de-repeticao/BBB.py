competidores = int(input())

maior_qtd = 0
nome_do_maior = ""
contador = 1

while (contador != competidores):
    nome = input()
    qtd_latinhas = int(input())

    if qtd_latinhas > maior_qtd:
        maior_qtd = qtd_latinhas
        nome_do_maior = nome

    contador += 1

print(f'{nome_do_maior} e o novo anjo!')