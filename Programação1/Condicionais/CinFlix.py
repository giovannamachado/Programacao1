cartegoria = input()
genero = input()

#Filmes genero
genero_filme1 = 'Acao'
genero_filme2 = 'Terror'
genero_filme3 = 'Drama'
genero_filme4 = 'Romance'
genero_filme5 = 'Aventura'
genero_filme6 = 'Animacao'
genero_filme7 = 'Comedia'
genero_filme8 = 'Fantasia'
genero_filme9 = 'Suspense'
genero_filme10 = 'Policial'
genero_filme11 = 'Ficcao'

#Filmes nomes
filme_nome1 = 'Kill Bill Vol. I'
filme_nome2 = 'It - A Coisa'
filme_nome3 = 'Sempre ao Seu Lado'
filme_nome4 = 'Me Chame Pelo Seu Nome'
filme_nome5 = 'Homem - Aranha: Sem Volta para Casa'
filme_nome6 = 'Encanto'
filme_nome7 = 'Nao Olhe Para Cima'
filme_nome8 = 'Harry Potter e a Pedra Filosofal'
filme_nome9 = 'Corra!'
filme_nome10 = 'Cidade de Deus'
filme_nome11 = 'Interestelar'

#Series genero
genero_serie1 = 'Acao'
genero_serie2 = 'Terror'
genero_serie3 = 'Drama'
genero_serie4 = 'Romance'
genero_serie5 = 'Aventura'
genero_serie6 = 'Animacao'
genero_serie7 = 'Comedia'
genero_serie8 = 'Fantasia'
genero_serie9 = 'Suspense'
genero_serie10 = 'Policial'
genero_serie11 = 'Ficcao'

#serie nomes
serie_nome1 = 'The Boys'
serie_nome2 = 'A Maldicao da Residencia Hill'
serie_nome3 = 'Euphoria'
serie_nome4 = 'Bridgerton'
serie_nome5 = 'The Witcher'
serie_nome6 = 'Arcane'
serie_nome7 = 'FRIENDS'
serie_nome8 = 'Game Of Thrones'
serie_nome9 = 'Prison Break'
serie_nome10 = 'Peaky Blinders'
serie_nome11 = 'Dark'

# condicionais filmes
if (cartegoria == 'Filme' and genero == genero_filme1): # kill bill
    print(filme_nome1, 'e o filme mais popular do genero', genero_filme1, 'no momento.')
elif (cartegoria == 'Filme' and genero == genero_filme2):
    print(filme_nome2, 'e o filme mais popular do genero', genero_filme2, 'no momento.')
elif (cartegoria == 'Filme' and genero == genero_filme3):
    print(filme_nome3, 'e o filme mais popular do genero', genero_filme3, 'no momento.')
elif (cartegoria == 'Filme' and genero == genero_filme4):
    print(filme_nome4, 'e o filme mais popular do genero', genero_filme4, 'no momento.')
elif (cartegoria == 'Filme' and genero == genero_filme5):
    print(filme_nome5, 'e o filme mais popular do genero', genero_filme5, 'no momento.')
elif (cartegoria == 'Filme' and genero == genero_filme6):
    print(filme_nome6, 'e o filme mais popular do genero', genero_filme6, 'no momento.')
elif (cartegoria == 'Filme' and genero == genero_filme7):
    print(filme_nome7, 'e o filme mais popular do genero', genero_filme7, 'no momento.')
elif (cartegoria == 'Filme' and genero == genero_filme8):
    print(filme_nome8, 'e o filme mais popular do genero', genero_filme8, 'no momento.')
elif (cartegoria == 'Filme' and genero == genero_filme9):
    print(filme_nome9, 'e o filme mais popular do genero', genero_filme9, 'no momento.')
elif (cartegoria == 'Filme' and genero == genero_filme10):
    print(filme_nome10, 'e o filme mais popular do genero', genero_filme10, 'no momento.')
elif (cartegoria == 'Filme' and genero == genero_filme11):
    print(filme_nome11, 'e o filme mais popular do genero', genero_filme11, 'no momento.')
#Condicionais Series
elif(cartegoria == 'Serie' and genero == genero_serie1):
    print(serie_nome1, 'e a serie mais popular do genero', genero_serie1, 'no momento.')
elif(cartegoria == 'Serie' and genero == genero_serie2):
    print(serie_nome2, 'e a serie mais popular do genero', genero_serie2, 'no momento.')
elif(cartegoria == 'Serie' and genero == genero_serie3):
    print(serie_nome3, 'e a serie mais popular do genero', genero_serie3, 'no momento.')
elif(cartegoria == 'Serie' and genero == genero_serie4):
    print(serie_nome4, 'e a serie mais popular do genero', genero_serie4, 'no momento.')
elif(cartegoria == 'Serie' and genero == genero_serie5):
    print(serie_nome5, 'e a serie mais popular do genero', genero_serie5, 'no momento.')
elif(cartegoria == 'Serie' and genero == genero_serie6):
    print(serie_nome6, 'e a serie mais popular do genero', genero_serie6, 'no momento.')
elif(cartegoria == 'Serie' and genero == genero_serie7):
    print(serie_nome7, 'e a serie mais popular do genero', genero_serie7, 'no momento.')
elif(cartegoria == 'Serie' and genero == genero_serie8):
    print(serie_nome8, 'e a serie mais popular do genero', genero_serie8, 'no momento.')
elif (cartegoria == 'Serie' and genero == genero_serie9):
    print(serie_nome9, 'e a serie mais popular do genero', genero_serie9, 'no momento.')
elif (cartegoria == 'Serie' and genero == genero_serie10):
    print(serie_nome10, 'e a serie mais popular do genero', genero_serie10, 'no momento.')
elif (cartegoria == 'Serie' and genero == genero_serie11):
    print(serie_nome11, 'e a serie mais popular do genero', genero_serie11, 'no momento.')
else:
    print()