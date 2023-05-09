import math
def procura_livro(lista_biblioteca, livro, inicio, fim):
    m = math.floor((fim + inicio) /2)
    if fim < inicio:
        return 0
    elif lista_biblioteca[m] == livro:
        return (m+1) * 7
    if livro < lista_biblioteca[m]:
        return procura_livro(lista_biblioteca, livro, inicio, m - 1)
    else:
        return procura_livro(lista_biblioteca, livro, m + 1, fim)

def capicuia(resultado_meio):
    auxiliar = str(resultado_meio)
    auxiliar = auxiliar[::-1]
    if auxiliar == auxiliar[:: -1]:
        return resultado_meio
    else:
        resultado_meio = resultado_meio + int(auxiliar)
        return capicuia(resultado_meio)

lista_livros = []
livro = 'Ghost Potrificationizer - E. Gadd'
quant_livros = int(input())
for i in range(quant_livros):
    livros = input()
    lista_livros.append(livros)

posicao_livro = str(procura_livro(lista_livros, livro, 0, quant_livros - 1))
poder = capicuia(int(posicao_livro))

if posicao_livro == "0":
    print('Mamma mia! Só Mario poderá me salvar agora!')
elif poder < 50:
    print('É uma catástrofe, eu tenho a arma mas só posso usá-la uma vez')
elif 50 <= poder <= 100:
    print('Terei que usar a minha arma com sabedoria!')
elif  100 <= poder <= 200:
    print('A arma está bem carregada, me dei bem!')
elif poder >= 200:
    print('Aha! EU NÃO TENHO MAIS MEDO DE NADA! PODEM VIR!')


